from django.contrib import admin
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from .models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
# 


# Personal File
@admin.register(UserProfile_MODEL)
class ProfileADMIN(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add a Search Box With The Fields Below:
        search_fields = ('pro_User', 'Pro_FatherName', 'Pro_GrandFatherName','Pro_MobileNnumber')
        #
        #
        # Add a Filter Box
        list_filter = (
        'pro_User'     , 
        'Pro_MobileNnumber'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'pro_User'                  , 
        # 'full_name'               ,
        # 'image_tag'               ,
        # 'Pro_FirstName'             ,
        'Pro_FatherName'            ,
        'Pro_GrandFatherName'       ,
        # 'Pro_FamilyName'            ,
        'Pro_MobileNnumber'                
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, 
        {
        'fields': (
        'pro_User'              ,
        # 'Pro_FirstName'         ,
        'Pro_FatherName'        ,
        'Pro_GrandFatherName'   ,
        # 'Pro_FamilyName'        ,
        'Pro_MobileNnumber'            
        )
        }
        ),
        # ('Advanced', {'classes': ('collapse',),'fields': ('Pro_MobileNnumber')}),
        )
# 