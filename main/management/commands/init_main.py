import json
import time
from os import listdir
from django.apps import apps
from os.path import join, isdir, isfile, splitext
from django.conf import settings
from django.core.management.base import BaseCommand


def seeder_factory(mdl, data, parent=None):
    for d in data:
        try:
            children = d.pop('children')
        except KeyError:
            children = None
        try:
            if parent is None:
                el, _ = mdl.objects.get_or_create(**d)
            else:
                el, _ = mdl.objects.get_or_create(**{**d, 'parent': parent})
        except Exception as ex:
            print(ex)
            continue

        if children is not None:
            seeder_factory(mdl, children, el)


class Command(BaseCommand):
    help = 'Развертование приложения main'
    seed_path = join(settings.BASE_DIR, 'D:\Distributiv\Project_RD\WebApp\main\management\seed')

    def handle(self, *args, **options):
        start_time = time.time()
        self.stdout.write('инициализация приложения main')
        app_dirs = [name for name in listdir(join(self.seed_path)) if isdir(join(self.seed_path, name))]
        app_dirs.sort()
        for app_name in app_dirs:
            self.stdout.write(f'    Приложение {app_name[4:]}')
            app_path = join(self.seed_path, app_name)
            mdls_name = [name for name in listdir(app_path) if isfile(join(app_path, name))]
            mdls_name.sort()
            for mdl_name in mdls_name:
                mdl_path = join(app_path, mdl_name)
                mdl, _ = splitext(mdl_name)
                self.stdout.write(f'        Модель {mdl}')
                model = apps.get_model(app_name[4:], mdl[4:])
                with open(mdl_path, encoding='utf-8') as file:
                    seeder_factory(model, json.load(file))
        self.stdout.write(f'Инициализация приложения main заверена за время: {str((time.time() - start_time) / 60)} минут')

