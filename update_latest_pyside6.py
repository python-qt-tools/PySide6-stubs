"""Generate the upstream stubs."""
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import os
from pathlib import Path
from typing import List, Set, Tuple

# from libcst import MetadataWrapper, parse_module

from version import PYSIDE6_VERSION, PYSIDE6_VERSION_STR

BASE_DIR = Path(__file__).parent
PATH_STUBS_PYSIDE6 = BASE_DIR / 'PySide6-stubs'
PATH_STUBS_SHIBOKEN6 = BASE_DIR / 'shiboken6-stubs'

PLATFORM_WINDOWS = "win_amd64"
PLATFORM_LINUX   = "manylinux_2_28_x86_64"
PLATFORM_MACOSX  = "macosx_10_9_universal2"

BRANCH_WINDOWS = 'upstream-pyside6-windows'
BRANCH_LINUX   = 'upstream-pyside6-linux'
BRANCH_MACOSX  = 'upstream-pyside6-macosx'

PYSIDE6_ESSENTIALS = "PySide6_Essentials"
PYSIDE6_ADDONS     = "PySide6_Addons"
PYSIDE6_SHIBOKEN   = "shiboken6"

def git_current_branch() -> str:
    '''Return the current git branch'''
    branches = subprocess.check_output(['git', 'branch'], text=True).splitlines()
    current_branch = [br for br in branches if br.startswith('* ')][0][2:]
    return current_branch


def download_stubs(download_folder: Path, platform: str, branch_name: str) -> None:
    """Download the stubs and copy them to pyside6-stubs folder."""
    current_branch = git_current_branch()
    print(f'Git checkout branch {branch_name}')
    subprocess.check_call(['git', 'checkout', branch_name])

    download_folder = download_folder.absolute()

    download_cmd = [
        sys.executable,
        "-m",
        "pip",
        "download",
        "-d",
        str(download_folder),
    ]
    if platform:
        download_cmd += [
            "--platform",
            platform,
            '--no-deps',
        ]
    for stub_name, target_folder in [
        (PYSIDE6_ESSENTIALS, PATH_STUBS_PYSIDE6),
        (PYSIDE6_ADDONS, PATH_STUBS_PYSIDE6),
        (PYSIDE6_SHIBOKEN, PATH_STUBS_SHIBOKEN6),
    ]:
        print(f'Downloading wheel {stub_name} for {platform}')
        output = subprocess.run(download_cmd + [
                f"{stub_name}=={'.'.join((str(nbr) for nbr in PYSIDE6_VERSION))}",
            ],
            env={
                #                'https_proxy' : 'http://xxx.xxx.xxx.xxx:80/',
                **os.environ
            },
            capture_output=True,
            text=True,
            check=True,
        ).stdout

        mo = re.search(r'^\s*(Saved|File was already downloaded) (.*)\s*$', output, flags=re.MULTILINE)
        if not mo:
            print(f'Could not find our re in the following output\n<<<\n{output}\n>>>')
            sys.exit(-1)

        wheel_fname = mo.group(2)
        assert stub_name.lower() in wheel_fname.lower()
        assert platform.lower() in wheel_fname.lower()

        # Extract the upstream pyi files
        with tempfile.TemporaryDirectory() as temp_folder_str:
            temp_folder = Path(temp_folder_str)
            print(f"Created temporary directory {temp_folder}")
            print(f"Extracting file {wheel_fname}")
            with zipfile.ZipFile(wheel_fname, "r") as zip_ref:
                zip_ref.extractall(temp_folder)

            target_folder.mkdir(exist_ok=True)

            # Take every pyi file from all folders and move it to "pyside6-stubs"
            for folder in temp_folder.glob("*"):
                print(f"Scanning folder for pyi files {folder}")
                for extracted_file in folder.glob("*.pyi"):
                    print(f"Copying {extracted_file.name} to {target_folder}")
                    copy_file = target_folder / extracted_file.name
                    shutil.copyfile(extracted_file, copy_file)

        # commit new files to branch name
        os.chdir(target_folder)
        print(f'Git add new files')
        subprocess.call(['git', 'add', target_folder])

    print(f'Git commit new files')
    subprocess.call(['git', 'commit', '-m', f'Upgrading upstream to version {PYSIDE6_VERSION_STR}'])
    print(f'Commit of new version to {target_folder} done')
    print(f'Restoring git branch {current_branch}')
    subprocess.check_call(['git', 'checkout', current_branch])



if __name__ == "__main__":
    # Create pyside6-stubs folder if necessary
    BASE_DIR.mkdir(exist_ok=True)

    incoming = Path(__file__).parent / 'incoming'
    incoming.mkdir(exist_ok=True)

    # Download required packages
    download_stubs(incoming, PLATFORM_WINDOWS, BRANCH_WINDOWS)
    download_stubs(incoming, PLATFORM_LINUX, BRANCH_LINUX)
    download_stubs(incoming, PLATFORM_MACOSX, BRANCH_MACOSX)
