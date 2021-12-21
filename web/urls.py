from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', include((
        path('', views.list_of_users, ),
        path('<slug:username>', views.user_profile, ),
        path('<slug:username>/posts', views.user_posts, ),
        path('<slug:username>/posts/<int:post_id>', views.user_posts, ),

        path('<slug:username>/follows', views.user_follows, ),
        path('<slug:username>/followers', views.user_followers, ),

    ))),
    path('bookmarks/posts', views.bookmarks_posts),
    path('bookmarks/comments', views.bookmarks_comments),
    path('messenger', views.dialogs),
    path('bookmarks/dialog/<int:dialog_id>', views.dialogs),
    path('posts', views.user_posts),
    path('posts/<post_id>', views.user_posts),
    path('posts/<post_id>/comments', views),
    path('feed', views.feed),
    path('profile', views.user_profile),
]
