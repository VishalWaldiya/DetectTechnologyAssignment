from django.contrib import admin
from account.models import EmployeeDetail

def changeDesignation_SeniorDeveloper(modeladmin, request, querysets):
    querysets.update(designation='Senior Developer')

def changeDesignation_Developer(modeladmin, request, querysets):
    querysets.update(designation='Developer')

def changeDesignation_HiringManager(modeladmin, request, querysets):
    querysets.update(designation='Hiring Manager')

def changeDesignation_Manager(modeladmin, request, querysets):
    querysets.update(designation='Manager')

def changeAdress_Chennai(modeladmin, request, querysets):
    querysets.update(address='Chennai')

def changeAdress_Coimbatore(modeladmin, request, querysets):
    querysets.update(address='Coimbatore')

def changeAdress_Hydrebad(modeladmin, request, querysets):
    querysets.update(address='Hydrebad')

def changeAdress_Bangalore(modeladmin, request, querysets):
    querysets.update(address='Bangalore')

changeDesignation_SeniorDeveloper.short_description = "Change Designation to 'Senior Developer'"
changeDesignation_Developer.short_description = "Change Designation to 'Developer'"
changeDesignation_HiringManager.short_description = "Change Designation to 'Hiring Manager'"
changeDesignation_Manager.short_description = "Change Designation to 'Manager'"
changeAdress_Chennai.short_description = "Change Address to 'Chennai'"
changeAdress_Coimbatore.short_description = "Change Address to 'Coimbatore'"
changeAdress_Hydrebad.short_description = "Change Address to 'Hydrebad'"
changeAdress_Bangalore.short_description = "Change Address to 'Bangalore'"


class EmployeeDetailAdmin(admin.ModelAdmin):
    search_fields = ['employeeId','designation','date_of_joining','name','address','phone_number','email']
    list_display = ['employeeId','designation','date_of_joining','name','address','phone_number','email']
    actions = [changeDesignation_SeniorDeveloper,changeDesignation_Developer,
changeDesignation_HiringManager,
changeDesignation_Manager,
changeAdress_Chennai,
changeAdress_Coimbatore,
changeAdress_Hydrebad,
changeAdress_Bangalore,]

admin.site.register(EmployeeDetail,EmployeeDetailAdmin)