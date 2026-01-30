import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecs_quotes_app.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "adminadmin"  # CHANGE le mot de passe

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser créé !")
else:
    print("Superuser existe déjà.")