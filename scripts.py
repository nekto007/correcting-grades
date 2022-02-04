import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import (
    Schoolkid,
    Chastisement,
    Mark,
    Lesson,
    Subject,
    Commendation,
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


def get_lessons(title: str, year: str, letter: str):
    try:
        lesson = Lesson.objects.filter(
            group_letter=letter,
            year_of_study=year,
            subject=title).order_by('date')
        return lesson
    except Lesson.ObjectDoesNotExist:
        print(f'Subject {title} does mot exist.')


def create_commendation(schoolkid: Schoolkid, lesson_title: str):
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
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
        subject = Subject.objects.get(title=lesson_title, year_of_study=year_of_study)
        lesson = random.choice(get_lessons(subject, year_of_study, group_letter))
        Commendation.objects.create(
            schoolkid=schoolkid,
            subject=lesson.subject,
            text=random.choice(commendations),
            created=lesson.date,
            teacher=lesson.teacher)
    except Subject.DoesNotExist:
        print(f"Subject {lesson_title} does not exist.")
