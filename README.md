# Advance-Keylogger
This Python-based keylogger monitors keyboard activity, captures screenshots, records webcam photos, and audio. It logs keystrokes, tracks app usage, and operates stealthily. Logs can be sent via email or FTP, and data is encrypted for security. Remote access is available.

# Advanced Keylogger with Screenshot, Webcam, and Audio Recording

This Python-based keylogger is equipped with advanced features to provide comprehensive monitoring of computer activities. In addition to logging keystrokes, it captures screenshots, takes webcam photos, and records audio, providing a detailed report of user interactions.

## Features

- **Keyboard Activity Monitoring:** Tracks all keystrokes, including special keys and combinations.
- **Screenshot Capturing:** Periodically captures screenshots of the user's screen.
- **Webcam Photo Capture:** Utilizes the webcam to capture images of the user.
- **Audio Recording:** Records audio using the computer's microphone.
- **Application Usage Logging:** Tracks the usage of different applications.
- **Stealth Mode:** Operates silently in the background, without user detection.
- **Email Reporting:** Sends logs via email for remote access and monitoring.
- **Secure Authentication:** Requires email credentials for secure transmission of logs.

## Usage

1. **Set Up Email Parameters:**
   - Open `keylogger.py` and replace `sender_email`, `sender_password`, and `recipient_email` with your email credentials.
   
2. **Run the Keylogger:**
   ```
   python keylogger.py
   ```

3. **Enter Email Credentials:**
   - Upon running the keylogger, you'll be prompted to enter your email address and application key (password).

4. **Accessing Logs:**
   - Logs will be sent to the provided email address.

## Note
- **Email Address:** Provide the email address where you want to receive the logs.
- **Application Key (Password):** Use this key as the password for authentication.

## Disclaimer
This keylogger is designed for educational purposes only. It is intended to demonstrate the capabilities of monitoring software and should be used responsibly and legally. We do not condone any illegal activities or misuse of this tool. Use it at your own risk.
