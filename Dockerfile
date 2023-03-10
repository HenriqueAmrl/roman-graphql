FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "wsgi:app", "-b", "0.0.0.0:8080" ]
EXPOSE 8080