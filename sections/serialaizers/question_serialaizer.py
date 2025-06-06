from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Question, Section



class QuestionSectionSerializer(ModelSerializer):
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'question_section')



class QuestionSerializer(QuestionSectionSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_section', 'question')
