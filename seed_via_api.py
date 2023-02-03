#!/usr/bin/python3
import json
import requests

# Read the data from the file
with open('data.json', 'r') as f:
    data = json.load(f)

# Set the base URL for the API endpoint
base_url = 'http://localhost:8000/api/tasks/'

# Iterate through the list of task items
for idx, task in enumerate(data):
    # Send the POST request with the task data
    response = requests.post(base_url, json=task)
    # Print the response status code to verify if the request was successful
    print(f'RESPONSE {idx} STATUS: {response.status_code}')
