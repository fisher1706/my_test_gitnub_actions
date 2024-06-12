import string
import random
from data.testing_data import DEFAULT_EMAIL
from faker import Faker


class Utils:
    fake = Faker('ru_Ru')

    def random_phone(self, code="38", operator="063", is_correct=True):
        return f"+{code}{operator}{self.random_data(chars=string.digits)}" if is_correct else self.random_data()

    def random_email(self, is_correct=True):
        return f"{self.random_data(size=5)}+{DEFAULT_EMAIL}" if is_correct else self.random_data()

    def random_code(self, is_correct=True):
        return f"{self.random_data(size=4, chars=string.digits)}" if is_correct else self.random_data()

    @staticmethod
    def random_data(size=7, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def get_random_data_from_list(data: list):
        return random.choice(data)

    def user_profile(self):
        profile = {
            'name': self.fake.name(),
            'email': self.fake.email(),
            'phone': self.random_phone()
        }
        return profile


if __name__ == '__main__':
    u = Utils()
    p = u.user_profile()
    print(p)
