FROM apache/airflow:2.8.1-python3.10


USER root 

# Instala postgresql-client-17
RUN apt-get update \
 && apt-get install -y wget gnupg lsb-release \
 && echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
 && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
 && apt-get update \
 && apt-get install -y postgresql-client-17

 USER airflow