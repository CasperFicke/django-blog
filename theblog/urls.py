from django.urls import path

# import views
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, CategoryListView, AddCategoryView, CategoryView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    # show all posts
    path ('', HomeView.as_view(), name="home"),
    # show single post url
    path ('posts/<int:pk>', PostView.as_view(), name='post-view'),
    # add post
    path ('add_post/', AddPostView.as_view(), name='add_post'),
    # edit post
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    # delete post
    path('post/<int:pk>', DeletePostView.as_view(), name='delete_post'),

    # show all categories
    path ('categories/', CategoryListView, name='category-list'),
    # add category
    path ('add_category/', AddCategoryView.as_view(), name='add_category'),

    # show all posts with same category
    path('category/<str:cats>/', CategoryView, name='category'),
    
    # like a post
    path('like/<int:pk>', LikeView, name='like_post'),

    # add comment
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
