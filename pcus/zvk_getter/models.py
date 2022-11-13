from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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


class Station(models.Model):
    title = models.CharField(max_length=64, verbose_name='PPlant name')
    star = models.BooleanField(default=True)
    zvk_name = models.CharField(max_length=15, verbose_name='zvk_unit_name', default='NU')
    rating = models.SmallIntegerField(default=1, verbose_name='get_rating')

    def __str__(self):
        return f'{self.title} -- {self.rating}'

    def get_absolute_url(self):
        return reverse('gen_detail', kwargs={'station_id': self.pk})


class Block(models.Model):
    in_work = 'P'
    emergency_repair = 'AP'
    current_repair = 'KP'
    capital_repair = 'KP'
    mean_repair = 'CP'
    forced_downtime = 'Bp'
    main_condition_choices = {
        (in_work, 'in_work'),
        (emergency_repair, 'emergency_repair'),
        (current_repair, 'current_repair'),
        (capital_repair, 'capital_repair'),
        (mean_repair, 'mean_repair'),
        (forced_downtime, 'forced_downtime'),
    }
    title = models.CharField(max_length=64, verbose_name='Block name')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, )
    star = models.BooleanField(default=True)
    zvk_name = models.CharField(max_length=15, verbose_name='zvk_unit_name', default='NU')
    main_condition = models.CharField(
        max_length=2,
        choices=main_condition_choices,
        default=in_work,
        verbose_name='repair type')

    def __str__(self):
        return f'{self.station} / {self.title}'

    def get_absolute_url(self):
        return reverse('block_id', kwargs={'block_id': self.pk})


class Generator(models.Model):
    in_work = 'P'
    emergency_repair = 'AP'
    current_repair = 'KP'
    capital_repair = 'KP'
    mean_repair = 'CP'
    forced_downtime = 'Bp'
    main_condition_choices = {
        (in_work, 'in_work'),
        (emergency_repair, 'emergency_repair'),
        (current_repair, 'current_repair'),
        (capital_repair, 'capital_repair'),
        (mean_repair, 'mean_repair'),
        (forced_downtime, 'forced_downtime'),
    }
    title = models.CharField(max_length=64, verbose_name='Generator name')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, )
    star = models.BooleanField(default=True)
    zvk_name = models.CharField(max_length=25, verbose_name='zvk_unit_name', default='NU')
    main_condition = models.CharField(
        max_length=2,
        choices=main_condition_choices,
        default=in_work,
        verbose_name='repair type')


    def __str__(self):
        return f'{self.block} {self.title}'

    def get_absolute_url(self):
        return reverse('gen_id', kwargs={'gen_id': self.pk})

