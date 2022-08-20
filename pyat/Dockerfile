FROM python:3.10.6

COPY ./app /src

WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=local

CMD ["python3", "run.py"]