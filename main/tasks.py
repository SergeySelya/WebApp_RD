from .models import Post_0, Post_1, Post_2, Post_3, Post_4, Post_5
from celery import shared_task


@shared_task
def add_salary():
    m0 = Post_0.objects.all()
    m0.total_paid += m0.wages
    m0.save()
    m1 = Post_1.objects.all()
    m1.total_paid += m1.wages
    m1.save()
    m2 = Post_2.objects.all()
    m2.total_paid += m2.wages
    m2.save()
    m3 = Post_3.objects.all()
    m3.total_paid += m3.wages
    m3.save()
    m4 = Post_4.objects.all()
    m4.total_paid += m4.wages
    m4.save()
    m5 = Post_5.objects.all()
    m5.total_paid += m5.wages
    m5.save()



