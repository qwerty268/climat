from django.db import models


class ParametrT(models.Model):
    data_time = models.DateTimeField(db_column='Data_Time', blank=True, null=True)  # Field name made lowercase.
    num_sens = models.CharField(db_column='Num_Sens', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    vlagnost = models.FloatField(db_column='Vlagnost', blank=True, null=True)  # Field name made lowercase.
    tochka_rosa = models.FloatField(db_column='Tochka_Rosa', blank=True, null=True)  # Field name made lowercase.
    status_sens = models.CharField(db_column='Status_sens', max_length=1, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Parametr_T'