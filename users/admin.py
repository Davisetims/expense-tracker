from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from users.models import User

class CustomUserAdmin(UserAdmin):
    # Adding fields to the existing fieldsets for the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (
            "Other Fields",  # Section title
            {
                "fields": (
                    'phone_number',
                    'avatar',
                    
                    
                )
            },
        ),
    )

    # Adding fields to the existing add_fieldsets for the user creation page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Other Fields",  # Section title for user creation form
            {
                "fields": (
                    'first_name',
                    'last_name',
                    'phone_number',
                    'email',
                )
            },
        ),
    )

    # Fields to display in the list view
    list_display = (
        'user_id', 
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'phone_number',  
        'is_staff', 
        'is_active'
    )
    
    # Optional: fields to filter by in the admin list view
    list_filter = ('is_staff', 'is_active')
    
    # Optional: fields to search by in the admin list view
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

    exclude = ('created_at',)
    
    def user_id(self, obj):
        return obj.id
    user_id.short_description ='user_id'


admin.site.register(User, CustomUserAdmin)