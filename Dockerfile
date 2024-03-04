FROM django:onbuild
USER root
COPY . /home/e-mer
RUN pip install -r requirements.txt