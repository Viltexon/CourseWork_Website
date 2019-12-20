from django.contrib import admin

# Register your models here.



from .models import Crew, Modules, News, Specializations, Tourism, Research, CrewSpec, Profile
from .models import Newsletter, CrewRes

admin.site.register(Crew)
admin.site.register(Modules)
admin.site.register(News)
admin.site.register(Specializations)
admin.site.register(Tourism)
admin.site.register(Research)
admin.site.register(CrewSpec)
admin.site.register(CrewRes)

admin.site.register(Newsletter)

admin.site.register(Profile)

