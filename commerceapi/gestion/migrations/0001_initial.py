# Generated by Django 3.0.4 on 2020-03-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
                ('subject', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contact_contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_column='firstName', max_length=50)),
                ('lastname', models.CharField(db_column='lastName', max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('cp', models.CharField(blank=True, max_length=5, null=True)),
                ('country', models.CharField(max_length=30)),
                ('mobile', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'profile_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'profile_basket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=1)),
                ('isnewsletter', models.BooleanField(db_column='IsNewsletter')),
            ],
            options={
                'db_table': 'profile_customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('delivery', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField()),
                ('enddate', models.DateTimeField(blank=True, db_column='endDate', null=True)),
                ('methodpayment', models.CharField(db_column='methodPayment', max_length=15)),
            ],
            options={
                'db_table': 'profile_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileOrderproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'profile_orderproduct',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'shop_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(blank=True, max_length=124, null=True)),
            ],
            options={
                'db_table': 'shop_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'shop_newsletter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'shop_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopProductcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('star', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'shop_productcomment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShopSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'shop_subcategory',
                'managed': False,
            },
        ),
    ]
