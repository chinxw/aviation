# Dockerfile

FROM python:3.6
RUN mkdir /immersivetech3
WORKDIR /immersivetech3
ADD requirements.txt /immersivetech3/
ADD . /immersivetech3/immersivetech

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir", "immersivetech", "--bind", ":8000", "immersivetech.wsgi:application"]



















# ADD docker-entrypoint.sh /immersivetech3/

# RUN pip3 install virtualenv
# RUN virtualenv env
# RUN . env/bin/activate
# RUN env/bin/pip install -r requirements.txt
# RUN env/bin/python3 immersivetech/manage.py collectstatic --noinput



# RUN ls env/bin
# RUN ls immersivetech/static
# EXPOSE port 8000 to allow communication to/from server
# EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
#CMD ["/start.sh"]
# done!

# RUN pip3 install django

# RUN which pip3
# RUN django-admin startproject immersivetech

# RUN cd immersivetech && ls
# RUN python3 /immersivetech3/immersivetech/manage.py makemigrations db
# RUN python3 /immersivetech3/immersivetech/manage.py migrate
