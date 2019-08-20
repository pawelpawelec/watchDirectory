import sys

from watchdog.observers import Observer
from MyEventHandler import MyEventHandler

observer = Observer()
event_handler = MyEventHandler()
observer.schedule(event_handler, sys.argv[1], True)
observer.start()