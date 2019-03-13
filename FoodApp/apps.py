from django.apps import AppConfig
class FoodappConfig(AppConfig):
    name = 'FoodApp'

from suit.apps import DjangoSuitConfig
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'