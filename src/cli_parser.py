import sys
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(prog="replica", description="Creates a replica of a specified directory")
    parser.add_argument(
        "source_dir",
        metavar="SOURCE_DIR",
        help="path to source directory to be replicated"
    )
    parser.add_argument(
        "dst_dir",
        metavar="DESTINATION_DIR",
        help="path to directory to put replica into; will be created if nonexistent"
    )
    parser.add_argument(
        "period",
        metavar="SYNC_PERIOD",
        help="syncronization period in seconds"
    )
    return parser.parse_args()

def cli():
    # Extracting arguments from CL
    args = parse_arguments()
    
    abs_path = os.path.abspath(args.source_dir)
    if not os.path.exists(abs_path):
        print("Specified source directory " + abs_path + " doesn't exist.\nPlease try again with a valid source.")
        sys.exit()
    src = args.source_dir
    
    abs_path = os.path.abspath(args.dst_dir)
    if not os.path.exists(abs_path):
        print("Specified destination directory " + abs_path + " doesn't exist and will be created.")
    dst = args.dst_dir

    try:
        period = int(args.period)    # CL args extract as strings, but period must be integer
    except ValueError:
        print("Invalid sync period valie.\nPlease use a numerical value in seconds.")
        sys.exit()

    return src, dst, period