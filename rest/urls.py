from django.urls import path,include
from .views import ArticleList,ArticleDetail,Articlegenericview
#noinspection PyUnresolvedReferences
from .views import ArticleViewset
#noinspection PyUnresolvedReferences
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('article',ArticleViewset,basename='article')


urlpatterns=[
    path('article/',ArticleList.as_view()),
    path('article/<int:pk>/',ArticleDetail.as_view()),
    path('generic/article/<int:id>/',Articlegenericview.as_view()),
    path('viewset/',include(router.urls)),
    ]
