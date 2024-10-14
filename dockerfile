FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt . 
RUN pipinstall--no-cache-dir-rrequirements.txt
COPY . .
EXPOSE 5000
CMD ["python","main.py"]