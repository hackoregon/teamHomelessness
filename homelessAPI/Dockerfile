FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
VOLUME /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install --upgrade --user awscli
ADD . /code/
ENTRYPOINT [ "/code/bin/docker-entrypoint.sh" ]
