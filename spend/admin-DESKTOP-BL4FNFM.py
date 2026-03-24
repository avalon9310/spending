from django.contrib import admin
from .models import Spend

class SpendAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_title', 'custom_user') 
    search_fields = ('title', 'amount') 

    @admin.display(description='標題')
    def custom_title(self, obj):
        return obj.title
    # def custom_title(self, obj):
    #     return obj.title
    # custom_title.short_description = '標題'

    
    @admin.display(description='創建者')
    def custom_user(self, obj):
        return obj.user
    # def custom_user(self, obj):
    #     return obj.user
    # custom_user.short_description = '創建者'
    
admin.site.register(Spend, SpendAdmin)
