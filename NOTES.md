
Food for thought, possible improvements:


## enum

All Qt enum are actually integers like

    class ExitStatus(enum.Enum):

        NormalExit               : QProcess.ExitStatus = ... # 0x0
        CrashExit                : QProcess.ExitStatus = ... # 0x1

The following code will work in python:

    v = QProcess.ExitStatus.NormalExit.value

But it won't typecheck...

One way to address this is to lie and pretend there are IntEnum

    class ExitStatus(enum.IntEnum):

        NormalExit               : QProcess.ExitStatus = ... # 0x0
        CrashExit                : QProcess.ExitStatus = ... # 0x1

Should we do this for all Qt enums ?
