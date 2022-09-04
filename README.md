# Replica — Veeam Task
A solution for a Veeam test task 2 for Developer in QA.

A command line Python script that syncronizes two directories.


Features:
- One-way sync (source acts as a complete reference)
- Periodic sync (period set in CLI)

Usage:
```
replica [-h] SOURCE_DIR DESTINATION_DIR SYNC_PERIOD

Creates a replica of a specified directory

positional arguments:
  SOURCE_DIR       path to source directory to be replicated
  DESTINATION_DIR  path to directory to put replica into; will be created if nonexistent
  SYNC_PERIOD      syncronization period in seconds

optional arguments:
  -h, --help       show help message and exit
```

Script takes both relative and absolute paths as arguments.

The maximum sync period depends on each individual machine, but is rather large.


Please note that, according to the task, the files are not updated based on which one is newer.
In case the script locates two files named the same in source and replica directories, the file in replica will be substituted with the file from source.
