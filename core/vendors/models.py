from django.db import models
from django.utils.translation import ugettext_lazy as _


class VendorCategory(models.Model):
    """ Vendor category model """
    name = models.CharField(_('Vendor Category Name'), max_length=255)

    def __str__(self):
        return self.name


class VendorTag(models.Model):
    """ Vendor tag model  """
    name = models.CharField(_('Vendor Category tag'), max_length=255)

    def __str__(self):
        return self.name


class VendorReview(models.Model):
    """ Vendor review model """
    MAX_STARS = 5

    VENDOR_REVIEW_STARS = [(i, i) for i in range(1, MAX_STARS + 1)]

    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    content = models.TextField()

    author = models.ForeignKey("members.Member", on_delete=models.DO_NOTHING)
    stars = models.PositiveSmallIntegerField(choices=VENDOR_REVIEW_STARS)
    vendor = models.ForeignKey(
        'Vendor', on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.author}"


class Vendor(models.Model):
    """ Vendor model """

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    VENDOR_STATUS = [(ACTIVE, ACTIVE), (INACTIVE, INACTIVE)]

    creation_date = models.DateField(
        _('Vendor System Creation date'), auto_now_add=True)
    update_date = models.DateField(_('Vendor update date'), auto_now=True)
    name = models.CharField(_('Vendor Name'), max_length=255)
    code = models.CharField(_('Vendor Code'), max_length=255, unique=True)
    country = models.CharField(_('Vendor Country'), max_length=255)
    status = models.CharField(
        _('Vendor Status'), choices=VENDOR_STATUS, max_length=10)
    categories = models.ManyToManyField(
        'VendorCategory', related_name="vendors", blank=True)
    tags = models.ManyToManyField(
        'VendorTag', related_name="vendors", blank=True)

    address = models.CharField(_('Vendor Street Address'), max_length=255)
    city = models.CharField(_('Vendor City Address'), max_length=255)
    zip = models.CharField(_('Vendor Zip Code Address'), max_length=255)
    phone = models.CharField(_('Vendor Phone number'), max_length=255)
    vat_number = models.CharField(
        _('Vendor VAT Number'), max_length=30, blank=True, null=True)
    iban = models.CharField(
        _('Vendor IBAN number'), max_length=30, blank=True, null=True)

    @property
    def avg_stars(self):
        """ Average reviews stars """
        reviews = list(self.reviews)
        return sum([review.star for review in reviews]) / len(reviews)

    def __str__(self):
        return self.name
