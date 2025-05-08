# Dockerfile
FROM python:3.9-slim
RUN pip install flask
RUN pip install numpy
COPY app.py /app.py
CMD ["python", "/app.py"]