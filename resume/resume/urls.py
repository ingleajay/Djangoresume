from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from biodata import views as v
from dashboard import views as d
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from biodata.forms import ResetForm, ResetConfirmForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('delete/<int:id>/', v.delete_user, name="delete"),
    path('update/', d.update_user, name="update"),
    path('<int:id>/', v.view_user, name="view"),
    path('login/', v.user_login, name="login"),
    path('reg/', v.register, name="reg"),
    path('resume/', d.create_resume, name="resume"),
    path('logout/', v.user_logout, name="logout"),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=ResetForm), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html/', form_class=ResetConfirmForm), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html/'), name="password_reset_complete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
