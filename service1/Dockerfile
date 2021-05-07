FROM python:3.9-alpine

WORKDIR /project

ADD . /project

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python","app.py"]