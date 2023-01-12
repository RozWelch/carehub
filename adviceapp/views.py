from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Carearticle
from .forms import Article_commentsForm


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
                "commented": False,
                "helpful_ticks": helpful_ticks,
                "comment_form": Article_commentsForm()
            },
        )


    def post(self, request, slug, *arges, **kwargs):
        queryset = Carearticle.objects.filter(approved_status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        helpful_ticks = False
        if post.helpful_ticks.filter(id=self.request.user.id).exists():
            helpful_ticks = True

        comment_form = Article_commentsForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            # comment.post = post
            comment.article_comment = post
            comment.save()
        else:
            comment_form = Article_commentsForm


        return render(
            request, 
            "post_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "helpful_ticks": helpful_ticks,
                "comment_form": Article_commentsForm()
            },
        )

"""Displays if the post is ticked as helpful"""
class CarearticleTick(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.helpful_ticks.filter(id=request.user.id).exists():
            post.helpful_ticks.remove(request.user)
        else:
            post.helpful_ticks.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        