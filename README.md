# Replica
A command line Python script that syncronizes two directories.


Features:
- One-way sync (source acts as a complete reference)
- Periodic sync (period set in CLI)
- Creates a logs/ directory and logs all file actions while syncing

Usage:
```
replica.py [-h] SOURCE_DIR DESTINATION_DIR SYNC_PERIOD

Creates a replica of a specified directory

positional arguments:
  SOURCE_DIR       path to source directory to be replicated
  DESTINATION_DIR  path to directory to put replica into
  SYNC_PERIOD      syncronization period in seconds

optional arguments:
  -h, --help       show help message and exit
```

Script takes both relative and absolute paths as arguments.

The maximum sync period depends on each individual machine, but is rather large.


Please note that the files are not updated based on which one is newer.
In case the script locates two files named the same in source and replica directories, the file in replica will be substituted with the file from source.
