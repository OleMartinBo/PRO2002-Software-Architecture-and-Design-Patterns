# Defines the runtime environment (Python)
FROM python:3.15.2

# Applies the working dir inside the container
WORKDIR /app

# Copies dependency definitions (requirements.txt)
COPY requirements.txt .

# Installs required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copies application code into the image
COPY . ./PRO2002WorkRequirement4/

# Defines how the application starts
CMD ["python", "-m", "flask", "--app", "PRO2002WorkRequirement4.app", "run", "--host=0.0.0.0"]