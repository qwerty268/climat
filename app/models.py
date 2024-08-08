from django.db import models


class ParametrT(models.Model):
    data_time = models.DateTimeField(db_column='Data_Time', blank=True, null=True)  # Field name made lowercase.
    num_sens = models.CharField(db_column='Num_Sens', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField()
    vlagnost = models.FloatField(db_column='Vlagnost', blank=True, null=True)  # Field name made lowercase.
    tochka_rosa = models.FloatField(db_column='Tochka_Rosa', blank=True, null=True)  # Field name made lowercase.
    status_sens = models.CharField(db_column='Status_sens', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametr_t'
