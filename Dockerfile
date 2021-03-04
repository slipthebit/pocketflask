FROM apline:3.7

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh"]

