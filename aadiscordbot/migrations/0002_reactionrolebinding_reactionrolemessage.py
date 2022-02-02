# Generated by Django 3.2.5 on 2021-08-01 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('aadiscordbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionRoleMessage',
            fields=[
                ('message', models.BigIntegerField(
                    primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('manage_reactions', 'Can Manage Reaction Roles'),),
            },
        ),
        migrations.CreateModel(
            name='ReactionRoleBinding',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(max_length=100)),
                ('emoji_text', models.CharField(max_length=100)),
                ('group', models.ForeignKey(default=None, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('message', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='aadiscordbot.reactionrolemessage')),
            ],
        ),
    ]
