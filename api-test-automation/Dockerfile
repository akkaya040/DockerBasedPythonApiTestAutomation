FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Run test with python without report
#CMD ["python", "test_api.py"]

#Run test with pytest. It generates report as stout
CMD ["pytest", "-v"]