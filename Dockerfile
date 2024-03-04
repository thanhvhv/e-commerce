FROM python
USER root
COPY . /home/e-mer
RUN apt update
RUN cd home/e-mer/ && pip install -r requirements.txt