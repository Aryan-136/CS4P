from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)

# List of WhatsApp numbers
customer_care_numbers = [
    "6353797269",  # Replace with your actual WhatsApp numbers
    "6353797269",
    "6353797269",
    "9898094002",
    "9173141889"
]

# Counter to keep track of the current number
counter_file = "counter.txt"

# Log file
log_file = "whatsapp_logs.txt"

# WhatsApp base URL
whatsapp_url = "https://wa.me/"

# Function to get the current counter value
def get_current_counter():
    try:
        with open(counter_file, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0  # Default counter if file doesn't exist

# Function to update the counter
def update_counter(counter):
    with open(counter_file, "w") as file:
        file.write(str(counter))

# Function to log redirection details
def log_redirect(number, sequence):
    with open(log_file, "a") as log:
        log_entry = f"{datetime.now()} | Redirect #{sequence} | WhatsApp Number: {number}\n"
        log.write(log_entry)

@app.route("/")
def redirect_to_whatsapp():
    counter = get_current_counter()
    number_to_redirect = customer_care_numbers[counter % len(customer_care_numbers)]
    sequence_number = counter + 1

    # Generate WhatsApp link
    whatsapp_link = f"{whatsapp_url}{number_to_redirect}"

    # Log the redirection
    log_redirect(number_to_redirect, sequence_number)

    # Update the counter for the next redirection
    update_counter(sequence_number)

    # Redirect the user to WhatsApp
    return redirect(whatsapp_link)

if __name__ == "__main__":
    app.run(debug=True)
