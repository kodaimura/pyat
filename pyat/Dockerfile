FROM python:3.10.6

COPY ./app /src

WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "run.py"]