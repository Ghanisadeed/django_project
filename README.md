```bash
git clone https://github.com/Ghanisadeed/django_project.git
cd django_project
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
