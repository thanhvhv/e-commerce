FROM python
USER root
COPY . /home/e-mer
RUN apt update
