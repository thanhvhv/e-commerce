FROM python
USER root
COPY . /home/e-mer
RUN apt update
RUN pip install -r requirements.txt