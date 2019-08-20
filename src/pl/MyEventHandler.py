import sys
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.src_path != sys.argv[2]:
            try:
                output_file = open(sys.argv[2], "a+")
                file = open(event.src_path, "r")
                for row in file.readlines():
                    new_row = row.replace('\n', event.src_path[len(sys.argv[1]):-4] + '\n')
                    output_file.write(new_row)
            finally:
                file.close()
                output_file.close()
