# Django Course


## Part 1: Create the menu page

- step 1: create the data in model.py
    ```python
    from django.db import models

    class Booking(models.Model):
        first_name = models.CharField(max_length=200)    
        last_name = models.CharField(max_length=200)
        guest_number = models.IntegerField()
        comment = models.CharField(max_length=1000, default="No comment")
            def __str__(self):
                return self.first_name + ' ' + self.last_name
            
    class Menu(models.Model):
        name = models.CharField(max_length=200)
        price = models.IntegerField()
        def __str__(self):
            return self.name
    ```
- step 2: register your model in admi.py
    ```python
    # admin.py
    from django.contrib import admin
    from .models import Menu  # Replace YourModel with the actual model name

    admin.site.register(Menu)
    ```
- step 3: make migrations

    Register the app and create a model Booking and Menu, then make migrations.

    Migrations:
    ```python
    python manage.py makemigrations
    python manage.py migrate 
    ```
- step 4: urls configurations
    ```python
    # project level
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('restaurant.urls')),
    ]

    # app level
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
        path('book/', views.book, name='book'),
        path('menu/', views.menu, name='menu'),
    ]
    ```

- step 5: create a superuser
    ```bash
    python3 manage.py createsuperuser
    ```
    - Username: bistroadmin
    - Email address: admin@littlelemon.com  
    - Password: lemon@786!

- step 6: Run the server and go to admin panel

- step 7: Add data to menu model from panel
    
- step 8: back to views.py

- step 9: create menu page

- step 10: add view logic inside the view menu

    ```python
    def menu(request):
        menu_data = Menu.objects.all()
        main_data = {
            "menu": menu_data, 
        }
        return render(request, 'menu.html', main_data)
    ```
- step 11: Add URL path for the view menu funtion

- step 12: go to html templates

- step 13: create menu.html
- step 14: modify menu.html
    ```html
    {% extends 'base.html' %}
    {% load static %}
    {% block content %}
        <h1>Menu</h1>
        <div class="column">
            {% for item in menu %}
                <p>
                    {{ item.name }}
                    <span class="menu-price">${{ item.price }}.00</span>
                </p>
            {% endfor %}
        </div>
    {% endblock %}
    ```

## Part 2: Create the menu item page

- step 1: add attribute 'menu_item_description' to model menu

- step 2: open Django admi and edit the items of menu

- step 3: create a view called 'display_menu_item'

- step 4: define the view logic for the view 'display_menu_item'
    ```python
    def display_menu_item(request, pk):
        if pk:
            menu_item = Menu.objects.get(pk=pk)
        else:
            menu_item = ""
        return render(request, 'menu_item.html', {'menu_item':menu_item})
    ```

- step 5: add the new view to url
    ```python
    path('menu_item/<int:pk>/', views.display_menu_item, name='menu_item')
    ```

- step 6: add link to menu item in menu.html to the menu_item.html
    ```html
    <a href="{% url 'menu_item' pk=item.pk %}">
        {{ item.name }}
    </a>
    ```

- step 7: create the menu_item.html

- step 8: template menu_item.html

- step 9: modifies the menu_item.html

    ```html
    {% extends 'base.html' %} 
    {% load static %} 
    {% block content %}
    <section>
    <article>

        <h1>Menu item</h1>

        <span>
            <a href="{% url 'home' %}">Home</a> /
            <a href="{% url 'menu' %}">Menu</a>/
        </span>

        <div class="row">
            <div class="column">
                <h2>{{ menu_item.name }}</h2>
                <p>{{ menu_item.menu_item_description}}</p>
                <p>${{ menu_item.price }}</p>
            </div>

            <div class="column">
                <img src="/static/img/menu_items/{{menu_item.name}}.jpg" alt="{{ menu_item.name}}" />
            </div>
        </div>

    </article>
    </section>
    {% endblock %}
    ```

## Part 3: Create the footer template
