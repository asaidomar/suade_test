from django.db import models
from django.utils.translation import ugettext_lazy as _


class VendorCategory(models.Model):
    """ Vendor category model """
    name = models.CharField(_('Vendor Category Name'), max_length=255)


class VendorTag(models.Model):
    """ Vendor tag model  """
    name = models.CharField(_('Vendor Category tag'), max_length=255)


class VendorReview(models.Model):
    """ Vendor review model """
    MAX_STARS = 5

    VENDOR_REVIEW_STARS = [ (i, i) for i in range(1, MAX_STARS + 1)]

    creation_date = models.DateField(auto_created=True)
    update_date = models.DateField(auto_now=True)
    content = models.TextField()

    author = models.ForeignKey("members.Member", on_delete=models.DO_NOTHING)
    stars = models.PositiveSmallIntegerField(choices=VENDOR_REVIEW_STARS)
    vendor = models.ForeignKey(
        'Vendor', on_delete=models.CASCADE, related_name="reviews")


class Vendor(models.Model):
    """ Vendor model """

    ACTIVE = 'active'
    NOACTIVE = 'active'

    VENDOR_STATUS = [(ACTIVE, ACTIVE), (NOACTIVE, NOACTIVE)]

    creation_date = models.DateField(auto_created=True)
    update_date = models.DateField(auto_now=True)
    name = models.CharField(_('Vendor Name'), max_length=255)
    code = models.CharField(_('Vendor Code'), max_length=255, unique=True)
    country = models.CharField(_('Vendor Country'), max_length=255)
    status = models.CharField(_('Vendor Status'), choices=VENDOR_STATUS)
    categories = models.ManyToManyField(
        'VendorCategory', related_name="vendors")

    @property
    def avg_stars(self):
        reviews = list(self.reviews)
        return sum([review.star for review in reviews]) / len(reviews)
