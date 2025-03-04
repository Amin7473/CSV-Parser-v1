# Upload_CSV

This is a Django project named **Upload_CSV**, which supports functionalities like uploading CSV files, utilizing Redis for websockets/celery, and using Celery for background tasks.

---

## Prerequisites
- Python (>= 3.8)
- Django (>= 4.0)
- PostgreSQL
- Redis
- Celery

---

## 1. Project Setup
### Clone the Repository
```bash
git clone https://github.com/Amin7473/CSV-Parser-v1.git
git checkout DEV/Main
cd upload_csv
```

### Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Install Project Dependencies
```bash
pip install -r requirements.txt
```

## 2. Database Setup
### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```


---

## 3. Run the Django Development Server
```bash
python manage.py runserver
```

Access the app at: `http://localhost:8000`

---

## 4. Redis Installation and Setup
### Install Redis on Ubuntu
```bash
sudo apt update
sudo apt install redis-server
```

### Start and Enable Redis
```bash
sudo systemctl start redis
sudo systemctl enable redis
```

### Verify Redis is Running
```bash
redis-cli ping
# PONG
```

---

## 5. Celery Installation and Setup
### Install Celery
```bash
pip install celery
```

### Run Celery Worker
```bash
celery -A upload_csv worker -l info
```


---

## 6. Additional Management Commands
- Check for Pending Migrations:
```bash
python manage.py showmigrations
```

- Clear Redis Cache (Optional):
```bash
redis-cli flushall
```


