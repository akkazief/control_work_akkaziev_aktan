from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Record(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Имя")
    email = models.EmailField(null=False, blank=False, verbose_name="Почта")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],verbose_name="Статус")


    def __str__(self):
        return self.name

    class Meta:
        db_table = "records"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
