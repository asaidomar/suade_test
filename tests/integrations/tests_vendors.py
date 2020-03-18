#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : tests_vendors
# date : 2020-03-17
# project: suade_test
# author : alisaidomar
from random import randint

import pytest
from django.urls import reverse

from core.vendors import models as vendor_models
from ..base import TestBase


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestCategoryAPI(TestBase):
    """ core.vendors.models.VendorCategory API tests """

    def test_create_category(self):
        def category_factory(**kwargs):  # noqa
            return {
                "name": "test_name"
            }

        self._test_create_resource(
            reverse("vendorcategory-list"),
            vendor_models.VendorCategory,
            category_factory
        )

    def test_get_categories(self, create_category):
        ret = self._test_get_resource(reverse("vendorcategory-list"))
        assert ret.json()[0]['id'] == create_category.pk

    def test_get_category(self, create_category):
        path = reverse("vendorcategory-detail",
                       kwargs={"pk": create_category.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_category.pk

    def test_patch_category(self, create_category):
        def category_factory(**kwargs):  # noqa
            return {
                "name": create_category.name + "Update"
            }

        path = reverse("vendorcategory-detail",
                       kwargs={"pk": create_category.pk})
        self._test_patch_resource(
            path,
            vendor_models.VendorCategory,
            category_factory
        )

    def test_delete_category(self, create_category):
        path = reverse("vendorcategory-detail",
                       kwargs={"pk": create_category.pk})
        self._test_delete_resource(path)


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestTagAPI(TestBase):
    """ core.vendors.models.VendorTag API tests """

    def test_create_tag(self):
        def tag_factory(**kwargs):  # noqa
            return {
                "name": "test_name"
            }

        self._test_create_resource(
            reverse("vendortag-list"),
            vendor_models.VendorTag,
            tag_factory
        )

    def test_get_tags(self, create_tag):
        ret = self._test_get_resource(reverse("vendortag-list"))
        assert ret.json()[0]['id'] == create_tag.pk

    def test_get_tag(self, create_tag):
        path = reverse("vendortag-detail",
                       kwargs={"pk": create_tag.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_tag.pk

    def test_patch_tag(self, create_tag):
        def tag_factory(**kwargs):  # noqa
            return {
                "name": create_tag.name + "Update"
            }

        path = reverse("vendortag-detail",
                       kwargs={"pk": create_tag.pk})
        self._test_patch_resource(
            path,
            vendor_models.VendorTag,
            tag_factory
        )

    def test_delete_tags(self, create_tag):
        path = reverse("vendortag-detail",
                       kwargs={"pk": create_tag.pk})
        self._test_delete_resource(path)


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestVendorAPI(TestBase):
    """ core.vendors.models.Vendor API tests """

    def test_create_vendor(self, create_member, create_tag, create_category):
        def vendor_factory(**kwargs):  # noqa
            vendor_data_dict = {
                'name': 'Craig Golden',
                'code': 'mbGNFdFHzxCPIjHRBGCv',
                'country': 'Montserrat',
                'status': 'active',
                'address': '4481 Li Lights',
                'city': 'West Justinmouth',
                'zip': 'EJrYucOGBvLHBmfGEhTk',
                'phone': '084.552.5679',
                'vat_number': "FR45555",
                'iban': "546667888991001",
                'categories': [create_category.pk],
                'tags': [create_tag.pk],
                "vat_rate": 20

            }
            return vendor_data_dict

        self._test_create_resource(
            reverse("vendor-list"),
            vendor_models.Vendor,
            vendor_factory
        )

    def test_get_vendors(self, create_vendor):
        ret = self._test_get_resource(reverse("vendor-list"))
        assert ret.json()[0]['id'] == create_vendor.pk

    def test_get_vendor(self, create_vendor):
        path = reverse("vendor-detail",
                       kwargs={"pk": create_vendor.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_vendor.pk

    def test_patch_vendor(self, create_vendor):
        def vendor_factory(**kwargs):  # noqa
            return {
                "name": create_vendor.name + "Update"
            }

        path = reverse("vendor-detail",
                       kwargs={"pk": create_vendor.pk})
        self._test_patch_resource(
            path,
            vendor_models.Vendor,
            vendor_factory
        )

    def test_delete_vendor(self, create_vendor):
        path = reverse("vendor-detail",
                       kwargs={"pk": create_vendor.pk})
        self._test_delete_resource(path)


@pytest.mark.urls('config.urls')
@pytest.mark.django_db
class TestReviewAPI(TestBase):
    """ core.vendors.models.VendorReview API tests """

    def test_create_review(self, create_member, create_vendor):
        def review_factory(**kwargs):  # noqa

            return {
                "content": "test_content",
                "author": create_member.pk,
                "stars": randint(1, vendor_models.VendorReview.MAX_STARS),
                "vendor": create_vendor.pk
            }

        self._test_create_resource(
            reverse("vendorreview-list"),
            vendor_models.VendorReview,
            review_factory
        )

    def test_get_reviews(self, create_review):
        ret = self._test_get_resource(reverse("vendorreview-list"))
        assert ret.json()[0]['id'] == create_review.pk

    def test_get_review(self, create_review):
        path = reverse("vendorreview-detail",
                       kwargs={"pk": create_review.pk})
        ret = self._test_get_resource(path)
        assert ret.json()['id'] == create_review.pk

    def test_patch_review(self, create_review):
        def review_factory(**kwargs):  # noqa
            return {
                "content": create_review.content + "Update"
            }

        path = reverse("vendorreview-detail",
                       kwargs={"pk": create_review.pk})
        self._test_patch_resource(
            path,
            vendor_models.VendorReview,
            review_factory
        )

    def test_delete_categories(self, create_review):
        ret = self._test_get_resource(reverse("vendorreview-list"))
        assert len(ret.json()) >= 1
