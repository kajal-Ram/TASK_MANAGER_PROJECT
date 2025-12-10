from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create user roles: Admin and User'

    def handle(self, *args, **options):
        for g in ['Admin', 'User']:
            group, created = Group.objects.get_or_create(name=g)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created group: {g}'))
            else:
                self.stdout.write(self.style.WARNING(f'Group already exists: {g}'))
