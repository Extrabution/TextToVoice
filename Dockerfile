FROM python

RUN mkdir -p ./code
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./src /code/src

RUN mkdir -p ./static
RUN mkdir -p ./static/audio
RUN mkdir -p ./static/text
#

EXPOSE 8001:8001

WORKDIR /code/src
CMD ["python3", "main.py"]