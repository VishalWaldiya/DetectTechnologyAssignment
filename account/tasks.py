from background_task import background
from account.models import EmployeeDetail
from django.db import IntegrityError
import json

@background(schedule=3600)
def load_fixture():
    with open('/home/vishal/Documents/Detect Technology/Assignment/test.json','r') as employeefile:
        data = json.loads(employeefile.read())

        for record in data:
            try:
                emp = EmployeeDetail(**record['fields'])
                emp.save()
            except IntegrityError:
                print("Record {} exists ".format(record['fields']['name']))
                continue
                # self.stdout.write(self.style.WARNING('Record "%s" Already Exists' %record['fields']['name']))