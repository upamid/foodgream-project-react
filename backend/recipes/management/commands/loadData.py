import json
import os

from django.conf import settings
from django.core.management import BaseCommand
from django.core import management
from django.core.management.commands import loaddata

from recipes.models import Ingredient

fixture_dir = ''
fixture_filename = 'ingredients.json'


class Command(BaseCommand):
    help = "load data"
    fixture_filename = 'ingerdients.json'
        
    def handle(self, *args, **options):
        fixture_file = os.path.join(fixture_dir, fixture_filename)
        print(fixture_file)
        f = open(fixture_file,)
        my_json_obj = json.load(f)
        for title in my_json_obj:
            Ingredient.objects.create(name=title['name'], measurement_unit=title['measurement_unit'])
        # management.call_command('loaddata', fixture_file)
