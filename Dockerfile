FROM python:3.13-slim

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools wheel
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY myapp.py config.py boot.sh ./
RUN chmod a+x boot.sh


ENV FLASK_APP=myapp.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]