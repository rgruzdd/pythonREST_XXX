from django.contrib import admin
from django.contrib.admin import site
from django.urls import path, include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include("ac_users.urls")),
    path('api/', include("students.urls")),
    path('api/', include("teachers.urls")),
    path('api/', include("web_details.urls")),

]


# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]
#
#
# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename='women')
# print(router.urls)