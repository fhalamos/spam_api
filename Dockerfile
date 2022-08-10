FROM python:3.7.0
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["bash", "./gunicorn.sh"]
