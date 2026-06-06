from django.urls import path
from records.views import records, create_record, update_record, delete_record

urlpatterns = [
    path('', records, name='main'),
    path('create/', create_record, name='create'),
    path('update/<int:pk>/', update_record, name='update'),
    path('delete/<int:pk>/', delete_record, name='delete'),
]