from django.test import TestCase
from .models import TaskModel
from datetime import datetime 

# Create your tests here.
class TaskDatabase(TestCase):
    def Insert_Data(self):
        TaskModel.objects.create(
                            title ="Finish school work",
                            description="complete all the task assign by the student",
                            due_date = datetime.now(),
                            status = "0",
                            user_choice = "0"
                        )
        self.assertEqual(TaskModel.objects.count(),1)
