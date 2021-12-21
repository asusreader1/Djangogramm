# Generated by Django 4.0 on 2021-12-19 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('followers', models.ManyToManyField(db_table='web_followers', related_name='follow_by', to='web.User')),
                ('follows', models.ManyToManyField(db_table='web_follows', related_name='followed_by', to='web.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('media', models.ImageField(blank=True, null=True, upload_to='')),
                ('pub_date', models.DateTimeField()),
                ('likes', models.ManyToManyField(db_table='web_post_like_user', related_name='posts_likes', to='web.User')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dialog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.dialog')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='input_messages', to='web.user')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to='web.user')),
            ],
        ),
        migrations.AddField(
            model_name='dialog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.user'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('likes', models.ManyToManyField(db_table='web_comment_like_user', related_name='comments_likes', to='web.User')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.user')),
            ],
        ),
    ]