from rest_framework import serializers

from common.models import Category
from products.models import Product, LikeDislike
from products.models.comment import Comment
from users.models import User


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class ProductListSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "title", "slug", "price", "image", "category", "likes", "dislikes"]


class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Product
        fields = ["id", "title", "slug", "price", "category"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = ProductCategorySerializer(instance.category).data
        return data


class BlogLikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.LikeType.choices)


class CommentList(serializers.ModelSerializer):
    model = Comment
    fields = "__all__"


class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)


class CommentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title",)


class CommentListSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer()
    product = CommentProductSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = CommentUserSerializer(instance.user).data
        data["product"] = CommentProductSerializer(instance.product).data
        return data
