# Generated by Django 4.1 on 2022-11-27 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="collection_post",
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
                    "user_id",
                    models.CharField(default="", max_length=30, verbose_name="用户id"),
                ),
                ("file_id", models.CharField(max_length=30, verbose_name="收藏文件id")),
            ],
        ),
        migrations.CreateModel(
            name="DownloadFile_post",
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
                    "user_id",
                    models.CharField(default="", max_length=30, verbose_name="用户id"),
                ),
                ("file_id", models.CharField(max_length=30, verbose_name="下载文件id")),
            ],
        ),
        migrations.CreateModel(
            name="user",
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
                ("nickname", models.CharField(max_length=30, verbose_name="昵称")),
                (
                    "gender",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="性别"
                    ),
                ),
                ("openid", models.CharField(max_length=30, verbose_name="openid")),
            ],
        ),
        migrations.CreateModel(
            name="dashboard",
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
                    "collection_num",
                    models.PositiveIntegerField(default=0, verbose_name="收藏数"),
                ),
                (
                    "UploadFile_num",
                    models.PositiveIntegerField(default=0, verbose_name="上传文件数"),
                ),
                (
                    "DownloadFile_num",
                    models.PositiveIntegerField(default=0, verbose_name="下载文件数"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="User.user",
                        verbose_name="对应用户id",
                    ),
                ),
            ],
        ),
    ]