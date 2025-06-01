FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel

RUN pip uninstall -y scikit-learn

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import sklearn; print('scikit-learn version:', sklearn.__version__)"

RUN python retrain.py

EXPOSE 5000

CMD ["python", "app/main.py"]

