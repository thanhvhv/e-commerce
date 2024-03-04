FROM python
USER root
COPY . /home/e-mer
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
RUN cd home/e-mer/ && pip install -r requirements.txt

EXPOSE 8000
