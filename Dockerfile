FROM python:3.11.6

ENV PYTHONUNBUFFRED=1

WORKDIR /CODE

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
