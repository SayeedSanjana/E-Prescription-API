from django.urls import path

# from .views import(
    
#     prescriptionCreate,
    
    
# )

from .views_functions.patients import (
    patients_view,
    patient_info_detail,
)
from .views_functions.prescription import (
    prescription_update_or_delete,
    prescription_view,
)
from .views_functions.notes import (
    notes_list_and_create_view,
    notes_info_detail_and_update
)


urlpatterns = [
    path('prescription-view/', prescription_view, name = 'prescription_view'),
    # path('prescription-create/', prescriptionCreate, name = 'prescriptionCreate'),
    path('prescription-detail-update-delete/<int:pk>/', prescription_update_or_delete, name = 'prescription_delete'),

    path('patients-info-view/', patients_view, name = 'patients_view'),
    path('patient-info-detail/<int:pk>/', patient_info_detail, name = 'prescription_update_delete'),

    path('notes-per-patient/', notes_list_and_create_view, name = 'notes_list_and_create_view'),
    path('patient-notes-info/<int:pk>/', notes_info_detail_and_update, name = 'notes_info_detail_and_update'),

]
