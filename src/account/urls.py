from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

import account.views

urlpatterns = [
    url(_(r'^register/$'),
        account.views.UserRegisterView.as_view(),
        name='register'),
    url(_(r'^login/$'),
        account.views.UserLoginView.as_view(),
        name='login'),
    url(_(r'^confirm/email/(?P<activation_key>.*)/$'),
        account.views.UserConfirmEmailView.as_view(),
        name='confirm_email'),
    url(_(r'^status/email/$'),
        account.views.UserEmailConfirmationStatusView.as_view(),
        name='status'),
]
