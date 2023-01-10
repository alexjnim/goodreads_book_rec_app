FROM python:3.9.5

WORKDIR /app

# install requirements first
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 8000

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "app:app"]

