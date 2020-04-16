# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    """:synopsis: Classe qui permet de creer la table AuthGroup dans la base de donnees
                 """
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    """:synopsis: Classe qui permet de creer la table AuthGroupPermissions dans la base de donnees
                 """
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    """:synopsis: Classe qui permet de creer la table AuthPermission dans la base de donnees
                 """
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    """:synopsis: Classe qui permet de creer la table AuthUser dans la base de donnees
                 """
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    """:synopsis: Classe qui permet de creer la table AuthUserGroups dans la base de donnees
                 """
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    """:synopsis: Classe qui permet de creer la table AuthUserUserPermissions dans la base de donnees
                 """
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ContactContact(models.Model):
    """:synopsis: Classe qui permet de creer la table ContactContact dans la base de donnees
                 """
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    message = models.TextField()
    date = models.DateTimeField()
    subject = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'contact_contact'


class DjangoAdminLog(models.Model):
    """:synopsis: Classe qui permet de creer la table DjangoAdminLog dans la base de donnees
                 """
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    """:synopsis: Classe qui permet de creer la table DjangoContentType dans la base de donnees
                 """
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    """:synopsis: Classe qui permet de creer la table DjangoMigrations dans la base de donnees
                 """
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    """:synopsis: Classe qui permet de creer la table DjangoSession dans la base de donnees
                 """
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProfileAddress(models.Model):
    """:synopsis: Classe qui permet de creer la table ProfileAddress dans la base de donnees
                 """
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    address = models.TextField()
    city = models.CharField(max_length=50)
    cp = models.CharField(max_length=5, blank=True, null=True)
    country = models.CharField(max_length=30)
    mobile = models.CharField(max_length=128, blank=True, null=True)
    customer = models.ForeignKey('ProfileCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_address'


class ProfileBasket(models.Model):
    """:synopsis: Classe qui permet de creer la table ProfileBasket dans la base de donnees
                 """
    quantity = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
    customer = models.ForeignKey('ProfileCustomer', models.DO_NOTHING)
    product = models.ForeignKey('ShopProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_basket'


class ProfileCustomer(models.Model):
    """:synopsis: Classe qui permet de creer la table ProfileCustomer dans la base de donnees
                 """
    mobile = models.CharField(max_length=128)
    gender = models.CharField(max_length=1)
    isnewsletter = models.BooleanField(db_column='IsNewsletter')  # Field name made lowercase.
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_customer'


class ProfileOrder(models.Model):
    """:synopsis: Classe qui permet de creer la table ProfileOrder dans la base de donnees
                 """
    status = models.CharField(max_length=50)
    delivery = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField()
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    methodpayment = models.CharField(db_column='methodPayment', max_length=15)  # Field name made lowercase.
    address = models.ForeignKey(ProfileAddress, models.DO_NOTHING)
    customer = models.ForeignKey(ProfileCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_order'


class ProfileOrderproduct(models.Model):
    """:synopsis: Classe qui permet de creer la table ProfileOrderproduct dans la base de donnees
                 """
    quantity = models.PositiveSmallIntegerField()
    order = models.ForeignKey(ProfileOrder, models.DO_NOTHING)
    product = models.ForeignKey('ShopProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_orderproduct'


class ShopCategory(models.Model):
    """:synopsis: Classe qui permet de creer la table ShopCategory dans la base de donnees
                 """
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'shop_category'


class ShopImages(models.Model):
    """:synopsis: Classe qui permet de creer la table ShopImages dans la base de donnees
                 """

    image = models.FileField(upload_to='upload/%Y/%m/%d')
    date = models.DateTimeField()
    product = models.ForeignKey('ShopProduct', models.DO_NOTHING)
    title = models.CharField(max_length=124, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_images'


class ShopNewsletter(models.Model):
    """:synopsis: Classe qui permet de creer la table ShopNewsletter dans la base de donnees
                 """
    email = models.CharField(max_length=254)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shop_newsletter'


class ShopProduct(models.Model):
    """:synopsis: Classe qui permet de creer la table ShopProduct dans la base de donnees
                 """
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    category = models.ForeignKey('ShopSubcategory', models.DO_NOTHING)
    image = models.FileField(upload_to='upload/%Y/%m/%d', blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'shop_product'


class ShopProductcomment(models.Model):
    """:synopsis: Classe qui permet de creer la table ShopProductcomment dans la base de donnees
                 """
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    comment = models.TextField()
    date = models.DateTimeField()
    product = models.ForeignKey(ShopProduct, models.DO_NOTHING)
    star = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'shop_productcomment'


class ShopSubcategory(models.Model):
    """:synopsis: Classe qui permet de creer la table ShopSubcategory dans la base de donnees
                 """
    name = models.CharField(max_length=30)
    category = models.ForeignKey(ShopCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_subcategory'
