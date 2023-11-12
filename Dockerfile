FROM python:3.12.0

# Set a directory for the application to use
WORKDIR /home/evan/Documents/code/encrypt

# Copies all files to container
COPY . .

# Installs the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specifies command to run the application
CMD ["python", "./encrypt.py"]
