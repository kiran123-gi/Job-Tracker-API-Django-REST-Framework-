# 📌 Day 25 – Job Tracker API (Django REST Framework)

🚀 Upgraded my Job Application Tracker by building REST APIs using Django REST Framework (DRF).

## 🔧 Features
- ✅ REST API for Job Applications
- ✅ Perform CRUD Operations:
  - GET (Fetch Jobs)
  - POST (Add Job)
  - PUT (Update Job)
  - DELETE (Remove Job)
- ✅ Filter Jobs by Status
- ✅ API Endpoint for Job Statistics
- ✅ Browsable API Interface

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## 📊 API Endpoints

- `/api/jobs/` → Get all jobs / Add new job  
- `/api/jobs/{id}/` → Update/Delete specific job  
- `/api/jobs/?status=Applied` → Filter by status  
- `/api/stats/` → Job statistics  

## 🧠 Key Learnings
- Working with Django REST Framework  
- Creating ModelViewSet & Serializers  
- Routing using DefaultRouter  
- Filtering with Query Parameters  
- Building scalable backend APIs  

## 🔗 How to Run
```bash
git clone 
cd job-tracker
python manage.py runserver
