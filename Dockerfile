FROM python:3.10-bullseyepip install --upgrade pip

WORKDIR /source

COPY requirements.txt .

RUN pip install -r requirements.txt .

COPY . .


# CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app", "--reload"]

