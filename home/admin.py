from django.contrib import admin

# Register your models here.
from .models import BlogModel , profile
from django.contrib import messages


admin.site.register(BlogModel)
admin.site.register(profile)

  
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title','user','slug')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
admin.site.unregister(BlogModel)
admin.site.register(BlogModel,BlogModelAdmin)

admin.site.unregister(profile) 
class profileAdmin(admin.ModelAdmin):
    list_display = ('verified', 'user', 'token')
  
    def verified(self, obj):
        return obj.is_verified == 1
  
    verified.boolean = True
    def make_verified(modeladmin, request, queryset):
        queryset.update(is_verified = 1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_unverfied(modeladmin, request, queryset):
        queryset.update(is_verified = 0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")

    admin.site.add_action(make_verified, "Make Active")
    admin.site.add_action(make_unverfied, "Make Inactive")
  
    def has_delete_permission(self, request, obj = None):
        return False
    def has_add_permission(self, request):
        return False
  
admin.site.register(profile,profileAdmin)
  