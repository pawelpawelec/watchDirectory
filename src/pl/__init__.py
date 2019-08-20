import time

from MyObserver import observer

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
observer.join()
