FROM python:3.11.3

RUN apt update && apt install vim apt-utils -y && \
    echo "pytest -vv --ff" >> /root/.bash_history


WORKDIR /home/BankApplication

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
