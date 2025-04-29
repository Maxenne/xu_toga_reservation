FROM python:3.10

WORKDIR /app

COPY . /app/

# Optional if needed:
# RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# # Expose the port the app runs on
# EXPOSE 8000