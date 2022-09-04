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
