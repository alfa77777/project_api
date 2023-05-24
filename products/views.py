from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from paginations import CustomPageNumberPagination
from products.models import Product, LikeDislike
from products.models.comment import Comment
from products.serializers import ProductListSerializer, ProductCreateSerializer, CommentCreateSerializer, \
    CommentListSerializer, ProductLikeDislikeSerializer


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


class ProductLikeDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ProductLikeDislikeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ProductLikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        type_ = serializer.validated_data.get("type")
        user = request.user
        product = Product.objects.filter(slug=self.kwargs.get("slug")).first()
        if not product:
            raise Http404
        like_dislike_blog = LikeDislike.objects.filter(product=product, user=user).first()
        if like_dislike_blog and like_dislike_blog.type == type_:
            like_dislike_blog.delete()
        else:
            LikeDislike.objects.update_or_create(product=product, user=user, defaults={"type": type_})
        data = {"type": type_, "detail": "Liked or disliked."}
        return Response(data)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("product", "timestamp")
    ordering_fields = ("product",)
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentCreateSerializer
        return CommentListSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    # serializer_class = ProductListSerializer
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CommentCreateSerializer
        return CommentListSerializer
