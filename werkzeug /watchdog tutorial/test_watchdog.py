import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Event handler functions
def on_created(event):
    print(f"created: {event.src_path}")

def on_deleted(event):
    print(f"deleted: {event.src_path}")

def on_modified(event):
    print(f"modified: {event.src_path}")

def on_moved(event):
    print(f"moved: from {event.src_path} to {event.dest_path}")

if __name__ == "__main__":  # Fixed the comparison operator
    # Create an instance of the event handler
    event_handler = FileSystemEventHandler()

    # Assign event handler methods
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved  # Fixed function assignment
    
    # Specify the directory to watch
    path = "." # ? if path="." current directory
    # path = "/home/bee-ams/Development/Flask/werkzeug"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    print(f"Watching for changes in {path}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
