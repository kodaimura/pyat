FROM python:3.10.6

WORKDIR /var/www/pyat

COPY ./app .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV EXEC_ENV=local

CMD ["python3", "run.py"]