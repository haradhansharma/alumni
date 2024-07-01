FROM alpine:latest

RUN apk --no-cache add postgresql-client bash curl

COPY backup.sh /backup.sh

RUN chmod +x /backup.sh

RUN echo "0 2 * * * /backup.sh" > /etc/crontabs/root

CMD ["crond", "-f"]


