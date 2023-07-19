FROM python:3.11-alpine

RUN pip install --no-cache-dir requests

COPY playtime_tracker.py .

CMD python playtime_tracker.py
