from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    # by default, django call the get_absolute_url() on each object
    def items(self):
        return Post.published.all()

    # lastmod, retrieve each object returned by items()
    def lastmod(self, obj):
        return obj.publish
