FROM django:onbuild
USER root
COPY . /home/e-mer
RUN pip freeze > requirements.txt
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install -r requirements.txt