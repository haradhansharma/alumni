from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'Alumni Super Admin Area'
admin.site.site_title = 'Operation Interface'
admin.site.index_title = 'Alumni Super Administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]
