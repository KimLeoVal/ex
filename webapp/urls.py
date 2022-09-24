from django.urls import path
from django.views.generic import RedirectView

from webapp.views import IndexView, CreatePhoto, PhotoView, UpdatePhoto, DeletePhoto, AlbumView, CreateAlbum, \
    UpdateAlbum, DeleteAlbum, AddFavoritePhoto, AddFavoriteAlbum

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
    path('photo/<int:pk>/favorite/', AddFavoritePhoto.as_view(), name='AddFavoritePhoto'),
    path('albums/<int:pk>/favorite/', AddFavoriteAlbum.as_view(), name='AddFavoriteAlbum'),
    # path('photos/<int:pk>/like', CreateLike.as_view(),name="CreateLike"),
    # path('comment/<int:pk>/like', CreateLikeComment.as_view(),name="CreateLikeComment"),
]
