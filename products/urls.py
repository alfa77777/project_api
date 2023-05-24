from django.urls import path

from products.views import (
    ProductListCreateView, ProductDetailView, CommentListCreateView, CommentDetailView,
    ProductLikeDislikeView
)

urlpatterns = [
    path("comments/", CommentListCreateView.as_view(), name="comment_list_create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment_detail"),
    path("<slug:slug>/like_dislike/", ProductLikeDislikeView.as_view(), name="blog_like_dislike"),
    path("", ProductListCreateView.as_view(), name="products_list_create"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),

]
