from rest_framework import serializers


# from django.contrib.auth import get_user_model
# User = get_user_model()

from django.contrib.auth.models import User
###########################################


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
# class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)
    this_is_not_real = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'this_is_not_real',
        ]

    # def get_other_products(self, obj):
    #     # print(obj) # user object
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data
