from django.core.management.base import BaseCommand, CommandError
from links.tasks import my_task

class Command(BaseCommand):
    help = 'Start tasks'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        my_task()