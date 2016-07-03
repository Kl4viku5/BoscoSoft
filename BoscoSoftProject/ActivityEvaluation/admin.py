from django.contrib import admin

from .models import Activity, Evaluation, Question, Answer

admin.site.register(Activity)
admin.site.register(Evaluation)
admin.site.register(Question)
admin.site.register(Answer)
