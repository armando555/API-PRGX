# temp stage
FROM python:3.8-slim as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /usr/src/app/requirements.txt 
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r /usr/src/app/requirements.txt


# final stage
FROM python:3.8-slim

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -yq --no-install-recommends git && \
    chown www-data:www-data -R /usr/src/app && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY . /usr/src/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]