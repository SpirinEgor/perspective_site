#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from django.db import models

MATERIALS = (
    ("Углеродистая сталь", "Углеродистая сталь"),
    ("СТ 10", "СТ 10"),
    ("СТ 20", "СТ 20"),
    ("СТ 35", "СТ 35"),
    ("СТ 45", "СТ 45"),
    ("СТ 20С", "СТ 20С"),
    ("СТ 20А", "СТ 20А"),
    ("СТ 20КТ", "СТ 20ФА"),
    ("СТ 13ХФА", "СТ 13ХФА"),
    ("СТ 09Г2С", "СТ 09Г2С"),
    ("СТ 12Х1МФ", "СТ 12Х1МФ"),
    ("СТ 15Х5М", "СТ 15Х5М"),
    ("04X18H10", "04X18H10"),
    ("06XH28MДT", "06XH28MДT"),
    ("08X13", "08X13"),
    ("08X17T", "08X17T"),
    ("08X20H14C2", "08X20H14C2"),
    ("08X18H10", "08X18H10"),
    ("08X18H10T", "08X18H10T"),
    ("08X18H12T", "08X18H12T"),
    ("08X17H15M3T", "08X17H15M3T"),
    ("08X22H6T", "08X22H6T"),
    ("08X18H12Б", "08X18H12Б"),
    ("10X17H13M2T", "10X17H13M2T"),
    ("10X23H18", "10X23H18"),
    ("12X13", "12X13"),
    ("12X17", "12X17"),
    ("12X18H10T", "12X18H10T"),
    ("12X18H12T", "12X18H12T"),
    ("12X18H9", "12X18H9"),
    ("15X25T", "15X25T"),
    ("17X18H9", "17X18H9"),
    ("Дюралюминий", "Дюралюминий"),
    ("Титан", "Титан"),
    ("Медь", "Медь"),
    ("Латунь", "Латунь"),
    ("Свинец", "Свинец"),
    ("Золото", "Золото")
)
FORM = (
    ("Круглая", "Круглая"),
    ("Квадратная", "Квадратная"),
    ("Прямоугольная", "Прямоугольная")
)

class Pipe(models.Model):
    GOST = models.CharField(verbose_name = "ГОСТ", db_index = True, max_length = 30)
    material = models.CharField(choices = MATERIALS, default = 1, db_index = True, verbose_name = "Материал", max_length = 30)
    size = models.CharField(verbose_name = "Диаметр", db_index = True, max_length = 30)
    wall_thickness = models.FloatField(verbose_name = "Толщина стенки")
    length = models.FloatField(verbose_name = "Длина трубы", default = 0)
    weight = models.FloatField(verbose_name = "Вес", default = 0)

    class Meta:
        ordering = ["GOST"]
        unique_together = ("GOST", "material", "wall_thickness", "size", "length", "weight")
        verbose_name = "труба"
        verbose_name_plural = "трубы"
