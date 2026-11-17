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

1. First open the Terminal(CMD) in VS Code and install the dependencies:
`````
python -m pip install -r PRO2002WorkRequirement4/requirements.txt
`````
2. In the Terminal navigate to the folder "PRO2002WorkRequirement4":
`````
cd PRO2002WorkRequirement4
`````
3. Run the automated test with the command in the Terminal: 
`````
python -m pytest testing -v
`````

### How to run the API locally (without Docker)
1. Open the Terminal(CMD) in VS Code and navigate to "PRO2002 Software Architecture and Design Patterns".
2. Start the Flask application with the command in the Terminal. 
`````
python -m flask --app PRO2002WorkRequirement4.app run
`````
3. When the Flask server is running, follow the link in the terminal or copy the URL below into the browser.
`````
http://127.0.0.1:5000/health
`````
4. The endpoint should then return: 
`````
{
  "Status": "ok"
}
`````
5. To close the application, enter ```CTRL + C```

#### Thunder client testing:
1. Open or install Thunder Client in VS Code
2. Press "New Request"
3. Select the "GET" method and paste in the the url below. 
`````
http://127.0.0.1:5000/health
`````
4. Press "send"
5. The endpoint should then return:
`````
{
  "Status": "ok"
}
`````
  In Thunder Client, it also should display "Status: 200 OK"

### How to build and run the container
1. Prerequisites: Make sure Docker desktop is installed and running.
2. Open the Terminal (CMD) in VS Code and go to the WR4 folder and enter:
`````
cd PRO2002WorkRequirement4
`````
3. To build the Docker image, enter following command in the Terminal.
   This command makes Docker read the Dockerfile and creates the image of the app:
`````
docker build -t health_api .
`````
3. To run the Docker image, enter the following command in the Terminal enter:
`````
docker run -p 5000:5000 --name health_api health_api
`````
4. The application should now be accessible in the browser via this link:
`````
http://localhost:5000/health
`````
5. This should return: 
`````
{
  "Status": "ok"
}
`````
6. To stop the container and close the application enter: ```CTRL + C``` in the Terminal.

### A brief explanation of the project structure
Based on the scope and constraints for this work requirement, the project is setup only into the necessary files and folder for the API.
The project structure do not include database, external services or authentication, to ensure the project is small and focused. However, if the application was to be expanded upon, I would use a Three layer architecture. 

##### The project structure:
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
|_Dockerfile
|_README_WR4.md
|_requirements.txt
`````