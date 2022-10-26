from django.db import models

class CSV_data(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File id - {self.pk}'


class ZVK_data(models.Model):
    self_number = models.IntegerField(verbose_name='№ свой')
    alien_number = models.IntegerField(verbose_name='№ чужой')
    zvk_giver = models.CharField(max_length=30, verbose_name='Предприятие')
    complex = models.CharField(max_length=50, verbose_name='Комплекс')
    empty_field = models.CharField(blank=True, null=True, max_length=3, verbose_name='empty_field')
    zvk_status = models.CharField(max_length=30, verbose_name='Состояние заявки')
    subject = models.CharField(max_length=50, verbose_name='Объект')
    equipment = models.CharField(max_length=50, verbose_name='Оборудование')
    equipment_detail = models.CharField(max_length=50, verbose_name='Оборудование, выводимое в ремонт')
    mode = models.CharField(max_length=30, verbose_name='Состояние оборудования по заявке')
    program = models.CharField(max_length=300, verbose_name='Программа переключений')
    use_in_mode = models.CharField(max_length=3, verbose_name='Актуализация')
    start_date = models.DateTimeField(blank=True, verbose_name='Разрешенное время - начало')
    end_date = models.DateTimeField(blank=True, verbose_name='Разрешенное время -  конец')
    asked_start_date = models.DateTimeField(blank=True, verbose_name='Просимое время - начало')
    repair_type = models.CharField(max_length=5, verbose_name='Ремонт')
    zvk_type = models.CharField(max_length=5, verbose_name='Категория')
    over_date = models.CharField(max_length=5, verbose_name='Просрочена')
    ag = models.CharField(max_length=5, verbose_name='А\Г')
    grounding = models.CharField(max_length=5, verbose_name='Заземление')
    conditions = models.CharField(max_length=5, verbose_name='Условия производства')

    def __str__(self):
        return f'{self.self_number} - {self.repair_type}'
