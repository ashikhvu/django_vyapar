from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register', views.register, name='register'),
    
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('sale_invoices', views.sale_invoices, name='sale_invoices'),
    path('estimate_quotation', views.estimate_quotation, name='estimate_quotation'),
    path('payment_in', views.payment_in, name='payment_in'),
    path('sale_order', views.sale_order, name='sale_order'),
    path('delivery_chellan', views.delivery_chellan, name='delivery_chellan'),
    path('sale_return_cr', views.sale_return_cr, name='sale_return_cr'),

    # created by athul
    path('settings', views.settings, name='settings'),
    path('hide_options', views.hide_options, name='hide_options'),

    path('staffhome/<id>', views.staffhome, name='staffhome'),
    path('adminhome', views.adminhome, name='adminhome'),
    
    
    path('staff_register', views.staff_register, name='staff_register'),
    path('staff_registraction', views.staff_registraction, name='staff_registraction'),
    path('company_reg', views.company_reg, name='company_reg'),
    path('company_reg2', views.company_reg2, name='company_reg2'),
    path('add_company', views.add_company, name='add_company'),
    path('log_page', views.log_page, name='log_page'),
    path('login', views.login, name='login'),
    path('adminaccept/<id>', views.adminaccept, name='adminaccept'),
    path('adminreject/<id>', views.adminreject, name='adminreject'),
    path('View_staff', views.View_staff, name='View_staff'),
    path('companyaccept/<id>', views.companyaccept, name='companyaccept'),
    path('companyreject/<id>', views.companyreject, name='companyreject'),
    path('client_request', views.client_request, name='client_request'),
    path('client_details', views.client_details, name='client_details'),
    path('staff_request', views.staff_request, name='staff_request'),
    path('payment_term', views.payment_term, name='payment_term'),
    path('add_payment_terms', views.add_payment_terms, name='add_payment_terms'),
    path('Allmodule/<uid>', views.Allmodule, name='Allmodule'),
    path('addmodules/<uid>', views.addmodules, name='addmodules'),
    path('client_request_overview/<id>', views.client_request_overview, name='client_request_overview'),
    path('client_details_overview/<id>', views.client_details_overview, name='client_details_overview'),


    
    path('companyreport', views.companyreport, name='companyreport'),
    path('Companyprofile', views.Companyprofile, name='Companyprofile'),
    path('editcompanyprofile', views.editcompanyprofile, name='editcompanyprofile'),
    path('editcompanyprofile_action', views.editcompanyprofile_action, name='editcompanyprofile_action'),
    path('editmodule', views.editmodule, name='editmodule'),
    path('editmodule_action', views.editmodule_action, name='editmodule_action'),
    path('admin_notification', views.admin_notification, name='admin_notification'),
    path('module_updation_details/<mid>', views.module_updation_details, name='module_updation_details'),
    path('module_updation_ok/<mid>', views.module_updation_ok, name='module_updation_ok'),
    path('staff_profile/<sid>', views.staff_profile, name='staff_profile'),
    path('editstaff_profile/<sid>', views.editstaff_profile, name='editstaff_profile'),
    path('editstaff_profile_action/<sid>', views.editstaff_profile_action, name='editstaff_profile_action'),

    path('distributor_home', views.distributor_home, name='distributor_home'),
    path('distributor_reg', views.distributor_reg, name='distributor_reg'),
    path('distributor_reg_action', views.distributor_reg_action, name='distributor_reg_action'),
    path('distributors', views.distributors, name='distributors'),
    path('clients', views.clients, name='clients'),
    path('distributor_request', views.distributor_request, name='distributor_request'),
    path('admin_distributor_accept/<id>', views.admin_distributor_accept, name='admin_distributor_accept'),
    path('admin_distributor_reject/<id>', views.admin_distributor_reject, name='admin_distributor_reject'),
    path('distributor_request_overview/<id>', views.distributor_request_overview, name='distributor_request_overview'),
    path('distributor_details', views.distributor_details, name='distributor_details'),
    path('distributor_details_overview/<id>', views.distributor_details_overview, name='distributor_details_overview'),
    path('dcompany_request', views.dcompany_request, name='dcompany_request'),
    path('dcompany_details', views.dcompany_details, name='dcompany_details'),
    path('dcompany_request_overview/<id>', views.dcompany_request_overview, name='dcompany_request_overview'),
    path('distributor_accept_company/<id>', views.distributor_accept_company, name='distributor_accept_company'),
    path('distributor_reject_company/<id>', views.distributor_reject_company, name='distributor_reject_company'),
    path('dcompany_details_overview/<id>', views.dcompany_details_overview, name='dcompany_details_overview'),
    path('distributor_profile', views.distributor_profile, name='distributor_profile'),
    # ========================================   ASHIKH V U (START) ======================================================

    path('item_create', views.item_create, name='item_create'),
    path('items_list', views.items_list, name='items_list'),
    path('item_create_new', views.item_create_new, name='item_create_new'),
    path('item_delete/<int:pk>', views.item_delete, name='item_delete'),
    path('item_view_or_edit/<int:pk>', views.item_view_or_edit, name='item_view_or_edit'),
    path('item_unit_create', views.item_unit_create, name='item_unit_create'),
    path('item_update/<int:pk>', views.item_update, name='item_update'),
    path('item_search_filter', views.item_search_filter, name='item_search_filter'),

    # ========================================   ASHIKH V U (END) ======================================================

    
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)