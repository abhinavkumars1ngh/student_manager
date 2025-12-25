from django.contrib import admin
from django.urls import path
from users.views import login_view, logout_view
from tasks.views import dashboard, add_task, delete_task, toggle_task
from notes.views import add_note, delete_note

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),

    path('add-task/', add_task, name='add_task'),
    path('delete-task/<int:id>/', delete_task, name='delete_task'),
    path('toggle-task/<int:id>/', toggle_task, name='toggle_task'),

    path('add-note/', add_note, name='add_note'),
    path('delete-note/<int:id>/', delete_note, name='delete_note'),
]