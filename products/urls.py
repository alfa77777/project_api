from django.urls import path

from products.views import (
    ProductListCreateView, ProductDetailView, CommentListCreateView, CommentDetailView, BlogLikeDislikeView
)

urlpatterns = [
    path("comments/", CommentListCreateView.as_view(), name="comment_list_create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment_detail"),
    path("<slug:slug>/like_dislike/", BlogLikeDislikeView.as_view(), name="blog_like_dislike"),
    path("", ProductListCreateView.as_view(), name="products_list_create"),
    # path("<int:pk>/", ProductRetrieveView.as_view(), name="product_read"),
    # path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    # path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),

]
