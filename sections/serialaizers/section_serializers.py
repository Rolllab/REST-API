from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, Content
from sections.serialaizers.content_serializers import ContentSectionSerializer


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    section_content_title = SerializerMethodField()

    @staticmethod
    def get_section_content_title(section):
        return ContentSectionSerializer(Content.objects.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'section_content_title')