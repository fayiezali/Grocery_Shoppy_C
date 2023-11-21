from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
#
#
#
# Password Change Done 
urlpatterns = [
        # thies Was Created By Django
        # Password Reset - Password Reset Done - Password Reset Confirm - Password Reset Comlete (3)
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
        # The URL To Redirect To After a Successful Password Reset Request
        # thies Was Created By Django
        path('password-reset/'                         , auth_views.PasswordResetView.as_view(
        template_name='password_reset/password_resetHTML.html', # The Name Of a Template To Display For The View Use
        subject_template_name='password_reset/password_reset_subject.txt',
        success_url= reverse_lazy('password_reset_done')), # Redirect To URL Address
        name='password_reset'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset/done/'                    , auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset/password_reset_doneHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_done'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset/password_reset_confirmHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_confirm'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        # thies Was Created By Django
        path('password-reset-complete/'               , auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset/password_reset_completeHTML.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_complete'), # Name URL pattern
]


