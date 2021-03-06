from django.db.models.query import QuerySet
from django.utils import timezone

class BaseQuerySet(QuerySet):
    """
    BaseQuerySet for the project contains the base queryset related properties and methods.
    """
    def delete(self):
        return super(BaseQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(BaseQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)
