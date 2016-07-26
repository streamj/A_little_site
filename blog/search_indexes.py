from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # every search engine required one of its fields has document=True,
    #  this field is primary search field
    # use_template=True indicate this field will be rendered to a data template
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='publish')

    # this method hase to return the model for the QuerySet for objects that
    # will be indexed
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().published.all()
