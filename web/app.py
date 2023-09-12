import os
import threading
from flask import Flask, redirect
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
count = 0
count_lock = threading.Lock()  # Lock to ensure safe access to the count variable

# Get the target link from the environment variable
target_link = os.getenv("TARGET_LINK")

# Define the path to the count.txt file on the host machine
count_file_path = '/app/data/count.txt'

# Function to save the count to the count.txt file on the host machine
def save_count():
    global count
    while True:
        # Save the count to the count.txt file on the host machine
        with open(count_file_path, "w") as count_file:
            count_file.write(str(count))

@app.route('/')
def redirect_to_external_link():
    global count
    with count_lock:
        count += 1
        # Immediately save the count to the count.txt file
        with open(count_file_path, "w") as count_file:
            count_file.write(str(count))
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
