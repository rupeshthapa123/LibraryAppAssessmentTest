from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='book'),
    path('upload/', views.upload, name='Upload Book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
]