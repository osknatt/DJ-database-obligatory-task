import csv
import datetime


from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # print(line)
                # TODO: Добавьте сохранение модели
                phone = Phone(
                    name=line[1],
                    price=line[3],
                    image=line[2],
                    release_date=datetime.datetime.strptime(line[4], '%Y-%m-%d'),
                    lte_exists=line[5],
                    slug=slugify(line[1])
                )
                phone.save()
