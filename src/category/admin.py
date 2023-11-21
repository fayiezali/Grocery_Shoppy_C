from django.contrib import admin
from .models import * # import all models
from django.utils.html import format_html
#
#
# admin.site.register(CategoryMODEL)
# admin.site.register(SubCategoryMODEL)


# Add The Child Table(ProductImageMODEL) Inside The Parent Table(ProductMODEL) 
class SubCategoryMODELAdmin(admin.TabularInline):
	model = SubCategoryMODEL
	prepopulated_fields  = {'SubCat_slug':('SubCat_name',)} # Auto Filled # Autofill Slug field from name field  
#
#
#
# Admin View for Category Model
class CategoryMODELAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','Cate_name','Cate_available','Cate_image',)
	list_filter          = ('Cate_available','Cate_name',) # filter by Available Field
	list_editable        = ('Cate_name','Cate_available',)
	prepopulated_fields  = {'Cate_slug':('Cate_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	inlines = [SubCategoryMODELAdmin]
	# list_display_links = ('CATE_category_image',) 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.Cate_image.url))
	picture_displayDEF.short_description='Picture' 
	
# Display the Model on the Admin Page
admin.site.register(CategoryMODEL, CategoryMODELAdmin)
#
#
#
# The class has been inherited as an addict in order to make a modification / customization 
class SubCategoryMODELAdmin(admin.ModelAdmin):
	#Admin View for Category Sub Model
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','SubCat_name','SubCat_available','SubCat_image',)
	list_filter          = ('SubCat_available','SubCat_name',) # filter by Available Field
	list_editable        = ('SubCat_name','SubCat_available',)
	prepopulated_fields  = {'SubCat_slug':('SubCat_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# list_display_links = ('CATE_category_image',) 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.SubCat_image.url))
	picture_displayDEF.short_description='Picture' 
#
# Display the Model on the Admin Page
admin.site.register(SubCategoryMODEL, SubCategoryMODELAdmin)








# # Add The Child Table(ProductImageMODEL) Inside The Parent Table(ProductMODEL) 
# class SubCategoryMODELAdmin(admin.TabularInline):
# 	model = SubCategoryMODEL
# 	prepopulated_fields  = {'SubCat_slug':('SubCat_name',)} # Auto Filled # Autofill Slug field from name field  
# #
# #
# # Add The Child Table(SubCategoryBranchMODEL) Inside The Parent Table(SubCategoryMODEL) 
# class SubCategoryBranchMODELAdmin(admin.TabularInline): 
# 	model = SubCategoryBranchMODEL
# 	prepopulated_fields  = {'SubCatBra_slug':('SubCatBra_name',)} # Auto Filled # Autofill Slug field from name field  
# #
# #
# # class CategoryMODELAdmin(admin.TabularInline): 
# # 	model = CategoryMODEL
# # 	prepopulated_fields  = {'Cate_slug':('Cate_name',)} # Auto Filled # Autofill Slug field from name field  

# # Admin View for Category Model
# class CategoryMODELAdmin(admin.ModelAdmin):
# 	# The fields to be shown on the Admin page
# 	list_display        = ('picture_displayDEF','Cate_name','Cate_available','Cate_image',)
# 	list_filter          = ('Cate_available','Cate_name',) # filter by Available Field
# 	list_editable        = ('Cate_name','Cate_available',)
# 	prepopulated_fields  = {'Cate_slug':('Cate_name',)} # Auto Filled # Autofill Slug field from name field  
# 	empty_value_display = '-empty-'
# 	inlines = [SubCategoryMODELAdmin]
# 	# list_display_links = ('CATE_category_image',) 

# 	# View The Image On the Admin Page
# 	def picture_displayDEF(self,obj):
# 	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.Cate_image.url))
# 	picture_displayDEF.short_description='Picture' 
	
# # Display the Model on the Admin Page
# admin.site.register(CategoryMODEL, CategoryMODELAdmin)
# #
# #
# #
# # The class has been inherited as an addict in order to make a modification / customization 
# class SubCategoryMODELAdmin(admin.ModelAdmin):
# 	#Admin View for Category Sub Model
# 	# The fields to be shown on the Admin page
# 	list_display        = ('picture_displayDEF','SubCat_name','SubCat_available','SubCat_image',)
# 	list_filter          = ('SubCat_available','SubCat_name',) # filter by Available Field
# 	list_editable        = ('SubCat_name','SubCat_available',)
# 	prepopulated_fields  = {'SubCat_slug':('SubCat_name',)} # Auto Filled # Autofill Slug field from name field  
# 	empty_value_display = '-empty-'
# 	inlines = [SubCategoryBranchMODELAdmin]

# 	# list_display_links = ('CATE_category_image',) 

# 	# View The Image On the Admin Page
# 	def picture_displayDEF(self,obj):
# 	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.SubCat_image.url))
# 	picture_displayDEF.short_description='Picture' 
# #
# # Display the Model on the Admin Page
# admin.site.register(SubCategoryMODEL, SubCategoryMODELAdmin)

