from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from faker.providers import BaseProvider
import numpy as np
from profile_api_app.models import Student, Achievement, Profile
from django.contrib.auth.models import User


# np.round takes second arg - 1 for decimal places
# np.arange increments by .1 starting from 0 and ending at 4.0 given that the last number should be the final increment (4.1 does not appear)
GPA = [np.round(grade, 2) for grade in np.arange(0, 4.1, 0.1)]
NUMBER_OF_USERS = [num for num in range(1,Profile.objects.all().count()+1)]


class Provider(BaseProvider):
    def gpa_selection(self):
        return self.random_element(GPA)

    def random_user(self):
        return self.random_element(NUMBER_OF_USERS)


class Command(BaseCommand):
    help = 'Generate Fake Data'

    def add_arguments(self, parser):
        # If we have nargs as ? or * and not + then default value will be used if none was given
        # We also provided the default value as non for our handle to check
        parser.add_argument('model', nargs='?', type=str, default=None)
        parser.add_argument('custom_user_id', nargs='?', type=int, default=None)

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)

        # We use **kwargs  to access our argument
        # This way we could add a specific user or a random user
        if kwargs['model'][:3].lower() == 'ach':
            print('achievement')
            # Achievement Model
            if kwargs['custom_user_id']:
                # We are going to inject fake data for only one user specified by the custom_user_id
                try:
                    profile = Profile.objects.get(kwargs['custom_user_id'])
                    user = profile.user
                    achievement_creation = Achievement.objects.create(
                        user= user,
                        user_profile= profile,
                        achievement_response= fake.paragraph(nb_sentences=10)
                    )

                    print(achievement_creation)
                except Exception:
                    print('User does not exist')
            else:
                # We are going to inject data for all users
                for user_id in NUMBER_OF_USERS:
                    profile = Profile.objects.get(id=user_id)
                    user = profile.user
                    achievement_creation = Achievement.objects.create(user=user, user_profile=profile,
                                                                      achievement_response= fake.paragraph(nb_sentences=10))
                    print(achievement_creation)
        elif kwargs['model'][:3].lower() == 'stu':
            print('student')
            # Student model
            if kwargs['custom_user_id']:
                # We are going to inject fake data for only one user specified by the custom_user_id
                try:
                    profile = Profile.objects.get(kwargs['custom_user_id'])
                    user = profile.user
                    student_creation = Student.objects.create(user=user, user_profile=profile,
                                                              overall_gpa=fake.gpa_selection(), activity_title=fake.job(),
                                                              activity_details=fake.paragraph(nb_sentences=5)
                                                                )
                    print(student_creation)
                except Exception:
                    print('User does not exist')
            else:
                # We are going to inject data for all users
                for students in NUMBER_OF_USERS:
                    profile = Profile.objects.get(id=students)
                    user = profile.user
                    student_creation = Student.objects.create(user=user, user_profile=profile,
                                                              overall_gpa=fake.gpa_selection(), activity_title=fake.job(),
                                                              activity_details=fake.paragraph(nb_sentences=5)
                                                                )
                    print(student_creation)
        else:
            print('Please indicate which model you would like to add data to')