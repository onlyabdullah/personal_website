from django import template
import blog.helpers as helpers

register = template.Library()


@register.inclusion_tag('blog/partials/latest_posts.html')
def latest_posts(count=3):
    return {'latest_posts': helpers.get_latest_posts(count)}


@register.inclusion_tag('blog/partials/most_commented_posts.html')
def most_commented_posts(count=3):
    return {'most_commented_posts': helpers.get_most_commented_posts(count)}


@register.inclusion_tag('blog/partials/similar_posts.html')
def similar_posts(post_id, count=3):
    return {'similar_posts': helpers.get_similar_posts(post_id, count)}
