FROM python:3.9.12

RUN pip install update pip
RUN pip install --upgrade pip

COPY ./ ./
RUN pip install -r requirements.txt