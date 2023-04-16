FROM python:3.11.3-slim

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
  && chown python:python -R /app

USER python

COPY --chown=python:python requirements.txt .
RUN pip3 install --no-warn-script-location --no-cache-dir --user -r requirements.txt


ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    USER="python"

COPY --chown=python:python ./project .

EXPOSE 8000

CMD ["python3", "./manage.py",  "runserver", "0.0.0.0:8000"]