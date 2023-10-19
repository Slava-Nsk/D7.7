from django.urls import path
from .filters import PostFilter
from .views import PostsSearch, PostsList, PostDetail, PostNewsCreate, PostNewsUpdate, PostNewsDelete, PostArticleCreate, PostArticleUpdate, PostArticleDelete

urlpatterns = [
    path('', PostsList.as_view(), name='posts_list_name'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail_name'),
    path('news/create/', PostNewsCreate.as_view(), name='create_news_name'),
    path('news/<int:pk>/update', PostNewsUpdate.as_view(), name='update_news_name'),
    path('news/<int:pk>/delete', PostNewsDelete.as_view(), name='delete_news_name'),

    path('article/create/', PostArticleCreate.as_view(), name='create_article_name'),
    path('article/<int:pk>/update', PostArticleUpdate.as_view(), name='update_article_name'),
    path('article/<int:pk>/delete', PostArticleDelete.as_view(), name='delete_article_name'),

    path('search/', PostsSearch.as_view(), name='posts_search_name'),

]
