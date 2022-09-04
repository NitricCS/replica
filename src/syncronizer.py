import sys
from time import sleep
from src.cli_parser import cli
from src.file_handler import Directory, get_diff, get_equal
from src.logger import Logger

LOG_PATH = "./logs/replica.log"

class Replica():
    def __init__(self, src, dst, period):
        self.source = Directory(src)
        self.destination = Directory(dst)
        self.period = period
    
    def find_differences(self):
        # Parsing directories
        src_files = self.source.get_contents()
        dst_files = self.destination.get_contents()

        # Figuring out differences
        self.new_files = get_diff(src_files[0], dst_files[0])          # files to copy
        self.files_to_remove = get_diff(dst_files[0], src_files[0])    # files to delete
        self.equal_files = get_equal(src_files[0], dst_files[0])       # files to check by date

        self.new_dirs = get_diff(src_files[1], dst_files[1])           # dirs to create
        self.dirs_to_remove = get_diff(dst_files[1], src_files[1])     # dirs to delete

    def sync(self):
        logger = Logger(LOG_PATH)
        logger.add_starting_record(self.source.path, self.destination.path)
        while (True):
            self.find_differences()

            # Syncronizing directories
            for dirname in self.new_dirs:                    # creating non-existent subdirs
                self.destination.makedir(dirname)
                logger.add_record("ad", dirname)
            
            for dirname in self.dirs_to_remove:              # removing extra subdirs
                self.destination.removedir(dirname)
                logger.add_record("rd", dirname)
            
            for filename in self.files_to_remove:            # deleting extra files
                self.destination.rmfile(filename)
                logger.add_record("rf", filename)
            
            for filename in self.new_files:                  # copying non-existent files
                self.destination.cpfile(self.source.path, filename)
                logger.add_record("af", filename)
            
            for filename in self.equal_files:                # substituting files with similar names
                mod_time_src = self.source.get_modified_time(filename)
                mod_time_dst = self.destination.get_modified_time(filename)
                if (mod_time_src != mod_time_dst):
                    self.destination.cpfile(self.source.path, filename)
                    logger.add_record("sf", filename)
            
            logger.progress_update()
            try:
                sleep(self.period)
            except OverflowError:
                print("Sync period is too large.\nPlease try a smaller number.")
                sys.exit()

if __name__ == "__main__":
    args = cli()
    r = Replica(args[0], args[1], args[2])
    r.sync()