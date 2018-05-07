from django.db import models


class AME(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255)
    ame = models.FloatField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = (('age', 'gender'),)


class Answer(models.Model):
    instace_id = models.UUIDField(primary_key=True)
    dataset_id = models.BigIntegerField()
    dataset_name = models.TextField(blank=True, null=True)
    dataset_owner = models.TextField(blank=True, null=True)
    dataset_year = models.FloatField(blank=True, null=True)
    row_id = models.BigIntegerField()
    landscape = models.CharField(max_length=255, blank=True, null=True)
    surveyor = models.CharField(max_length=255, blank=True, null=True)
    participant = models.CharField(max_length=255, blank=True, null=True)
    arrival = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    hh_type_control = models.NullBooleanField()
    hh_type_org_benef = models.NullBooleanField()
    hh_type_other_benef = models.NullBooleanField()
    hh_id = models.CharField(max_length=255, blank=True, null=True)
    livelihood_1 = models.CharField(max_length=255, blank=True, null=True)
    livelihood_2 = models.CharField(max_length=255, blank=True, null=True)
    livelihood_3 = models.CharField(max_length=255, blank=True, null=True)
    livelihood_4 = models.CharField(max_length=255, blank=True, null=True)
    benef_project = models.NullBooleanField()
    explain_project = models.CharField(max_length=255, blank=True, null=True)
    know_pa = models.NullBooleanField()
    benef_pa = models.NullBooleanField()
    explain_benef_pa = models.CharField(max_length=255, blank=True, null=True)
    bns_plus = models.CharField(max_length=255, blank=True, null=True)
    survey_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = (('dataset_id', 'row_id'),)


class AnswerGPS(models.Model):
    answer = models.OneToOneField(
        Answer,
        on_delete=models.CASCADE,
    )
    instace_id = models.UUIDField(primary_key=True)
    lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    long = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # TODO: Add support for geodata


class AnswerGS(models.Model):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
    )
    gs = models.TextField()
    necessary = models.NullBooleanField()
    have = models.NullBooleanField()
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)


class AnswerHHMembers(models.Model):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
    )
    gender = models.TextField(blank=True, null=True)
    birth = models.IntegerField(blank=True, null=True)
    ethnicity = models.TextField(blank=True, null=True)
    head = models.NullBooleanField()


class AnswerNR(models.Model):
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
    )
    nr = models.TextField()
    nr_collect = models.IntegerField(blank=True, null=True)