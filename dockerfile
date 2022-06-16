FROM python:3.10-alpine

WORKDIR /code

COPY /src/requirements.txt /requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r /requirements.txt

COPY /src/. /code

CMD ["python3", "app.py"]



