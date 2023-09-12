FROM python:3.11
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt