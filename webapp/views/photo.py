# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.models import Permission
# from django.db.models import Q
# from django.http import JsonResponse
# from django.shortcuts import redirect, get_object_or_404
# from django.urls import reverse_lazy
#
# # Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
# from django.views import View
#
# from ..forms import ArticleForm, SearchForm, ArticleDeleteForm, UserArticleForm
# from ..models import Article
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#
#
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    model = Photo
    template_name = "photos/index.html"
    context_object_name = "photos"
    ordering = "-updated_at"
    paginate_by = 6


    def get_queryset(self):
        return Photo.objects.filter(is_public=1).order_by("-created_at")



class PhotoView(DetailView):
    template_name = "photos/photo_view.html"
    model = Photo

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['albums'] = self.object.albums.order_by("-created_at")
    #     return context
#
#
class CreatePhoto(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photos/create.html"


    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)
#
    def get_success_url(self):
        return reverse('webapp:PhotoView', kwargs={'pk': self.object.pk})



class UpdatePhoto(PermissionRequiredMixin, UpdateView):
    form_class = PhotoForm
    template_name = "photos/update.html"
    model = Photo

    def has_permission(self):
        return self.request.user.has_perm("webapp.change_photo") or \
               self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:PhotoView', kwargs={'pk': self.object.pk})
#
#
class DeletePhoto(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    success_url = reverse_lazy('webapp:index')
    permission_required = "webapp.delete_photo"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

class AddFavoritePhoto(View):

    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        user=self.request.user
        photo.favorites.add(user)
        photo.save()
        return redirect('webapp:index')




#
# class CreateLike(View):
#     def get(self, request, *args, **kwargs):
#         pk=kwargs.get('pk')
#         article=get_object_or_404(Article,pk=pk)
#         user = self.request.user
#         if article.user.filter(id=user.pk):
#             article.user.remove(user)
#         else:
#             article.user.add(user)
#         likes=len(article.user.all())
#         param={'likes':likes, 'pk': article.pk}
#
#
#         return JsonResponse(param)
