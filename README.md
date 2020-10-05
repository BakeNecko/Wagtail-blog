## **Мини (пока что) блог на Wagtail-CMS**
### Стек технологий:
1. Wagtail + Django
2. Postgres
3. Docker
4. CSS/JS

[Документация по Wagtail]: https://docs.wagtail.io/en/stable/getting_started/index.html

[Лучший Сайт для изучения Wagtail]: https://learnwagtail.com/

**Коротко о состоянии проекта:**
1. Добавление Статей - Есть
2. Редактирование Страниц - Есть
3. Postgres - не подключен и не развернут
4. Docker - Почти нет

**Как развернуть? (Без Докера)**
```bash
python3 -m venv venv
sourse venv/bin/active
pip3 install -r requirements.txt
cd src
python3 mange.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
```
