# Generated by Django 5.0.6 on 2024-07-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_views_counter_alter_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                ("slug", models.SlugField(blank=True, unique=True)),
                (
                    "content",
                    models.CharField(
                        help_text="Введите текст",
                        max_length=1000,
                        verbose_name="Содержимое",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото",
                        null=True,
                        upload_to="BlogPost/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "view_count",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите кол-во просмотров",
                        verbose_name="Счетчик просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог-пост",
                "verbose_name_plural": "Блог-посты",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="views_counter",
        ),
    ]
