FROM python:3.9-slim-buster
LABEL maintainer="Tandras_"

RUN mkdir /usr/src/app/

COPY . /usr/src/app/

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
