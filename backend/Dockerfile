FROM python:3.12-slim

RUN addgroup --system app && adduser --system --no-create-home --ingroup app app

WORKDIR /app
COPY app.py .
RUN chown -R app:app /app && chmod 644 app.py
USER app
EXPOSE 8080

CMD ["python", "-u", "app.py"]
