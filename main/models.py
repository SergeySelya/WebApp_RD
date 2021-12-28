from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Post_0(models.Model):
    fio = models.CharField("ФИО", max_length=30)
    post = models.CharField("Должность", max_length=50)
    start_date = models.DateField("Дата приема")
    wages = models.IntegerField(verbose_name="Зарплата")
    total_paid = models.IntegerField(verbose_name="Всего выплачено")


    class Meta:
        verbose_name = "ген. деиректора"
        verbose_name_plural = "Level 0 - ген. директор"

    def __str__(self):
        return self.fio


class Post_1(models.Model):
    # user = models.ForeignKey(User, verbose_name="ФИО", on_delete=models.CASCADE)
    fio = models.CharField("ФИО", max_length=30)
    post = models.CharField("Должность", max_length=50)
    post_head = models.ForeignKey(Post_0, verbose_name="Начальник", on_delete=models.SET_NULL, null=True)
    start_date = models.DateField("Дата приема")
    wages = models.IntegerField(verbose_name="Зарплата")
    total_paid = models.IntegerField(verbose_name="Всего выплачено")

    class Meta:
        verbose_name = "Директора"
        verbose_name_plural = "Level 1 - директор"

    def __str__(self):
        return self.fio

class Post_2(models.Model):
    # user = models.ForeignKey(User, verbose_name="ФИО", on_delete=models.CASCADE)
    fio = models.CharField("ФИО", max_length=30)
    post = models.CharField("Должность", max_length=50)
    post_head = models.ForeignKey(Post_1, verbose_name="Начальник", on_delete=models.SET_NULL, null=True)
    start_date = models.DateField("Дата приема")
    wages = models.IntegerField(verbose_name="Зарплата")
    total_paid = models.IntegerField(verbose_name="Всего выплачено")

    class Meta:
        verbose_name = "главные менеджеры"
        verbose_name_plural = "Level 2 - главный менеджер"

    def __str__(self):
        return self.fio


class Post_3(models.Model):
    # user = models.ForeignKey(User, verbose_name="ФИО", on_delete=models.CASCADE)
    fio = models.CharField("ФИО", max_length=30)
    post = models.CharField("Должность", max_length=50)
    post_head = models.ForeignKey(Post_2, verbose_name="Начальник", on_delete=models.SET_NULL, null=True)
    start_date = models.DateField("Дата приема")
    wages = models.IntegerField(verbose_name="Зарплата")
    total_paid = models.IntegerField(verbose_name="Всего выплачено")

    class Meta:
        verbose_name = "младшие менеджеры"
        verbose_name_plural = "Level 3 - младший менеджер"

    def __str__(self):
        return self.fio


class Post_4(models.Model):
    # user = models.ForeignKey(User, verbose_name="ФИО", on_delete=models.CASCADE)
    fio = models.CharField("ФИО", max_length=30)
    post = models.CharField("Должность", max_length=50)
    post_head = models.ForeignKey(Post_3, verbose_name="Начальник", on_delete=models.SET_NULL, null=True)
    start_date = models.DateField("Дата приема")
    wages = models.IntegerField(verbose_name="Зарплата")
    total_paid = models.IntegerField(verbose_name="Всего выплачено")

    class Meta:
        verbose_name = "консультанты"
        verbose_name_plural = "Level 4 - консультант"

    def __str__(self):
        return self.fio


class Post_5(models.Model):
    # user = models.ForeignKey(User, verbose_name="ФИО", on_delete=models.CASCADE)
    fio = models.CharField("ФИО", max_length=30)
    post = models.CharField("Должность", max_length=50)
    post_head = models.ForeignKey(Post_4, verbose_name="Начальник", on_delete=models.SET_NULL, null=True)
    start_date = models.DateField("Дата приема")
    wages = models.IntegerField(verbose_name="Зарплата")
    total_paid = models.IntegerField(verbose_name="Всего выплачено")

    class Meta:
        verbose_name = "стажеры"
        verbose_name_plural = "Level 5 - стажер"

    def __str__(self):
        return self.fio