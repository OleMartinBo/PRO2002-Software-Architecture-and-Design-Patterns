# Work Requirement 4 Building, Testing, and Containerizing a Flask API
In this final work requirement, you will implement a small but complete backend service. 
The goal is to demonstrate that you can build a minimal Flask-based REST API, test it, 
and package it using container technology, while clearly explaining how everything fits together.

Submission deadline: 20.11.2026, 12:00

### Objectives
* Build a minimal REST API using Flask
* Write a simple automated test for an API endpoint
* Containerize a Python application using Docker
* Explain structure, tooling, and execution clearly

### What to Do
Create a small Flask-based REST API project with the following components:
1. Implement a Flask application with one simple demo endpoint. The endpoint should return a JSON response. Keep the logic minimal and easy to understand
2. Write one automated test for the endpoint. The test should verify:Correct HTTP status code and Expected response body. Use a standard Python testing tool (e.g. pytest)
3. Containerize the application using Docker. The container must be able to: Build successfully and Run the Flask API

## Documentation
This sections explains the setup and how to use the application.

### What the application does

### How to run the test

### How to run the API locally (without Docker)

### How to build and run the container

### A brief explanation of the project structure
Three layer architecture (Note! Changed as this was not necessary for one simple endpoint)

`````
PRO2002WorkRequirement4/
|_health_api/
| |__routes/
|    |__init__.py
|    |_health_route.py
|_testing/
| |__init__.py
| |__test.py
|__init__.py
|_app.py
|_README_WR4.md
|_requirements.txt
`````

#### Sources (Remove later, keep during development)
https://flask.palletsprojects.com/en/stable/changes/
https://devguide.python.org/versions/ 
https://flask.palletsprojects.com/en/stable/testing/#sending-requests-with-the-test-client
