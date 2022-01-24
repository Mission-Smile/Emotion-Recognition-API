# init a base image
FROM python:3.9-slim

# Upgrade pip
RUN pip install --upgrade pip
# define the present working directory
WORKDIR /app
# copy the contents into the working dir
COPY . /app
# run pip to install the dependencies of the flask app
RUN apt-get -y update
RUN pip install -r requirements.txt

#RUN pip3 --no-cache-dir install -r requirements.txt
# expose port
# EXPOSE 8000

# define the command to start the container
# CMD ["python", "app.py"]

CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload