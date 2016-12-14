from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    link = models.TextField(null=True, blank=True, max_length=100, verbose_name='Ссылка на сайт')
    sector = models.CharField(null=True, blank=True, max_length=100, verbose_name='Отрасль')
    phone = models.IntegerField(null=True, blank=True, verbose_name='Телефон')
    address = models.TextField(null=True, blank=True, max_length=200, verbose_name='Адрес')
    vacancy_count = models.IntegerField(null=True, blank=True, default=1, verbose_name='Количество вакансий')
    company_size = models.CharField(null=True, blank=True, max_length=50, verbose_name='Размер компании')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name