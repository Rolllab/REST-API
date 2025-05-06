# ------------------------------------- Command create users ----------------------------------------------------
import os
from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User, UserRoles


load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        admin = User.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
            first_name=os.getenv('ADMIN_FIRST_NAME'),
            last_name=os.getenv('ADMIN_LAST_NAME'),
            role=UserRoles.MODERATOR,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        admin.set_password(os.getenv('ADMIN_PASSWORD'))
        admin.save()
        print("Администратор создан!!!")

        moderator = User.objects.create(
            email=os.getenv('MODERATOR_EMAIL'),
            first_name=os.getenv('MODERATOR_FIRST_NAME'),
            last_name=os.getenv('MODERATOR_LAST_NAME'),
            role=UserRoles.MODERATOR,
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )

        moderator.set_password(os.getenv('MODERATOR_PASSWORD'))
        moderator.save()
        print("Модератор создан!!!")

        member = User.objects.create(
            email=os.getenv('USER_EMAIL'),
            first_name=os.getenv('USER_FIRST_NAME'),
            last_name=os.getenv('USER_LAST_NAME'),
            role=UserRoles.MEMBER,
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        member.set_password(os.getenv('USER_PASSWORD'))
        member.save()
        print("Создан новый пользователь!!!")