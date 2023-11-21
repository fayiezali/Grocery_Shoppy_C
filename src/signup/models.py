from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# (1)Personal Data
class UserProfile_MODEL(models.Model):
#
    pro_User                   = models.OneToOneField(User               , on_delete=models.CASCADE   , blank=False  , null=False , verbose_name="اسم المشترك")
    # Pro_FirstName              = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="الإسم الأول")
    Pro_FatherName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الاب")
    Pro_GrandFatherName        = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الجد")
    # Pro_FamilyName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم العائلة")
    Pro_MobileNnumber          = models.CharField(max_length=13                    , db_index=True , blank=True  , null=True  , verbose_name="الجوال"              , default='+966555555555')

    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.pro_User) 
    #
    # def __str__(self):
    #     return f"{self.Pro_FirstName}, {self.Pro_FamilyName}"

    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['pro_User']
    #
    class Meta:
        # The Name of the Model That Will Be Displayed In The Admin Page
        # verbose_name      = _('Personal')
        verbose_name_plural = 'User Profile'
    #
    # 'admin'عرض الصورة في صفحة
    # 'admin'عرض إسم المستخدم رباعياً في صفحة
    # def full_name(self):
    #     return str(self.Pro_FirstName + ' ' + self.Pro_FatherName + ' ' + self.Pro_GrandFatherName + ' ' + self.Pro_FamilyName)
    # full_name.short_description='الإسم رباعيا'  # 'admin'عرض إسم الصورة في صفحة