from django.urls import path
from django.views.generic import RedirectView

from webapp.views import IndexView, CreatePhoto, PhotoView, UpdatePhoto, DeletePhoto, AlbumView, CreateAlbum, \
    UpdateAlbum, DeleteAlbum, AddFavPhoto, AddFavAlbum

app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path('photos/', RedirectView.as_view(pattern_name="index")),
    path('photos/add/', CreatePhoto.as_view(), name="CreatePhoto"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="PhotoView"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="UpdatePhoto"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="DeletePhoto"),
    path('albums/<int:pk>/', AlbumView.as_view(), name="AlbumView"),
    path('albums/add/', CreateAlbum.as_view(), name="CreateAlbum"),
    # path('article/<int:pk>/comment/add/', CreateCommentView.as_view(), name="article_comment_create"),
    path('albums/<int:pk>/update/', UpdateAlbum.as_view(), name="UpdateAlbum"),
    path('albums/<int:pk>/delete/', DeleteAlbum.as_view(), name="DeleteAlbum"),

    path('photos/<int:pk>/favorite', AddFavPhoto.as_view(),name="AddFavPhoto"),
    path('albums/<int:pk>/favorite', AddFavAlbum.as_view(),name="AddFavAlbum"),
]
