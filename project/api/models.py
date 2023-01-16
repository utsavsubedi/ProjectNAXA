from django.db import models

# Create your models here.
PROJECT_STATUS_CHOICE = (
    ('O', 'On-Going'),
    ('C', 'Completed')
)

BUDGET_TYPE = (
    ('OFF', 'Off Budget'),
    ('ON', 'On Budget')
)

class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_status = models.CharField(max_length=20, choices=PROJECT_STATUS_CHOICE, default='O')
    donor = models.CharField(max_length=100)
    executing_agency = models.CharField(max_length=100)
    implementing_partner = models.CharField(max_length=100)
    counterpart_agency = models.CharField(max_length=100)
    humanitarian = models.BooleanField(default=False)
    assistance_code = models.IntegerField()
    agremeent_date = models.DateField()
    effective_date = models.DateField()
    sector = models.CharField(max_length=50, blank=True, null=True)
    sector_code = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


    class Meta:
        unique_together = ( 'project_title', 'effective_date')

    def __str__(self):
        return f'{self.project_title}'

class Budget(models.Model):
    budget_type = models.CharField(max_length=20, choices=BUDGET_TYPE, default='ON' )
    commitments = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.budget_type} - {self.commitments}'


class Address(models.Model):
    province = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    municipality = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('province', 'district', 'municipality', 'project', 'budget')

    def __str__(self):
        return f'{self.province} - {self.district} - {self.municipality}'