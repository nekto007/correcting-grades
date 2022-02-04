import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import (
    Schoolkid,
)


def get_shoolkid(kid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
        return schoolkid

    except Schoolkid.DoesNotExist:
        print(f"Schoolkid {kid_name} doesn't exist.")

    except Schoolkid.MultipleObjectsReturned:
        print("Several students were found, please specify the request.")



