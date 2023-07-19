FROM python:3.11-slim

RUN pip install requests

COPY playtime_tracker.py .

CMD python playtime_tracker.py
