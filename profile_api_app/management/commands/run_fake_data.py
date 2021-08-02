from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from faker.providers import BaseProvider
import numpy as np
from profile_api_app.models import Student, Achievement


# np.round takes second arg - 1 for decimal places
# np.arange increments by .1 starting from 0 and ending at 4.0 given that the last number should be the final increment (4.1 does not appear)
GPA = [np.round(grade, 2) for grade in np.arange(0, 4.1, 0.1)]


class Provider(BaseProvider):
    def gpa_selection(self):
        return self.random_element(GPA)


class Command(BaseCommand):
    help = 'Generate Fake Data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)
        print(fake.gpa_selection())
        Student.objects.create()