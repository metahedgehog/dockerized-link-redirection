import os
import threading
import time
from flask import Flask, redirect
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Read the previous count value from the count.txt file if it exists
count_file_path = '/app/data/count.txt'
if os.path.exists(count_file_path):
    with open(count_file_path, "r") as count_file:
        try:
            count = int(count_file.read())
        except ValueError:
            count = 0
else:
    count = 0

# Initialize last_count
last_count = count

# Lock to ensure safe access to the count variable
count_lock = threading.Lock()

# Get the target link from the environment variable
target_link = os.getenv("TARGET_LINK")

# Function to save the count to the count.txt file on the host machine
def save_count():
    global count, last_count
    while True:
        # Check if the count has changed
        if count != last_count:
            # Save the count to the count.txt file on the host machine
            with open(count_file_path, "w") as count_file:
                count_file.write(str(count))
            last_count = count  # Update last_count
        # Sleep for a short period to reduce CPU usage
        time.sleep(1)  # Adjust the sleep duration as needed

@app.route('/')
def redirect_to_external_link():
    global count
    with count_lock:
        count += 1
    # Redirect to the target link from the environment variable
    return redirect(target_link, code=302)

@app.route('/counter', methods=['GET'])
def get_count():
    with count_lock:
        current_count = count
    return f'Visits: {current_count}\n'

if __name__ == '__main__':
    # Create and start the background thread for saving the count
    save_thread = threading.Thread(target=save_count)
    save_thread.daemon = True
    save_thread.start()

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
