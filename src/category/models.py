from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
#
#
# 
# Model Category
class CategoryMODEL(models.Model):
	
	Cate_name         = models.CharField(max_length=200      			  , db_index=True  ,                            verbose_name="Name")
	Cate_slug         = models.SlugField(max_length=200      			  , db_index=True  , unique=True ,              verbose_name="Slug")
	Cate_image        = models.ImageField(upload_to="Catgory_File_Photo/" , db_index=True  , blank=False , null=False , verbose_name="Image Preview"  ,default='Default_Image.png')
	Cate_available 	  = models.BooleanField(default=True                  , db_index=True  ,                            verbose_name="Available")
#
	class Meta:
	# 'Z-A' in descending order
		ordering = ('Cate_name',)
		verbose_name = "Category"
		# The Name of the Model That Will Be Displayed In The Admin Page
		verbose_name_plural = "Categories"

    # 'admin'display the field name on a page
	def __str__(self):
		return self.Cate_name

	# def get_absolute_url(self):
	# 	return reverse('shop:product_list_category',args=[self.slug])
#
#
#
# Module Sub Category
class SubCategoryMODEL(models.Model):
	SubCat_category      = models.ForeignKey(CategoryMODEL , related_name='categories_sub' , on_delete=models.CASCADE              								, verbose_name="Category")
	SubCat_name          = models.CharField(max_length=200 							, db_index=True                                								, verbose_name="Name")
	SubCat_slug          = models.SlugField(max_length=200 							, db_index=True	,unique=True                   								, verbose_name="Slug")
	SubCat_image         = models.ImageField(upload_to="Sub_Catgories_File_Photo/" 	, db_index=True , blank=False , default='Default_Image.png'    , null=False , verbose_name="Image Preview"  )
	SubCat_available 	 = models.BooleanField(default=True      					, db_index=True                                								, verbose_name="Available")

	class Meta:
	# 'Z-A' in descending order
		ordering = ('SubCat_name',)
		verbose_name = "Sub Category"
		# The Name of the Model That Will Be Displayed In The Admin Page
		verbose_name_plural = "Sub Categories"

    # 'admin'display the field name on a page
	def __str__(self):
		return self.SubCat_name

	@staticmethod
	def get_all_categories():
            return SubCategoryMODEL.objects.all()
#

#
#
# #
# # Module Sub Category Branch
# class SubCategoryBranchMODEL(models.Model):
# 	SubCatBra_category       = models.ForeignKey(SubCategoryMODEL , related_name='sub_category_branch' , on_delete=models.CASCADE 										, verbose_name="Sub Category Branch") 
# 	SubCatBra_name           = models.CharField(max_length=200 , db_index=True                                                            								, verbose_name="Name")
# 	SubCatBra_slug           = models.SlugField(max_length=200 , db_index=True,unique=True                            					  								, verbose_name="Slug")
# 	SubCatBra_image          = models.ImageField(upload_to="Sub_Catgories_Branch_File_Photo/" , db_index=True , blank=False  , null=False ,default='Default_Image.png'  , verbose_name="Image Preview")
# 	SubCatBra_available 	 = models.BooleanField(default=True       , db_index=True                                  					  								, verbose_name="Available")

# 	class Meta:
# 	    # 'Z-A' in descending order
# 		ordering = ('SubCatBra_name',)
# 		verbose_name = "Sub Category Branch"
# 		# The Name of the Model That Will Be Displayed In The Admin Page
# 		verbose_name_plural = "Sub Categories Branch"

#     # 'admin'display the field name on a page
# 	def __str__(self):
# 		return self.SubCatBra_name
# #
#
#