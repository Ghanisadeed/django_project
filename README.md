```bash
git clone https://github.com/yourusername/django-blog-api.git
cd django-blog-api
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
