# Keylogger Cybersecurity Project
This repository contains a Python script for a keylogger, a tool designed to record keystrokes made on a keyboard. The keylogger script logs keystrokes to a text file, providing insights into user activity on a computer system.

## Features:
### Keystroke Logging: 
Captures keystrokes in real-time.
### Timestamps: 
Each keystroke is timestamped for accurate tracking.
### Session Management: 
Logs the start and end of each logging session.
### Encryption and Decryption (Fernet):
Logs are encrypted using the Fernet symmetric encryption scheme after the session has ended, providing confidentiality and data integrity.
### Customizable: 
Easily configurable to specify logging directory and format.

## Usage:
### Clone the Repository: 
Clone this repository to your local machine.
### Run the Script: 
Execute the keylogger.py script in a Python environment.
### Press Keys: 
Press keys on the keyboard to record keystrokes.
### Stop Logging: 
Press the esc key to stop the keylogger.
### Check Logs: 
View the generated log files in the KeyLogs directory for recorded keystrokes.

## Ethical Considerations:
### Permission: 
Obtain explicit permission from users before monitoring their keystrokes.
### Legitimate Use: 
Ensure the keylogger is used for ethical and legal purposes, such as monitoring employee activity with their knowledge.
### Privacy: 
Respect user privacy and handle logged data securely.

## Dependencies:
### -> Python 3.12.3
### -> pynput library
### -> cryptography library (for Fernet encryption)

## Disclaimer:
This keylogger script is intended for educational and cybersecurity research purposes only. Misuse of this tool for unauthorized monitoring or malicious activities is strictly prohibited.
