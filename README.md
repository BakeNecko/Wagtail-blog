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
3. Пагинация, теги для статей и поиск по тегам - Есть
4. Поиск статей в search в nav - Есть
4. Postgres - подключен и развернут
5. Docker - Есть

**Как развернуть? (Без Докера)**
```bash
python3 -m venv venv
sourse venv/bin/active
pip3 install -r requirements.txt
cd src
python3 mange.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
```
**С Докером**
```bash
make prod  # Фоновый режим
make run # Консольный режим
```