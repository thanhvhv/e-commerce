FROM django:onbuild
USER root
COPY . /home/e-mer
RUN pip install --upgrade pip
RUN apt update -y && apt-get install -y libpq-dev
