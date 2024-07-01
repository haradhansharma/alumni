FROM python:3.10-slim

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy
COPY . /app/
RUN chmod +x start-reload.sh
EXPOSE 8000

CMD ["/app/start-reload.sh"]

# CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "abackend.asgi:application"]
