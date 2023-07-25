FROM python:3.9-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk add --update --no-cache py3-numpy py3-pandas

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

RUN crontab ./app/crontab

CMD ["crond", "-f"]