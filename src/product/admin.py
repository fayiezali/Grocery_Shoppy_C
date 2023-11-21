from django.contrib import admin
from . models import *
from django.utils.html import format_html

# admin.site.register(ProductMODEL)

# Admin View for Category Model
class ProductMODELAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','product_category','product_name','product_description','product_price','product_image','product_is_active','product_publish_date')
	list_filter          = ('product_category','product_name','product_is_active','product_publish_date') # filter by Available Field
	list_editable        = ('product_category','product_name','product_is_active','product_description','product_price','product_image',)
	# prepopulated_fields  = {'Cate_slug':('Cate_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# inlines = [ProductMODELAdmin]
	# list_display_links = ('CATE_category_image',) 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.product_image.url))
	picture_displayDEF.short_description='Picture' 
	
# Display the Model on the Admin Page
admin.site.register(ProductMODEL, ProductMODELAdmin)
