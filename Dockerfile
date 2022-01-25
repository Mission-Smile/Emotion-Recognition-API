# init a base image
FROM python:3.9

# Upgrade pip
RUN pip install --upgrade pip
RUN apt-get upgrade
RUN apt-get update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

# define the present working directory
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# copy the contents into the working dir
COPY . /app
# run pip to install the dependencies of the flask app
RUN apt-get -y update

# define the command to start the container
# CMD ["python", "app.py"]

CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload