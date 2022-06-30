from django.contrib import admin

from capstone.models import Subscription
from capstone.models import Inbox
# Register your models here.
admin.site.register(Subscription)
admin.site.register(Inbox)