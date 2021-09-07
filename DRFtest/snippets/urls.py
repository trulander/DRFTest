from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
# ]

# на основе функций
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>', views.snippet_detail)
# ]

# на основе классов представлений
urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

#добавление обработки типа контента через заголовок Accept
urlpatterns = format_suffix_patterns(urlpatterns)