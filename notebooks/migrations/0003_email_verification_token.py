from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import secrets


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0002_add_user_document'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerificationToken',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID',
                )),
                ('token', models.CharField(
                    default=secrets.token_urlsafe,
                    max_length=64,
                    unique=True,
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='email_verification',
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
        ),
    ]
