FROM python:3.11

WORKDIR /calendar

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /calendar

CMD ["python", "main.py"]
