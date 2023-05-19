from money_tracker.views import create_transaction_flutter, show_tracker
from django.urls import path, include
from money_tracker.views import create_transaction
from money_tracker.views import show_xml 
from money_tracker.views import show_json 
from money_tracker.views import show_xml_by_id, show_json_by_id 
from money_tracker.views import register #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import modify_transaction
from money_tracker.views import delete_transaction
from money_tracker.views import create_transaction_ajax








app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('xml/', show_xml, name='show_xml'), 
    path('create', create_transaction, name='create_transaction'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('modify/<int:id>', modify_transaction, name='modify_transaction'), #sesuaikan dengan nama fungsi yang dibuat
    path('delete/<int:id>', delete_transaction, name='delete_transaction'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-ajax/', create_transaction_ajax, name='create_transaction_ajax'),
    path('create-flutter/', create_transaction_flutter, name='create_transaction_flutter'),




]
