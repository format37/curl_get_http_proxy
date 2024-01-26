FROM python:3.11-slim-buster
WORKDIR /server
COPY requirements.txt /server
RUN pip3 install -r requirements.txt --no-cache-dir
COPY server.py /server
COPY config.ini /server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000"]