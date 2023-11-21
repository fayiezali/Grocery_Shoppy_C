from django.db import models
from .models import *
from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now
from category.models import SubCategoryMODEL  

# Model Proudect
class ProductMODEL(models.Model):
    product_category     = models.ForeignKey(SubCategoryMODEL , related_name='products_subcategorybranch', on_delete=models.CASCADE ,  verbose_name='Sub Category Branch')
    # product_category     = models.ForeignKey(SubCategoryBranchMODEL , related_name='products_subcategorybranch', on_delete=models.CASCADE ,  verbose_name='Sub Category Branch')
    product_name         = models.CharField(max_length=200)
    product_description  = models.TextField()
    # product_price        = models.DecimalField(max_digits=10,decimal_places=2)
    product_price        = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('00.00'), blank=True , null=True , verbose_name="Price")
    product_image        = models.ImageField(upload_to="Productes_File_Photo/%Y/%m/%d/")
    product_is_active 	 = models.BooleanField(default=False)
    product_publish_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering            = ('-product_publish_date',)
        verbose_name        = "Product"
        verbose_name_plural = "Products" 



    @staticmethod
    def get_products_by_id(ids):
        return ProductMODEL.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return ProductMODEL.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return ProductMODEL.objects.filter (product_category=category_id)
        else:
            return ProductMODEL.get_all_products();
    # 'admin'display the field name on a page
    def __str__(self):
        return self.product_name



class ProductImageMODEL(models.Model): 
    ProductImage_product = models.ForeignKey(ProductMODEL ,  related_name="productimages_product" ,on_delete=models.CASCADE ,  verbose_name='Product Name')
    ProductImage_image   = models.ImageField(upload_to="Productes_File_Photo/" , db_index=True , blank=False  , null=False , verbose_name="Image Preview"  , default='Default_Image.png')

    class Meta:
        ordering = ('-ProductImage_product',)
        index_together = (('id',),)
        verbose_name = "Product Image"
        verbose_name_plural = "Products Images"

    # 'admin'display the field name on a page 
    def __str__(self):
        return self.ProductImage_product

    # def get_absolute_url(self):
    #     return reverse('product:product_detail',args=[self.id])