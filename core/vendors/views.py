#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : views
# date : 2020-03-16
# project: suade_test
# author : alisaidomar

from rest_framework import viewsets
from rest_framework import permissions

from core.vendors import serializers as vendor_serializers
from core.vendors import models as vendor_models


class VendorViewSet(viewsets.ModelViewSet):
    """ Vendor view Set """
    model = vendor_models.Vendor
    serializer_class = vendor_serializers.VendorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = vendor_models.Vendor.objects


class CategoryViewSet(viewsets.ModelViewSet):
    """ Category view Set """
    model = vendor_models.VendorCategory
    serializer_class = vendor_serializers.VendorCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = vendor_models.VendorCategory.objects


class TagViewSet(viewsets.ModelViewSet):
    """ Category view Set """
    model = vendor_models.VendorTag
    serializer_class = vendor_serializers.VendorTagSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = vendor_models.VendorTag.objects


class ReviewViewSet(viewsets.ModelViewSet):
    """ Category view Set """
    model = vendor_models.VendorReview
    serializer_class = vendor_serializers.VendorReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = vendor_models.VendorReview.objects
