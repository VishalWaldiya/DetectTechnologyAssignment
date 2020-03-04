from django.core.management.base import BaseCommand, CommandError
from account.models import EmployeeDetail
import argparse,json
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Loads all data from mydata.json into DB'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))
        parser.add_argument('number_of_data', type=int)

    def handle(self, *args, **options):
        # for arg in options['file']:
        data = json.loads(options['file'].read())
        number_of_records_to_be_saved = options['number_of_data']

        for i in range(number_of_records_to_be_saved):
            try:
                record = data[i]
                emp = EmployeeDetail(**record['fields'])
                emp.save()
            except IntegrityError:
                print(record['fields']['name'])
                self.stdout.write(self.style.WARNING('Record "%s" Already Exists' %record['fields']['name']))

            except IndexError:
                self.stdout.write(self.style.ERROR('Insuffcient Records in Fixture'))
                break
        self.stdout.write(self.style.SUCCESS('All records already added'))
        # import pdb; pdb.set_trace()
        # self.stdout.write(self.style.SUCCESS('Successfully loaded employe details "%s"' % 10))
        # for poll_id in options['file']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))