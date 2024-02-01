from django.db import models

class Controller(models.Model):
    type = models.CharField(max_length=10, verbose_name = 'Тип')
    sn = models.IntegerField(verbose_name = 'Серийный номер контроллера')
    fw = models.CharField(max_length=10, verbose_name = 'Версия прошивки контроллера')
    conn_fw = models.CharField(max_length=10, verbose_name = 'Версия прошивки модуля связи')
    active = models.IntegerField(verbose_name = 'Признак активированности контроллера')
    mode = models.IntegerField(verbose_name = 'Режим работы контроллера')
    controller_ip = models.URLField(verbose_name = 'IP адрес контроллера в локальной сети')

    def __str__(self):
        return f"{self.type} - {self.sn}"