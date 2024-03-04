FROM django:onbuild
USER root
COPY . /home/e-mer
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt