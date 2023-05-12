<<<<<<< HEAD
# Generated by Django 4.2.1 on 2023-05-12 08:49
=======
# Generated by Django 4.2.1 on 2023-05-11 05:49
>>>>>>> upstream/main

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('is_free', models.BooleanField(default=False, verbose_name='무료나눔')),
                ('bargain', models.BooleanField(default=False, verbose_name='가격제안 여부')),
                ('place', models.TextField(blank=True, verbose_name='장소')),
                ('views', models.IntegerField(default=0, verbose_name='조회수')),
                ('transaction_status', models.IntegerField(default=0, verbose_name='거래상태')),
                ('refreshed_at', models.DateTimeField(null=True, verbose_name='끌어올리기')),
                ('is_hide', models.BooleanField(default=False, verbose_name='숨기기')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('bookmark', models.ManyToManyField(blank=True, related_name='bookmark_product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='분류')),
                ('is_used', models.BooleanField(default=True, verbose_name='True=사용, False=사용안함')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='%Y/%m/', verbose_name='이미지')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
