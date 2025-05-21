from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section, Content
from sections.tests.utils import get_admin_user, get_member_user



class ContentTestCase(APITestCase):

    # id=1 (В базе данных)
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title='Test Section',
            description='Test Description',
        )

        self.test_content = Content.objects.create(
            section=self.test_section,
            title='Test Title',
            content='Test Content'
        )

    def test_07_content_create(self):
        data = {
            'section': self.test_section.id,
            'title': 'Test Title Create',
            'content': 'Test Content Create',
        }
        response = self.client.post('/content/create/', data=data)
        # print(response.status_code)
        # print(response.json())
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), 'Test Title Create')
        self.assertEqual(response.json().get('content'), 'Test Content Create')

    def test_08_content_detail(self):
        response = self.client.get(f'/content/{self.test_content.id}/')
        # print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Title')
        self.assertEqual(response.json().get('content'), 'Test Content')

    def test_09_content_update(self):
        data = {
            'section': self.test_section.id,
            'title': 'Test Title Update Patch'
        }
        response = self.client.patch(f'/content/{self.test_content.id}/update/', data=data)
        # print(response.status_code)
        # print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Title Update Patch')

    def test_10_content_delete(self):
        response = self.client.delete(f'/content/{self.test_content.id}/delete/')
        # print(response.status_code)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_11_content_list(self):
        response = self.client.get('/content/')
        # print(response.status_code)
        # print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json().get('results')[0]['title'], 'Test Title')

    def test_12_content_create_forbidden(self):
        member = get_member_user()
        response = self.client.post('/users/token/', {'email': member.email, 'password': 'qwerty'})
        access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        data = {
            'section': self.test_section.id,
            'title': 'Test Title Create',
            'content': 'Test Content Create',
        }

        response = self.client.post('/content/create/', data=data)
        # print(response.status_code)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')
