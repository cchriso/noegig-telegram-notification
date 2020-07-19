FROM python:3.6-slim-buster
COPY requirements.txt /tmp
ENV TZ=Europe/Vienna
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm requirements.txt -rf && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/local/share
COPY script.py /usr/local/share
CMD ["python3", "script.py"]