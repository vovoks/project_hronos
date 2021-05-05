import hashlib
import json

from django.core.management.base import BaseCommand, CommandError
from os import listdir
from os.path import isfile, join
from ...models import FileUpload
from ...parser import parse_schedule


class Command(BaseCommand):
    help = 'Загружает файлы расписания в формате json из ../schedules'

    def handle(self, *args, **options):
        base_path = join("../", "schedules")
        file_list = [f for f in listdir(base_path) if isfile(join(base_path, f)) and ".json" in f]

        hash_list = []

        for f in file_list:
            hash_md5 = hashlib.md5()
            with open(join(base_path, f), "rb") as json_file:
                for chunk in iter(lambda: json_file.read(4096), b""):
                    hash_md5.update(chunk)
                    hash_list.append((f, hash_md5.hexdigest()))

        obj = FileUpload.objects.filter(file_hash__in=[x[1] for x in hash_list])

        for item in obj:
            hash_list.remove((item.file_name, item.file_hash))

        for f in hash_list:
            with open(join(base_path, f[0]), "r+") as json_file:
                success, error = parse_schedule(json_file.read())

                if success:
                    obj = FileUpload.objects.create(file_name=f[0], file_hash=f[1])
                    obj.save()

                    for s in success:
                        self.stdout.write(self.style.SUCCESS(s))

                if error:
                    for s in error:
                        self.stdout.write(self.style.ERROR(s))
