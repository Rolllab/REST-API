from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content, Question
from sections.permissions import IsModerator, IsSuperuser
from sections.serialaizers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serialaizers.content_serializers import ContentSerializer, ContentSectionSerializer, \
    ContentListSerializer
from sections.serialaizers.question_serialaizer import QuestionSectionSerializer, QuestionSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator, QuestionPaginator



class SectionListApiView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = SectionPaginator



class SectionCreateApiView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)



class SectionRetrieveApiView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, )



class SectionUpdateApiView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)



class SectionDestroyApiView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)



class ContentListApiView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = SectionContentPaginator



class ContentCreateApiView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)



class ContentRetrieveApiView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, )



class ContentUpdateApiView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)



class ContentDestroyApiView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)



class QuestionListApiView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = QuestionPaginator



class QuestionRetrieveApiView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        answer = [question.answer for question in Question.objects.all()]
        answer = answer[self.kwargs.get('pk') -1].strip().lower()
        user_answer = request.data.get('user_answer').strip().lower()
        is_correct = user_answer == answer
        return Response({"is_correct": is_correct})
