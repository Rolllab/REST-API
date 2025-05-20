from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section
from sections.tests.utils import get_admin_user, get_member_user

class SectionTestCase(APITestCase):

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

    # id=2 (В базе данных)
    def test_01_section_create(self):
        data = {
            'title': 'Test Section Create',
            'description': 'Test Description Create'
        }

        response = self.client.post('/section/create/', data=data)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), 'Test Section Create')
        self.assertEqual(response.json().get('description'), 'Test Description Create')

    # id=3 (В базе данных)
    def test_02_section_detail(self):
        response = self.client.get('/section/3/')       # цифра 3 - это потому, что id=3

        # response = self.client.get(f'/section/{self.test_section.id}/')       # цифру 3 можно получить и так

        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Section')
        self.assertEqual(response.json().get('description'), 'Test Description')

    # id=4 (В базе данных)
    def test_03_section_update(self):
        data = {
            'title': 'Test Section Update Put',
            'description': 'Test Section Description Put',
        }

        response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)   # self.test_section.id = 4
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Section Update Put')
        self.assertEqual(response.json().get('description'), 'Test Section Description Put')


    def test_04_section_delete(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        print(response.status_code)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    # id=6
    def test_05_section_list(self):
        response = self.client.get('/section/')
        print(response.json())
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json().get('results')[0]['title'], 'Test Section')

    def test_06_section_create_forbidden(self):
        member = get_member_user()
        response = self.client.post('/users/token/', {'email': member.email, 'password': 'qwerty'})
        access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        data = {
            'title': 'Test Section Create',
            'description': 'Test Description Create'
        }

        response = self.client.post('/section/create/', data=data)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')
