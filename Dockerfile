# Dockerfile

FROM python:3.6
RUN mkdir /immersivetech3
WORKDIR /immersivetech3
ADD requirements.txt /immersivetech3/
ADD . /immersivetech3/immersivetech

RUN pip install -r requirements.txt
RUN python3 immersivetech/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--chdir",  "immersivetech", "--bind", ":8000", "immersivetech.wsgi:application", "--log-file","-"]
# CMD ["gunicorn", "--chdir",  "immersivetech", "--bind", ":8000", "immersivetech.wsgi:application", "--capture-output", "--error-logfile","-", "--enable-stdio-inheritance", "--log-level", "debug"]