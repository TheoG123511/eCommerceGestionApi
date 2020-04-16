from rest_framework import serializers
from .models import ShopProduct, ProfileOrder, ProfileOrderproduct, ShopImages, ProfileCustomer, ContactContact
from .models import ProfileAddress, ShopSubcategory


class OrderSerializer(serializers.ModelSerializer):
    """
        :synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model ProfileOrder
    """
    class Meta:
        model = ProfileOrder
        fields = ['id', 'customer', 'address', 'status', 'delivery', 'date', 'methodpayment']

    def create(self, validated_data):
        """
        :synopsis: Creer une nouvelle entrer dans la base de donnees et retourne le resultat
        """
        return ProfileOrder.objects.create(**validated_data)


class OrderDetailsSerializer(serializers.ModelSerializer):
    """
        :synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model OrderDetailsSerializer
    """
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = ProfileOrderproduct
        fields = ['id', 'quantity', 'order', 'product', 'product_name', 'product_price']


class ProductSerializer(serializers.ModelSerializer):
    """
    :synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model ProductSerializer
    """
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = ShopProduct
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image', 'category_name', 'date', 'category']

    def create(self, validated_data):
        """
        :synopsis: Creer une nouvelle entrer dans la base de donnees et retourne le resultat
        """
        return ShopProduct.objects.create(**validated_data)


class ProductImageSerializer(serializers.ModelSerializer):
    """
    :synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model ProductImageSerializer
    """
    class Meta:
        model = ShopImages
        fields = ['id', 'image', 'date', 'product', 'title']


class CustomerSerializer(serializers.ModelSerializer):
    """:synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model CustomerSerializer"""
    first_name = serializers.ReadOnlyField(source='user.first_name')
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    date_joined = serializers.ReadOnlyField(source='user.date_joined')
    last_login = serializers.ReadOnlyField(source='user.last_login')

    class Meta:
        model = ProfileCustomer
        fields = ['id', 'mobile', 'gender', 'isnewsletter', 'user', 'first_name', 'username', 'email', 'last_name',
                  'date_joined', 'last_login']


class ContactSerializer(serializers.ModelSerializer):
    """:synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model ContactSerializer"""
    class Meta:
        model = ContactContact
        fields = ['nom', 'email', 'message', 'date', 'subject', 'id']


class AddressSerializer(serializers.ModelSerializer):
    """:synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model AddressSerializer"""
    class Meta:
        model = ProfileAddress
        fields = ['id', 'firstname', 'lastname', 'address', 'city', 'cp', 'country', 'mobile', 'customer']


class SubCategorySerializer(serializers.ModelSerializer):
    """:synopsis: Classe qui permet de serializer et déserialisez des donnes provenant du model SubCategorySerializer"""
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = ShopSubcategory
        fields = ['id', 'name', 'category_name', 'category']
