#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : serializers
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from rest_framework import serializers
from core.vendors.models import (
    Vendor, VendorCategory, VendorReview, VendorTag)


class VendorSerializer(serializers.ModelSerializer):
    """ core.vendors.models.Vendor Serializer,
    used by core.vendors.api.views.VendorsListView """

    class Meta:
        """Meta class information """
        model = Vendor
        fields = '__all__'
        read_only_fields = ("pk", "creation_date", "update_date")


class VendorCategorySerializer(serializers.ModelSerializer):
    """ core.vendors.models.VendorCategory Serializer,
    used by core.vendors.api.views.VendorCategoryViewSet """

    class Meta:
        """Meta class information """
        model = VendorCategory
        fields = '__all__'
        read_only_fields = ("pk", )


class VendorReviewSerializer(serializers.ModelSerializer):
    """ core.vendors.models.VendorReview Serializer,
    used by core.vendors.api.views.VendorReviewViewSet """

    class Meta:
        """Meta class information """
        model = VendorReview
        fields = '__all__'
        read_only_fields = ("pk", 'creation_date', 'update_date')


class VendorTagSerializer(serializers.ModelSerializer):
    """ core.vendors.models.VendorTag Serializer,
    used by core.vendors.api.views.VendorTagViewSet """

    class Meta:
        """Meta class information """
        model = VendorTag
        fields = '__all__'
        read_only_fields = ("pk", )
