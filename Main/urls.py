from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Buniwa.urls')),
]

# Custom 404 view
# handler404 = four


admin.site.site_header = "Buniwa site admin (DEV)"
admin.site.site_title = "Buniwa | Admin"
admin.site.index_title = "Buniwa administration"