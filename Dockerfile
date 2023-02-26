FROM openjdk:slim
COPY --from=python:3.10-slim / /
# FROM python:3.10-slim

ENV PYTHONUNBUFFER True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x rsjk.sh
RUN chmod +x runCode.sh

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 server:app
