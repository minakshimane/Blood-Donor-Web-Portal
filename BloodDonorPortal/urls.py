"""BloodDonorPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BloodDonor import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('onlogin/', views.onlogin, name='onlogin'),
    path('adminhome/',views.adminhome,name='adminhome'),

    path('register/',views.showRegister,name='register'),
    path('savedonar/',views.savedonar,name='savedonar'),
    path('dashboard/',views.dashboard,name='dashboard'),


    path('donar/',views.donar,name='donar'),
    #path('register/',views.register,name='register'),
    #path('savedonar/',views.savedonar,name='savedonar'),
    path('ondonarlogin/',views.ondonarlogin,name='ondonarlogin'),
    path('donarlog/',views.donarlog,name="donarlog"),
    path('donor_profile/',views.donor_profile,name='donor_profile'),
    path('donar_update/',views.donar_update,name="donar_update"),
    path('update_donor/',views.update_donor,name='update_donor'),
    path('logout/',views.logout,name='logout'),
    path('logoutd/',views.logoutd,name='logoutd'),
    #error kuthe yetoy logout karyachya adhi mage ghetlyawar parat donor war cli k kel ki welcome none yete  url che page kuthe ahe html


    path('org/', views.org,name="org"),
    path('orgLogin/',views.orgLogin,name='orgLogin'),

    path('faqs/',views.faqs,name="faqs"),
    path('faqsSend/',views.inboxTo,name="faqsSend"),

    path('inbox/',views.inbox,name="inbox"),
    path('gly/',views.gly,name='gly'),

    path('showdonor/',views.showdonor,name='showdonor'),

    path('donarA/',views.leftdonar,name='donarA'),
    path('onnext/',views.leftdonarnext,name='onnext'),
    path('onsecondnext/',views.onsecondnext,name='onsecondnext'),

    path('bloodA/',views.leftBloodBank,name='bloodA'),
    path('onBankNext/',views.leftBloodBankNext,name='onBankNext'),
    path('onSecondBankNext/',views.leftBloodBanksecondNext,name='onSecondBankNext'),
    path('other/',views.other,name='other'),

    path('hospitalA/', views.lefthospital,name='hospitalA'),
    path('onHospitalNext/', views.leftHospitalNext,name='onHospitalNext'),
    path('onSecondHospitalNext/',views.leftHospitalSecondNext,name="onSecondHospitalNext"),

    path('organisation/',views.organisation,name="organisation"),
    path('saveOrganizationDetails/',views.saveOrganizationDetails,name="saveOrganizationDetails",),

    path('profiles/',views.profileView,name='profiles'),
    path('donorProfiles',views.profilesViewOfDonor,name="donorProfiles"),
    path('organizationProfiles/', views.profilesViewOfOrg,name="organizationProfiles"),

    path('benefits/',views.benefits,name='benefits'),
    path('important/',views.important,name='important'),
    path('whbenefits/',views.whbenefits,name='whbenefits'),

]


