# locallibrary

Проект - тестовое задание с построением древовидного меню. 

Главная страница выглядит так:

![image](https://user-images.githubusercontent.com/33355208/218150985-0899548c-ab65-4b44-987e-40591c2de844.png)


За основу взят учебный проект по Django от Mozilla - библиотека. На скриншоте два меню "main menu" и "About", реализованы через template tag.


![image](https://user-images.githubusercontent.com/33355208/218151410-ee2dc4ad-daa5-4137-80c6-c91cde662687.png)


"main menu":

![image](https://user-images.githubusercontent.com/33355208/218151067-911312de-7745-473d-ac4c-fd6858b12f31.png)

![image](https://user-images.githubusercontent.com/33355208/218151105-f39cf340-2d6e-409b-baaf-43ec5c5ef0e2.png)


"About":

![image](https://user-images.githubusercontent.com/33355208/218151168-ada2fca1-6dac-4b74-8cec-814002248d3b.png)

Файлы содержащие дерево: 
- catalog/templates/navigation_tree.html 
- catalog/templates/navigation_drawnodes.htmll 
- catalog/models.py Модели: NavigationTree, NavigationMenu
- catalog/templatetags/nav_menu.py


Применены стили bootstrap (dropdown menu). Меню определяются по названию и настраиваются через админку. Там можно создать меню и дерево меню. Админка: admin/admin. 

![image](https://user-images.githubusercontent.com/33355208/218151823-0ecb0d05-471e-482a-addc-776020842727.png)

Конечные и промежуточные точки меню (кроме корневой) содержат ссылки. Порядок определяется полем order. 

Для отрисовки одного меню выполняется один SQL-запрос:


![image](https://user-images.githubusercontent.com/33355208/217704015-6b66cea4-fc0f-4859-a7e1-01cb4f5af5c2.png)


Не используются сторонние библиотеки, кроме django-debug для отладки.

Меню добавляется с помощью тегов:
{% draw_menu "main menu" %}
{% draw_menu "About" %}

![image](https://user-images.githubusercontent.com/33355208/218151968-b46a22bf-e738-4b4d-9b03-c9b1f453885d.png)

Есть определенные проблемы с внешним видом - не сильно заморочено.


В базе, NavigationMenu:
![image](https://user-images.githubusercontent.com/33355208/217705198-5b2b4842-9439-4e98-9416-0a693d030466.png)

NavigationTree:
![image](https://user-images.githubusercontent.com/33355208/218152024-a6295d43-fb1f-480b-8233-f6201ed0d967.png)

Пункты тестового задания выполнены все кроме 5: Активный пункт меню определяется исходя из URL текущей страницы.
