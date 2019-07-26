from django.db import models

# Create your models here.

class Actions(models.Model):
    actionid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    eventsource = models.IntegerField()
    evaltype = models.IntegerField()
    status = models.IntegerField()
    esc_period = models.IntegerField()
    def_shortdata = models.CharField(max_length=255)
    def_longdata = models.TextField()
    recovery_msg = models.IntegerField()
    r_shortdata = models.CharField(max_length=255)
    r_longdata = models.TextField()
    formula = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'actions'

