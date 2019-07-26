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

class Alerts(models.Model):
    alertid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, db_column='actionid')
    eventid = models.ForeignKey('Events', db_column='eventid')
    userid = models.ForeignKey('Users', db_column='userid', blank=True, null=True)
    clock = models.IntegerField()
    mediatypeid = models.ForeignKey('MediaType', db_column='mediatypeid', blank=True, null=True)
    sendto = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.IntegerField()
    retries = models.IntegerField()
    error = models.CharField(max_length=128)
    esc_step = models.IntegerField()
    alerttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alerts'


class ApplicationTemplate(models.Model):
    application_templateid = models.BigIntegerField(primary_key=True)
    applicationid = models.ForeignKey('Applications', db_column='applicationid')
    templateid = models.ForeignKey('Applications', db_column='templateid')

    class Meta:
        managed = False
        db_table = 'application_template'


class Applications(models.Model):
    applicationid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', db_column='hostid')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'applications'


class Auditlog(models.Model):
    auditid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid')
    clock = models.IntegerField()
    action = models.IntegerField()
    resourcetype = models.IntegerField()
    details = models.CharField(max_length=128)
    ip = models.CharField(max_length=39)
    resourceid = models.BigIntegerField()
    resourcename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auditlog'