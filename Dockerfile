FROM python:3.12

WORKDIR /app
COPY . .

RUN apt-get update -y && apt-get install -y npm
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.12 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN reflex init

CMD reflex run --env prod --backend-only