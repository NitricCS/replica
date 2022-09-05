import os
import stat
from shutil import copy2, rmtree

##### Directory class
class Directory():
    def __init__(self, p):
        self.path = os.path.abspath(p)

    # Parse a directory
    def get_contents(self):
        files = []
        dirs = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dirname in dirnames:                            # parse subdirs
                d = os.path.join(dirpath, dirname)
                relative_path = os.path.relpath(d, self.path)
                if relative_path not in dirs:
                    dirs.append(relative_path)                  # append avoiding duplicates
            for filename in filenames:                          # parse files
                if dirpath in dirs:
                    dirs.remove(dirpath)
                filepath = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(filepath, self.path)
                files.append(relative_path)
        return files, dirs                          # returns a tuple ([files], [dirs])
    
    ### File actions inside directory
    # Create new subdir in current directory
    def makedir(self, rel_path):
        absolute_path = os.path.join(self.path, rel_path)
        os.makedirs(absolute_path, exist_ok=True)
    
    # Remove a subdir from current directory
    def removedir(self, rel_path):
        absolute_path = os.path.join(self.path, rel_path)
        if os.path.exists(absolute_path):
            rmtree(absolute_path, onerror=remove_readonly)
    
    # Copy a file from defined source to current directory
    def cpfile(self, src, filename):
        absolute_src = os.path.join(src, filename)
        absolute_dst = os.path.join(self.path, filename)
        copy2(absolute_src, absolute_dst)         # copy2 preserves metadata

    # Remove a file from current dir by relative path
    def rmfile(self, rel_path):
        absolute_path = os.path.join(self.path, rel_path)
        if os.path.exists(absolute_path):
            os.remove(absolute_path)
    
    # Get modified time of a file
    def get_modified_time(self, rel_path):
        absolute_path = os.path.join(self.path, rel_path)
        modified_time = os.path.getmtime(absolute_path)
        return modified_time


##### Separate functions
# Get files from dir1 that are not in dir2
def get_diff(dir1, dir2):
    difference = list(set(dir1) - set(dir2))
    return difference

# Get files that exist in both directories
def get_equal(dir1, dir2):
    eq_files = list(set(dir1).intersection(dir2))
    return eq_files

# Attempt to remove read-only bit on Windows
def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)