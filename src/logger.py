from datetime import datetime
from os import path, makedirs

class Logger():
    def __init__(self, log_path):
        self.path = path.abspath(log_path)
    
    # Current date and time for log records
    def get_time(self):
        now = datetime.now()
        now_time = now.strftime("%H:%M:%S")
        return now_time
    
    def get_datetime(self):
        now = datetime.now()
        now_timestamp = now.strftime("%d.%m.%y %H:%M:%S")
        return now_timestamp
    
    # Log record on startup
    def add_starting_record(self, src, dst):
        log = ""
        makedirs(path.dirname(path.abspath(self.path)), exist_ok=True)
        f = open(self.path, "a", encoding="utf-8")
        log = "Sync started " + self.get_datetime() + ". "
        log += "Source dir: " + src + ", replica: " + dst
        print(log)
        f.write(log + "\n")
        f.close()
    
    # Log record on action
    def add_record(self, type, obj):
        log_text = ""
        makedirs(path.dirname(path.abspath(self.path)), exist_ok=True)
        f = open(self.path, "a", encoding="utf-8")
        if type == "rd":        # dir removed
            log_text = "Removed directory " + obj + " from replica"
        elif type == "ad":      # dir copied
            log_text = "Created new subdirectory " + obj + " in replica"
        elif type == "rf":      # file removed
            log_text = "Deleted file " + obj + " from replica"
        elif type == "af":      # file copied
            log_text = "Copied new file " + obj + " from source to replica"
        elif type == "sf":      # file substituted
            log_text = "Substituted file " + obj + " in replica by the version from source"
        log = "[" + self.get_datetime() + "] " + log_text + "\n"
        print(log_text)
        f.write(log)
        f.close()
    
    # CLI verbose update
    def progress_update(self):
        log = "Sync cycle finished at " + self.get_time()
        print(log)