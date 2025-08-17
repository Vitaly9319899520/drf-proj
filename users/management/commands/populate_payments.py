from django.core.management.base import BaseCommand
from users.models import Payment, User, Course

class Command(BaseCommand):
    help = 'Populate payments data'

    def handle(self, *args, **kwargs):
        user = User.objects.get(pk=1)
        course = Course.objects.get(pk=1)
        Payment.objects.create(user=user, payment_date="2023-10-01", paid_course=course, amount=1000, payment_method='cash')
        self.stdout.write(self.style.SUCCESS('Successfully populated payments data'))