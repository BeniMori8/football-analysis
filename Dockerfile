FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install pandas pydantic
COPY . .
USER 1001
CMD ["python", "processor.py"]