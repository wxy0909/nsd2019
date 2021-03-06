from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)

    def __str__(self):
        return "%s=>%s:%s" % (self.group, self.hostname, self.ipaddr)

class Module(models.Model):
    modluename = models.CharField(max_length=50)

    def __str__(self):
        return self.modluename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200)
    module = models.ForeignKey(Module)

    def __str__(self):
        return "%s=>%s" % (self.module, self.arg_text)
