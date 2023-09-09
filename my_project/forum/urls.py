from django.urls import path
from forum import views


urlpatterns = [
    path('', views.TopicsIndexView.as_view(), name='all_topics'),
    path('new_topic', views.CreateTopicView.as_view(), name='add_topic'),
    path('detail_topic/<int:id>', views.DetailTopicView.as_view(), name='detail_topic'),
    path('new_comment/<int:id>', views.AddCommentView.as_view(), name='new_comment'),
    path('comments/add/', views.CommentCreateView.as_view(), name='comment_create'),
]
