FROM python:3.11

WORKDIR /calendar

COPY . /calendar

CMD ["python", "main.py"]