from django.db.models import Count
from .models import Post


def get_latest_posts(count=3):
    return Post.published.order_by('-publish')[:count]


def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('post_comments')).order_by('-total_comments', '-publish')[:count]


def get_similar_posts(post_id, count=3):
    post = Post.objects.get(pk=post_id)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in=post_tags_ids).exclude(id=post.id)
    return similar_posts.annotate(same_tags=Count(
        'tags')).order_by('-same_tags', '-publish')[:count]
