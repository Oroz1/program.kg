# Generated by Django 3.2.12 on 2022-02-25 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Полное имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Элетронная почта')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Подтверждение')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Статус администратора')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Атрибут',
                'verbose_name_plural': 'Атрибуты',
            },
        ),
        migrations.CreateModel(
            name='AttributesTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Название атрибута',
                'verbose_name_plural': 'Название атрибутов',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание о категории')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categories', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название страны')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='DeliveriesStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Статус доставки',
                'verbose_name_plural': 'Статусы доставок',
            },
        ),
        migrations.CreateModel(
            name='DeliveriesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Наименование доставки',
                'verbose_name_plural': 'Наименовании доставок',
            },
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Название скидки')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цифра в скидках')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='MakerOfProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('logo', models.ImageField(upload_to='makers/images/', verbose_name='Логотип')),
                ('title', models.CharField(max_length=255, verbose_name='Название компании производителей')),
                ('description', models.TextField(verbose_name='Описание компании')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.countries', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Призводитель',
                'verbose_name_plural': 'Призводители',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('full_name', models.CharField(max_length=400, verbose_name='ФИО')),
                ('phone_1', models.CharField(max_length=15, verbose_name='Первый номер телефона')),
                ('phone_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Второй номер телефона')),
                ('address', models.CharField(max_length=400, verbose_name='Адрес')),
                ('information', models.TextField(verbose_name='Дополнительная информация')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Общая сумма заказа без скидок')),
                ('total_price_discount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Общая сумма заказа с учетом скидок')),
                ('delivery_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.deliveriestype', verbose_name='Способ доставки')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.deliveriesstatus', verbose_name='Статус доставки')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Имя товара')),
                ('short_description', models.TextField(verbose_name='краткое описание товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Себестоимость')),
                ('markup', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Надбавка')),
                ('sale_price_no_taxes', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Продажная цена без НДС')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Вычисляется с учетом налога')),
                ('attributes', models.ManyToManyField(to='core.Attributes', verbose_name='Атрибуты')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('image', models.ImageField(upload_to='products/images/', verbose_name='Картина')),
            ],
            options={
                'verbose_name': 'Картина товара',
                'verbose_name_plural': 'Картины товаров',
            },
        ),
        migrations.CreateModel(
            name='RateTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='UsersStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование статуа')),
            ],
            options={
                'verbose_name': 'Статус пользователя',
                'verbose_name_plural': 'Статусы пользователей',
            },
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Название налога')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Значение налога')),
                ('rate_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.ratetypes', verbose_name='Тип значение налога')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.CreateModel(
            name='ProductsDiscounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('description', models.TextField(verbose_name='Описание скидки')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Начало скидки')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Конец скидки')),
                ('discount_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.discounts', verbose_name='свойство cкидка')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Товар со скидкой',
                'verbose_name_plural': 'Товары со скидками',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(related_name='productsImages', to='core.ProductsImages', verbose_name='Картины товаров'),
        ),
        migrations.AddField(
            model_name='products',
            name='main_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.productsimages', verbose_name='Главная картина'),
        ),
        migrations.AddField(
            model_name='products',
            name='maker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.makerofproducts', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='products',
            name='markup_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.ratetypes', verbose_name='Тип надбавки'),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('content', models.TextField(verbose_name='Контент поста')),
                ('published', models.BooleanField(default=False, verbose_name='Статус видимости')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('content', models.TextField(verbose_name='Контент страницы')),
                ('published', models.BooleanField(default=False, verbose_name='Статус видимости')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='OrdersDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('discount_sum', models.PositiveIntegerField(verbose_name='сумма скидки в цифрах')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='цена товара')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество товара')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Общая сумма без учета скидки')),
                ('total_price_discount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name=' сумма с учетом скидок')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.orders', verbose_name='Заказ')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Список заказа',
                'verbose_name_plural': 'Списки заказов',
            },
        ),
        migrations.AddField(
            model_name='discounts',
            name='rate_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.ratetypes', verbose_name='Тип значение скидки'),
        ),
        migrations.AddField(
            model_name='attributes',
            name='attribute_title_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.attributestitles', verbose_name='Название аттрибута'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ManyToManyField(to='core.UsersStatus', verbose_name='Статус(ы) пользователя'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]