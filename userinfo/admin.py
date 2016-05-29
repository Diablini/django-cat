from django.contrib import admin
from models import myUser

# Register your models here.

class myUserAdmin(admin.ModelAdmin):
	pass
admin.site.register(myUser, myUserAdmin)



