# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
# from django.views import View
# from django.views.generic import CreateView, UpdateView, DeleteView
#
# from ..forms import CommentForm
# from ..models import Article, Comment
#
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumView(DetailView):
    template_name = "albums/album_view.html"
    model = Album


class CreateAlbum(PermissionRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/create.html"

    def form_valid(self, form):

        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:AlbumView", kwargs={"pk": self.object.pk})
#
#
class UpdateAlbum(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    template_name = "albums/update.html"
    model = Album
    permission_required = 'webapp:change_album'


    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        album = get_object_or_404(Album, pk=pk)
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse("webapp:AlbumView", kwargs={"pk": self.object.pk})
#
#
class DeleteAlbum(PermissionRequiredMixin,DeleteView):
    model = Album
    template_name = "albums/delete.html"
    success_url = reverse_lazy('webapp:index')
    permission_required = "webapp.delete_album"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

class AddFavoriteAlbum(View):

    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        user=self.request.user
        album.favorites.add(user)
        album.save()
        return redirect('webapp:index')
#
# class CreateLikeComment(View):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         print(pk)
#         comment = get_object_or_404(Comment, pk=pk)
#         print(comment)
#         user = self.request.user
#         if comment.user.filter(id=user.pk):
#             print(comment.user.filter(id=user.pk))
#             comment.user.remove(user.pk)
#         else:
#             comment.user.add(user)
#         likes = len(comment.user.all())
#         param = {'likes': likes}
#
#         return JsonResponse(param)
#
