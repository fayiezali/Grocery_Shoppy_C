from django.db import models
from order_orderdetail.models import OrderMODEL
from .models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now
from django.db.models.signals import post_save , post_delete # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده#



class ShipmentTrackMODEL(models.Model):
    shipment_track_user              = models.OneToOneField(User, on_delete = models.SET_NULL , null=True, blank=True)
    shipment_track_order_id          = models.CharField(max_length=10, default='', null=True, blank=True)
    shipment_track_confirmed_order   = models.BooleanField(default=False)
    shipment_track_Processing_order  = models.BooleanField(default=False)
    shipment_track_dispatch_product  = models.BooleanField(default=False)
    shipment_track_delivery          = models.BooleanField(default=False)
    shipment_track_Product_delivered = models.BooleanField(default=False)
    # shipment_track_user              = models.ForeignKey(User , on_delete = models.CASCADE)
    # shipment_track_order_id          = models.ForeignKey(OrderMODEL, on_delete=models.CASCADE, null=True, blank=True)
    # shipment_track_order_id          = models.ForeignKey(OrderMODEL, on_delete=models.CASCADE)

    
    class Meta: 
        ordering = ('-shipment_track_order_id',)
        verbose_name = "Shipment Track"
        verbose_name_plural = "Shipment Tracs" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name: ' + str(self.shipment_track_user) + '-' \
                'Order ID: ' + str(self.shipment_track_order_id) 
#
# #
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ
    def shipment_trackMODEL(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            ShipmentTrackMODEL.objects.create(shipment_track_user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(shipment_trackMODEL , sender=User)


