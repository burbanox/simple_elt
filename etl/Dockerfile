FROM python:3.8-slim

WORKDIR /code

# Añadir repositorio oficial de PostgreSQL 17 y cliente
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bookworm-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y postgresql-client-17 && \
    apt-get clean
    
COPY script.sh /code/script.sh
COPY . .

CMD ["python3", "etl/etl.py"]
