from django.urls import path
from . import views



urlpatterns = [
    
    path("admin_dsh",views.admin_dsh,name='admin_dsh'),
    path("banner",views.banner,name='banner'),
    path("add_banner",views.add_banner,name='add_banner'),
    path("add_banner_action",views.add_banner_action,name='add_banner_action'),
    path("edit_banner/<int:bid>",views.edit_banner,name='edit_banner'),
    path("edt_banner_action",views.edt_banner_action,name='edt_banner_action'),
    path("banner_action/<int:bid>",views.banner_action,name='banner_action'),
    path("show_category",views.show_category,name='show_category'),
    path("add_category",views.add_category,name='add_category'),
    path("add_category_action",views.add_category_action,name='add_category_action'),
    path("edit_category/<int:cid>",views.edit_category,name='edit_category'),
    path("edt_category_action",views.edt_category_action,name='edt_category_action'),
    path("category_action/<int:cid>",views.category_action,name='category_action'),
    path("show_brand",views.show_brand,name='show_brand'),
    path("add_brand",views.add_brand,name='add_brand'),
    path("add_brand_action",views.add_brand_action,name='add_brand_action'),
    path("edit_brand/<int:bid>",views.edit_brand,name='edit_brand'),
    path("edt_brand_action",views.edt_brand_action,name='edt_brand_action'),
    path("brand_action/<int:bid>",views.brand_action,name='brand_action'),
    path("show_product",views.show_product,name='show_product'),
    path("edit_product/<int:uid>",views.edit_product,name='edit_product'),
    path("edit_product_action",views.edit_product_action,name='edit_product_action'),
    path("admin_view_product/<int:uid>",views.admin_view_product,name='admin_view_product'),
    path("add_product",views.add_product,name='add_product'),
    path("show_user",views.show_user,name='show_user'),
    path('customeraction/<int:uid>/', views.customeraction, name='customeraction'),
    path('product_action/<int:uid>/', views.product_action, name='product_action'),
    path('add_product_action', views.add_product_action, name='add_product_action'),
    path('order', views.order, name='order'),
    path('coupon_admin', views.coupon_admin, name='coupon_admin'),
    path('manage_coupons/', views.manage_coupons, name='manage_coupons'),
    path('delete_coupon/<int:coupon_id>/', views.delete_coupon, name='delete_coupon'),
    path('edit_coupon/<int:coupon_id>/', views.edit_coupon, name='edit_coupon'),
    path('order_details/<int:oid>/', views.order_details, name='order_details'),
    path('admin_sid/handle_return_request/<int:request_id>/', views.handle_return_request, name='handle_return_request'),
    path('return_requests_admin', views.return_requests_admin, name='return_requests_admin'), 
    path('admin_sid/handle_return_request/<int:request_id>/', views.handle_return_request, name='handle_return_request'),
 
    
]