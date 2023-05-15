FROM python:latest
WORKDIR /code
ENV PYTHONPATH=/code
ENV PATH=/code:$PATH
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code