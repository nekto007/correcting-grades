import os
import random

import django

from datacenter.models import (
    Chastisement,
    Commendation,
    Lesson,
    Mark,
    Schoolkid,
    Subject,
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


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


def create_commendation(schoolkid: Schoolkid, lesson_title: str):
    commendations = [
        'Прекрасно!',
        'Молодец!',
        'Талантливо!',
        'Хорошо!',
        'Великолепно!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Отлично!',
        'Красава',
        'Здорово!'
    ]
    try:
        subject = Subject.objects.get(title=lesson_title, year_of_study=schoolkid.year_of_study)
        lesson = Lesson.objects.filter(
            group_letter=schoolkid.group_letter,
            year_of_study=schoolkid.year_of_study,
            subject=subject).order_by('date').first()
        Commendation.objects.create(
            schoolkid=schoolkid,
            subject=lesson.subject,
            text=random.choice(commendations),
            created=lesson.date,
            teacher=lesson.teacher)
    except Subject.DoesNotExist:
        print(f"Subject {lesson_title} does not exist.")
