FROM python:3.6-slim-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
# Don't copy the app files here, we'll mount them as a volume for hot reload
# COPY . .
EXPOSE 4000
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]