
This directory contains script which apply fixes/transformation to the whole stub codebase.

The scripts are designed so that they can be run multiple times on the codebase without damage, meaning
they will only fix what has not already been fixed.

The naming `collect_XXX` indicates that the script will collect information into a JSON file, to be reviewed. The
next script with a naming `apply_XXX` takes the JSON file as input and performs the code transformation.


