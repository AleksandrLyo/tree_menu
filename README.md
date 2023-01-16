# tree_menu
Древовидное менюю           

### Описание:
Django приложение реализовывающее древовидное меню через templatetag. Добавление новых меню и его элементов в бд просходит через админку Django. Нарисовать на любой нужной странице меню по его slug c помощью тега {% draw_menu 'main_menu' %}, где 'main_menu' - slug нужного меню.

### Запуск:
```bash
git clone https://github.com/AleksandrLyo/tree_menu.git
cd tree_menu/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd tree_menu/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Создание меню:
```bash
http://127.0.0.1:8000/admin/menu/menu/add/ - Добавление нового меню
http://127.0.0.1:8000/admin/menu/item/add/ - Создание пунктов меню
http://127.0.0.1:8000/menu/ - Просмотр готового меню
```
