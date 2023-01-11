from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Carearticle


"""Displays all articles in the browse articles page"""
class CarearticleList(generic.ListView):
    model = Carearticle
    queryset = Carearticle.objects.filter(approved_status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

"""Displays single articles view with all content and comments"""
class CarearticleDetail(View):

    def get(self, request, slug, *arges, **kwargs):
        queryset = Carearticle.objects.filter(approved_status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        helpful_ticks = False
        if post.helpful_ticks.filter(id=self.request.user.id).exists():
            helpful_ticks = True

        return render(
            request, 
            "post_details.html",
            {
                "post": post,
                "comments": comments,
                "helpful_ticks": helpful_ticks
            },
        )