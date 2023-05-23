from django.urls import path, include
from myapp import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,    PasswordResetDoneView,   PasswordResetConfirmView,    PasswordResetCompleteView


urlpatterns = [
    path('home/',views.homeview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('form/',views.formview.as_view()),
    path('mattress/',views.mattressview),
    path('contact/',views.contactview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('services/',views.servicesview.as_view()),
    path('insertcontact/',views.insertcontact),
    path('blogs/',views.blogview),
    path('blogsdetail/<int:id>',views.blogsdetail),
    path('collection/',views.collection),
    path('Faq/',views.Faqview),
    path('product/<int:id>',views.productview),
    path('productdetail/<int:id>',views.productdetail),
    path('signup/',views.signupview),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('dolike/',views.dolike),
    path('shipping/',views.shippingview.as_view()),
    path('Signup/',views.signupview),
    path('insertemail/',views.insertemail),
    path('Myorder/',views.Myorderview),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('Addblogs/',views.Addblogsview.as_view()),
    path('insertblogs/',views.insertblogs),
  ]
