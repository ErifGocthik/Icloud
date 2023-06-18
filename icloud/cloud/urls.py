from django.urls import path

from cloud.views import cloud_image_detail, CloudList, test_view, delete_from_cloud, ArchiveList, \
    ArchiveListForm, ArchiveDetails, delete_from_archive, ArchiveCycle, ArchiveList2, CloudListMain, \
    controlImageInArchive, add_image_in_archive, remove_image_from_archive

app_name = 'cloud'

urlpatterns = [
    path('', CloudListMain.as_view(), name='cloud_list'),
    path('imageform/', CloudList.as_view(), name='img_form'),
    path('image<int:id>_detail/', cloud_image_detail, name='img_detail'),
    path('test/', test_view, name='test'),
    path('delete/<int:id>', delete_from_cloud, name='delete'),
    path('archives/', ArchiveList.as_view(), name='archives'),
    path('archive_form/', ArchiveListForm.as_view(), name='archive_form'),
    path('archive/<int:pk>', ArchiveDetails.as_view(), name='archive_detail'),
    path('archive/<int:id>/remove/<int:pk>', delete_from_archive, name='delete_arch'),
    path('<int:id>/add/<int:pk>',  controlImageInArchive, name='check_image'),
    path('<int:id>/movein/<int:pk>', add_image_in_archive, name='add_image'),
    path('<int:id>/moveout/<int:pk>', remove_image_from_archive, name='remove_image')
]
