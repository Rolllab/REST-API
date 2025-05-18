from os import path as p

from django.urls import path

from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig
from sections.views import SectionListApiView, SectionCreateApiView, SectionRetrieveApiView, SectionUpdateApiView, \
    SectionDestroyApiView, ContentListApiView, ContentCreateApiView, ContentRetrieveApiView, ContentUpdateApiView, \
    ContentDestroyApiView, QuestionListApiView, QuestionRetrieveApiView


app_name = SectionsConfig.name

router = DefaultRouter()

section = 'section/'
create = 'create/'
update = 'update/'
delete = 'delete/'
int_pk = '<int:pk>/'
content = 'content/'
question = 'question/'

urlpatterns = [
    # Section urlpatterns
    path(p.join(section), SectionListApiView.as_view(), name='section_list'),
    path(p.join(section, create), SectionCreateApiView.as_view(), name='section_create'),
    path(p.join(section, int_pk), SectionRetrieveApiView.as_view(), name='section_detail'),
    path(p.join(section, int_pk, update), SectionUpdateApiView.as_view(), name='section_update'),
    path(p.join(section, int_pk, delete), SectionDestroyApiView.as_view(), name='section_delete'),

    # Content urlpatterns
    path(p.join(content), ContentListApiView.as_view(), name='content_list'),
    path(p.join(content, create), ContentCreateApiView.as_view(), name='content_create'),
    path(p.join(content, int_pk), ContentRetrieveApiView.as_view(), name='content_detail'),
    path(p.join(content, int_pk, update), ContentUpdateApiView.as_view(), name='content_update'),
    path(p.join(content, int_pk, delete), ContentDestroyApiView.as_view(), name='content_delete'),

    # Questions urlpatterns
    path(p.join(question), QuestionListApiView.as_view(), name='question_list'),
    path(p.join(question, int_pk), QuestionRetrieveApiView.as_view(), name='question'),
] + router.urls
