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
# ENV PYTHONUNBUFFERED 1
RUN mkdir /immersivetech3
WORKDIR /immersivetech3
ADD requirements.txt /immersivetech3/
RUN pip3 install -r requirements.txt
RUN virtualenv env
RUN . env/bin/activate
RUN pip3 install django
RUN django-admin startproject immersivetech
ADD . /immersivetech3/immersivetech

# RUN cd immersivetech && ls
# RUN python3 /immersivetech3/immersivetech/manage.py makemigrations db
# RUN python3 /immersivetech3/immersivetech/manage.py migrate
