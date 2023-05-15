FROM python:latest
WORKDIR /
ENV PYTHONPATH=/
ENV PATH=/:$PATH
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./