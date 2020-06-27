from django.shortcuts import redirect
from django.views import generic as generic_views
from taggit.models import Tag

from .models import Post, Comment
from .forms import CommentsCreateForm


class PostsListView(generic_views.ListView):
    model = Post
    paginate_by = 5
    tag = None
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if (self.tag):
            return Post.objects.filter(tags__in=[self.tag])
        return Post.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context

    def dispatch(self, request, tag_slug=None, *args, **kwargs):
        if tag_slug:
            self.allow_empty = False
            self.tag = Tag.objects.get(slug=tag_slug)
        return super(PostsListView, self).dispatch(request, *args, **kwargs)


class PostsDetailView(generic_views.DetailView):
    model = Post
    template_name = 'blog/posts_detail.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        comment_form = CommentsCreateForm(data=request.POST)
        if comment_form.is_valid():
            self.object = self.get_object()
            new_comment = comment_form.save(commit=False)
            new_comment.post = self.object
            new_comment.save()
            return redirect('blog:posts_detail', pk=self.object.pk, slug=self.object.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = CommentsCreateForm
        return context
