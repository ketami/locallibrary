# locallibrary

Проект - тестовое задание с построением древовидного меню. 

Главная страница выглядит так:

![image](https://user-images.githubusercontent.com/33355208/217703356-488a41c9-f325-4f88-b171-b107a3858303.png)

За основу взят учебный проект по Django от Mozilla - библиотека. На скриншоте два меню "main menu" и "About", реализованы через template tag.

![image](https://user-images.githubusercontent.com/33355208/217703520-9710ede4-d198-468d-a328-358f6dd9d708.png)

Применены стили bootstrap (dropdown menu). Меню определяются по названию и настраиваются через админку. Там можно создать меню и дерево меню. Админка: admin/admin. 

![image](https://user-images.githubusercontent.com/33355208/217703781-12a47ea8-fd4a-4399-af24-724b4f466084.png)

Конечные и промежуточные точки меню (кроме корневой) содержат ссылки. Порядок определяется полем order. 

Для отрисовки одного меню выполняется один SQL-запрос:


![image](https://user-images.githubusercontent.com/33355208/217704015-6b66cea4-fc0f-4859-a7e1-01cb4f5af5c2.png)


Не используются сторонние библиотеки, кроме django-debug для отладки.

![image](https://user-images.githubusercontent.com/33355208/217704237-294dc411-9553-412a-a13c-348071e88490.png)


Меню добавляется с помощью тегов:
{% draw_menu "main menu" %}
{% draw_menu "About" %}

![image](https://user-images.githubusercontent.com/33355208/217704568-6a0edf90-31d2-4652-854b-5a389bb1630b.png)

Есть определенные проблемы с внешним видом - не сильно заморочено.
