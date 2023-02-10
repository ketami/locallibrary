# locallibrary

Проект - тестовое задание с построением древовидного меню. 

Главная страница выглядит так:

![image](https://user-images.githubusercontent.com/33355208/217703356-488a41c9-f325-4f88-b171-b107a3858303.png)

За основу взят учебный проект по Django от Mozilla - библиотека. На скриншоте два меню "main menu" и "About", реализованы через template tag.

"main menu":

![image](https://user-images.githubusercontent.com/33355208/217705460-83c00064-4d03-4a25-8d6e-0ad61dd64108.png)

"About":

![image](https://user-images.githubusercontent.com/33355208/217704237-294dc411-9553-412a-a13c-348071e88490.png)

Файлы содержащие дерево: 
- catalog/templates/navigation_tree.html 
- catalog/templates/navigation_drawnodes.htmll 
- catalog/models.py Модели: NavigationTree, NavigationMenu
- catalog/templatetags/nav_menu.py


Применены стили bootstrap (dropdown menu). Меню определяются по названию и настраиваются через админку. Там можно создать меню и дерево меню. Админка: admin/admin. 

![image](https://user-images.githubusercontent.com/33355208/217703781-12a47ea8-fd4a-4399-af24-724b4f466084.png)

Конечные и промежуточные точки меню (кроме корневой) содержат ссылки. Порядок определяется полем order. 

Для отрисовки одного меню выполняется один SQL-запрос:


![image](https://user-images.githubusercontent.com/33355208/217704015-6b66cea4-fc0f-4859-a7e1-01cb4f5af5c2.png)


Не используются сторонние библиотеки, кроме django-debug для отладки.

Меню добавляется с помощью тегов:
{% draw_menu "main menu" %}
{% draw_menu "About" %}

![image](https://user-images.githubusercontent.com/33355208/217704568-6a0edf90-31d2-4652-854b-5a389bb1630b.png)

Есть определенные проблемы с внешним видом - не сильно заморочено.


В базе, NavigationMenu:
![image](https://user-images.githubusercontent.com/33355208/217705198-5b2b4842-9439-4e98-9416-0a693d030466.png)

NavigationTree:
![image](https://user-images.githubusercontent.com/33355208/217705239-1b9cba24-709d-4750-9196-fc8cb18d26d3.png)

Пункты тестового задания выполнены все кроме 5: Активный пункт меню определяется исходя из URL текущей страницы.
