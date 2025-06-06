from django.db import models
from users.models import NULLABLE
from django.utils.translation import gettext_lazy as _


class Section(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['id']


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    content = models.CharField(verbose_name=_('Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Section Content')
        verbose_name_plural = _('Section Contents')
        ordering = ['id']


class Question(models.Model):
    question_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)
    question = models.TextField(verbose_name=_('Question'), **NULLABLE)
    answer = models.CharField(max_length=40, verbose_name=_('Answer'), **NULLABLE)

    def __str__(self):
        return f'Вопрос по курсу {self.question_section.title}'

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['question_section']
