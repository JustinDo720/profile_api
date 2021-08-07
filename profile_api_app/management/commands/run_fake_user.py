from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

USERNAMES = [
    'DarkenBlue',
    'DarkenMuffin',
    'DarkenSnow',
    'DarkenJacob',
    'DarkenLogan',
    'LightenBlue',
    'LightenMuffin',
    'LightenSnow',
    'LightenJacob',
    'LightenLogan',
    'DarkenJustin',
    'LightenJustin',
    'BlueBot',
    'NavyBot',
    'justi',

]

PASSWORD = 'testing123'


class Command(BaseCommand):
    help = 'Generate Users'

    def handle(self, *args, **kwargs):

        for name in USERNAMES:
            try:
                if name.lower() == 'justi':
                    print(f'Registered AUTH : {name}')
                    admin_user = User.objects.create_user(username=name, password=PASSWORD, is_staff=True, is_superuser=True)
                    print(admin_user)
                else:
                    print(f'Registered: {name}')
                    new_user = User.objects.create(username=name, password=PASSWORD)
                    print(new_user)
            except IntegrityError:
                continue
