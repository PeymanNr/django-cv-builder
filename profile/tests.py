import unittest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from profile.models import Skill


class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test2024432',
                                             password='<PASSWORD>')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = self.client.post('/user/profile/skills/',
                                    {'name': 'skilltesdt1'}, format='json')
        self.skill_id = response.data['id']

    def tearDown(self):
        self.user.delete()
        skill = Skill.objects.get(id=self.skill_id)
        skill.delete()

    def test_profile_get(self):
        response = self.client.get('/user/profile/')
        self.assertEqual(response.status_code, 200)

        self.assertIn('user', response.data)
        self.assertEqual(response.data['user'], 'test2024432')

    def test_profile_patch(self):
        response = self.client.patch('/user/profile/', {'bio': 'New bio'},
                                     format='json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['bio'], 'New bio')

    def test_profile_put(self):
        response = self.client.put('/user/profile/',
                                   {
                                       'bio': 'New bio',
                                       'skills': [self.skill_id],
                                       'job_experience': 'Software Engineer',
                                       'education': 'Azad',
                                       'certificates': 'Certificate'
                                   }, format='json')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['bio'], 'New bio')
        self.assertEqual(response.data['skills'], [self.skill_id])
        self.assertEqual(response.data['job_experience'], 'Software Engineer')
        self.assertEqual(response.data['education'], 'Azad')
        self.assertEqual(response.data['certificates'], 'Certificate')
