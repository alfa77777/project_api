from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from paginations import CustomPageNumberPagination
from products.models import Product
# from products.models.comment import Comment
from products.serializers import ProductListSerializer, ProductCreateSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("category", "brand")
    ordering_fields = ("id", "price")
    search_fields = ("title", "category__title", "brand__title")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductListSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    # serializer_class = ProductListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProductCreateSerializer
        return ProductListSerializer


# class CommentListCreateView(generics.ListCreateAPIView):
#     queryset = Comment.objects.order_by("-id")
#     filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
#     filterset_fields = ("product", "timestamp")
#     ordering_fields = ("product",)
#     pagination_class = CustomPageNumberPagination
#
#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             return CommentCreateSerializer
#         return CommentListSerializer
#
#
# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     # serializer_class = ProductListSerializer
#     lookup_field = "id"
#
#     def get_serializer_class(self):
#         if self.request.method in ["PUT", "PATCH"]:
#             return CommentCreateSerializer
#         return CommentListSerializer

