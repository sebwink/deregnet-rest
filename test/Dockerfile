FROM python:3

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y httpie && \
    python3 -m pip install xonsh 

RUN git clone https://github.com/vishnubob/wait-for-it
RUN mkdir test 

WORKDIR /test

COPY . .

CMD ["/wait-for-it/wait-for-it.sh", "--timeout=0", "kong:8000" ,"--", "bash", "test.sh"]
