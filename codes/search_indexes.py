from .models import Code
from haystack import indexes

class CodeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Code

    def index_queryset(self, using=None):
        return self.get_model().objects.all()