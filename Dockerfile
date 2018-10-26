# Dockerfile

# FROM directive instructing base image to build upon
#FROM python:3-onbuild

# Install any needed packages specified in requirements.txt
#RUN pip3 install -r requirements.txt

# COPY startup script into known file location in container
#COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
#EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
#CMD ["/start.sh"]
# done!

FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
