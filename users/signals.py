from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

        subject = 'Добро пожаловать в библиотеку!'
        greeting = f'Здравствуйте {profile.username}, '
        msg1 = 'Ваш аккаунт успешно создан!\n'
        msg2 = 'Вы можете приступить к каталогизации вашей библиотеки.'
        message = f'{greeting}{msg1}{msg2}'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )
