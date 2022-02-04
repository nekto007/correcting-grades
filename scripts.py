import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import (
    Schoolkid,
    Chastisement,
    Mark,
)


def get_schoolkid(kid_name: str):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
        return schoolkid

    except Schoolkid.DoesNotExist:
        print(f"Schoolkid {kid_name} doesn't exist.")

    except Schoolkid.MultipleObjectsReturned:
        print("Several students were found, please specify the request.")


def fix_marks(schoolkid: Schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid,
        points__lt=4).update(points=5)


def remove_chastisements(schoolkid: Schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()
