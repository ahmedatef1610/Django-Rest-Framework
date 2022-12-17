from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title

###########################################


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):

    # user = UserPublicSerializer(read_only=True)
    # user = UserPublicSerializer(read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)

    # related_products = ProductInlineSerializer(source='user.product_set.all', many=True, read_only=True)

    # my_discount = serializers.SerializerMethodField(read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)

    edit_url = serializers.SerializerMethodField(read_only=True)

    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    # url = serializers.HyperlinkedIdentityField(view_name='products-detail', lookup_field='pk')

    # email = serializers.EmailField(write_only=True)

    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])

    # name = serializers.CharField(source='title', read_only=True)
    # email = serializers.EmailField(source='user.email', read_only=True)

    # reviews = ReviewSerializer(source='review_set', many=True)
    
    body = serializers.CharField(source='content')
    
    class Meta:
        model = Product
        fields = [
            'public',
            'owner',
            'id',
            'pk',
            'title',
            # 'content',
            'body',
            'price',
            'sale_price',
            'created_at',
            'updated_at',
            'url',
            'edit_url',
            'path',
            'endpoint',
            # 'email',
            # 'my_user_data',
            # 'user',
            # 'my_discount',
            # 'name',
            # 'related_products',
        ]

    # def get_my_user_data(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return {"username": obj.user.username}

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     # instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        # return f"/api/v2/products/{obj.pk}/"
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_url(self, obj):
    #     # return f"/api/v2/products/{obj.pk}/"
    #     request = self.context.get('request')  # self.request
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

#############################################################################################################################

###############################
    # def get_my_discount(self, obj):
    #     # print(obj.id)
    #     # obj.user —> user.username
    #     # obj.category -> |
    #     try:
    #         return obj.get_discount()
    #     except Exception as e:
    #         print(e)
###############################

#############################################################################################################################
