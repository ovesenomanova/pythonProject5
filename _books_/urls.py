from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('writers/', include('apps.writers.urls')),
    path('books/', include('apps.books.urls'))
]
