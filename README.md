# Script for the electronic school diary

This script allows you to correct bad grades (2 and 3) in subjects, delete remarks and add thanks from teachers in an
electronic diary.

The diary project is located at this [address](https://github.com/devmanorg/e-diary ).

For the script to work, you need to deploy [the project of this site] in advance (https://github.com/devmanorg/e-diary),

a database of diary ratings is also needed.

## Preparation

1. Download `scripts.py`

```bash
curl https://github.com/gennadis/e-diary/blob/master/scripts.py  --output scripts.py
```

2. Download the code, put it in the project folder next to `manage.py`

3. Open Django shell

```bash
python manage.py shell
```

4. Import `scripts.py` in Django shell

```python
import scripts
```                        

## Examples

1. `get_schoolkid(kid_name)` :
   Takes the name of the child to be found and returns the object of the Schoolkid model from the database. If no
   students with the same name are found or several students are found, an exception is called, run

```python
schoolkid = get_schoolkid('Your Name')
```

2. `fix_marks(schoolkid)` :
   Accepts the Schoolkid model object as input and corrects all the bad grades are 5, run

```python
fix_marks(schoolkid)
```

3. `remove_chastisements(schoolkid)` :
   Takes the object of the Schoolkid model and deletes all the student's comments from the database, run

```python
remove_chastisements(schoolkid)
```

4. `get_lessons(title, year, letter)` :
   Accepts the name of the subject, the year and the letter of the student's class, returns a set of found objects of
   the Lesson model.

`create_commendation(kid_name, lesson_title)` :
Accepts the student's name, the name of the lesson subject and creates an object of the Recommendation model with the
text of praise on a random day of lessons held, run

```python
create_commendation(schoolkid, 'Subject Title')
```

## Project objectives

The code is written for educational purposes — this is a lesson in a course on Python and web development on
the [Devman] website (https://dvmn.org ).