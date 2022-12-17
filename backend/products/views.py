from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication
from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

from .models import Product
from .serializers import ProductSerializer

###########################################


class ProductDetailAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view = False
    
    # lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission,]

###########################################


class ProductUpdateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [IsStaffEditorPermission]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission,]
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

###########################################


class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission,]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

###########################################


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print("#"*30)
        # print(serializer)
        # print("#"*30)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        # print("#"*30)
        serializer.save(content=content)
        # instance = serializer.save(content=content)
        # send a django signal

###########################################


class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    allow_staff_view = False
    
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication,]
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication,]

    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission,]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print("#"*30)
        # print(serializer)
        # print("#"*30)
        # print(serializer.validated_data)

        # email = serializer.validated_data.pop('email')

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        # print("#"*30)
        serializer.save(user=self.request.user, content=content)
        # instance = serializer.save(content=content)
        # send a django signal

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     # print(user)
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # return super().get_queryset(*args, **kwargs)
    #     return qs.filter(user=user)


###########################################


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

###########################################
# Mixins and a Generic API View


class ProductMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin,  mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView,):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, pk=None, *args, **kwargs):  # HTTP -> get
        print(args, kwargs, pk)
        # pk = kwargs.get("pk") # use this if not add pk in parameter
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # HTTP -> post
        if request.data or request.POST:
            return self.create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):

        # email = serializer.validated_data.pop('email')

        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):

        # instance = serializer.save()
        # if not instance.content:
        #     instance.content = instance.title

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_destroy(self, instance):
    #     super().perform_destroy(instance)


###########################################
# Using Function Based Views For Create Retrieve or List


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    method = request.method  # PUT —> update # DESTROY -> delete

    if method == "GET":
        if pk is not None:
            # # get request -—> detail view

            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404

            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
            # # list view
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)

###########################################
