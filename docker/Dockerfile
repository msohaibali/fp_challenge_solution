# Get the Fast API image with Python version 3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Create the directory for the container
WORKDIR /fp_challenge_solution
COPY requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY ./Models/OperationsDictionary.py ./Models/OperationsDictionary.py
COPY ./Models/ResponseModel.py ./Models/ResponseModel.py
COPY ./BLC/FeaturesGenerator.py ./BLC/FeaturesGenerator.py
COPY ./utils/ProcessingUtils.py ./utils/ProcessingUtils.py
COPY ./config.json ./config.json
COPY ./output ./output
COPY ./app.py ./

# Run by specifying the host and port
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]