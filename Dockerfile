FROM alpine:latest
WORKDIR /app
RUN apk update \
    && apk add git zsh python3 py3-pip curl vim
RUN pip3 install flask && pip3 install pytest
COPY . /app
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh"]