from rest_framework import permissions
from rest_framework import generics
from .models import ShopProduct, ProfileOrder, ProfileOrderproduct, ShopImages, ProfileCustomer, ContactContact
from .models import ProfileAddress, ShopSubcategory
from .serializers import OrderSerializer, ProductSerializer, OrderDetailsSerializer, ProductImageSerializer
from .serializers import CustomerSerializer, ContactSerializer, AddressSerializer, SubCategorySerializer
from django.shortcuts import get_list_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView


class DocsView(APIView):
    """
    :synopsis: RESTFul Documentation de l'api (lien utilisable)
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        apidocs = {'product/': request.build_absolute_uri('product/'),
                   'update/product/<int:pk>': request.build_absolute_uri('update/product/<int:pk>'),
                   'order/': request.build_absolute_uri('order/'),
                   'update/order/<int:pk>': request.build_absolute_uri('update/order/<int:pk>'),
                   'order/details/<int:order__customer__id>/<int:order__id>':
                       request.build_absolute_uri('order/details/<int:order__customer__id>/<int:order__id>'),
                   'add/img/': request.build_absolute_uri('add/img/'),
                   'customer/': request.build_absolute_uri('customer/'),
                   'contact/': request.build_absolute_uri('contact/'),
                   'contact/<int:pk>': request.build_absolute_uri('contact/<int:pk>'),
                   'address/': request.build_absolute_uri('address/'),
                   'address/<int:customer>': request.build_absolute_uri('address/<int:customer>'),
                   'address/order/<int:customer>/<int:pk>':
                       request.build_absolute_uri('address/order/<int:customer>/<int:pk>'),
                   'subcategory/': request.build_absolute_uri('subcategory/'),
                   }
        return Response(apidocs)


class ProductList(generics.ListCreateAPIView):
    """:synopsis: Classe qui retourne la liste de tous les produits
        Methode disponible : GET ou POST
        """
    queryset = ShopProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """:synopsis: Classe qui retourne les information relatif a un produit ou de le supprimer
                  ou encore de modifier ses information (en fonction de sa pk)
       Methode disponible : GET, PUT, DELETE
       """
    queryset = ShopProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductImageList(generics.ListCreateAPIView):
    """:synopsis: Classe qui retourne la liste de toutes les images
       Methode disponible : GET ou POST
       """
    queryset = ShopImages.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderList(generics.ListAPIView):
    """:synopsis: Classe qui retourne la liste de toutes les commandes
       Methode disponible : GET
       """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = ProfileOrder.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = get_list_or_404(ProfileOrder, customer__id=customer_id)
        return queryset


class OrderUpdate(generics.RetrieveUpdateAPIView):
    """:synopsis: Classe qui retourne les information relatif a une commande ou de la supprimer
                  ou encore de modifier ses information (en fonction de sa pk)
       Methode disponible : GET, DELETE ou PUT
       """
    queryset = ProfileOrder.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetail(generics.ListAPIView):
    """:synopsis: Classe qui retourne les articles présent dans une commande grace a l'id du client et
                  l'id de la commande
           Methode disponible : GET
           """
    lookup_field = ('order__customer__id', 'order__id')
    serializer_class = OrderDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        order = self.kwargs['order__id']
        customer = self.kwargs['order__customer__id']
        return get_list_or_404(ProfileOrderproduct, order__customer__id=customer, order__id=order)


class CustomerList(generics.ListAPIView):
    """:synopsis: Classe qui retourne la liste de tous utilisateur qui sont des clients
       Methode disponible : GET
       """
    queryset = ProfileCustomer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactList(generics.ListAPIView):
    """:synopsis: Classe qui retourne la liste de toutes les demande de contact recu
       Methode disponible : GET
       """
    queryset = ContactContact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDelete(generics.RetrieveDestroyAPIView):
    """:synopsis: Classe qui permet de supprimer une demande de contact grace a sa pk
       Methode disponible : GET ou DELETE
       """
    queryset = ContactContact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressList(generics.ListAPIView):
    """:synopsis: Classe qui retourne toutes les adresse enregistrer accepte le parametre ?customer=id_customer qui
                  permet d'afficher les adresse concernant un client précis
       Methode disponible : GET
       """
    queryset = ProfileAddress.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = ProfileAddress.objects.all()
        customer = self.request.query_params.get('customer', None)
        if customer is not None:
            queryset = get_list_or_404(ProfileAddress, customer__id=customer)
        return queryset


class AddressOrderDetails(generics.ListAPIView):
    """:synopsis: Classe qui retourne l'addresse correspondante a une commande (param : /idCustomer/idOrder)
       Methode disponible : GET
       """
    lookup_field = ('customer', 'pk')
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer = self.kwargs['customer']
        pk = self.kwargs['pk']
        return get_list_or_404(ProfileAddress, customer=customer, profileorder__pk=pk)


class AddressCustomerDetails(generics.ListAPIView):
    """:synopsis: Classe qui retourne toutes les adresse enregistrer d'un client grace a sa pk
       Methode disponible : GET
       """
    lookup_field = 'customer'
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer = self.kwargs['customer']
        return get_list_or_404(ProfileAddress, customer=customer)


class SubCategoryList(generics.ListAPIView):
    """
       :synopsis: Classe qui retourne toutes les sous categorie
       Methode disponible : GET
       """

    queryset = ShopSubcategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
