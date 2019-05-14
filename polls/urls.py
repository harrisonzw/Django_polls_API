# # from django.conf.urls import url
# from django.urls import path, include
# from . import views
# # from polls.views import vote
# from rest_framework.routers import DefaultRouter

# app_name ="polls"

# router = DefaultRouter()
# router.register('', views.QuestionViewSet, base_name='questions')
# urlpatterns = router.urls

# path('questions/<int:question_id>/', views., name=' '),

# # urlpatterns = [
# #     path('', views.index, name='index'),
# #     path('<int:question_id>/', views.detail, name='detail'),
# #     path('<int:question_id>/results/', views.results, name='results'),
# #     path('<int:question_id>/vote/', views.vote, name='vote'),

# #     path(r'', include(router.urls)),
# #     #path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
# # ]

from django.urls import path
from . import apiviews

app_name = 'polls'
urlpatterns = [
    path('questions/', apiviews.questions_view, name='questions_view'),
    path('questions/<int:question_id>/', apiviews.question_detail_view, name='question_detail_view'),
    path('questions/<int:question_id>/choices/', apiviews.choices_view, name='choices_view'),
    path('questions/<int:question_id>/vote/', apiviews.vote_view, name='vote_view'),
    path('questions/<int:question_id>/result/', apiviews.question_result_view, name='question_result_view'),
]