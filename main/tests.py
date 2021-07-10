from django.test import TestCase


class ViewsTestCases(TestCase):

    def check(self, data):
        response = self.client.post('/result', data)
        self.assertEqual(response.status_code, 200)

    def test_homepage_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_result_without_links_post(self):
        data = {'last_name': 'Цветков', 'first_name': 'Максим'}
        self.check(data)

    def test_result_github_post(self):
        data = {'last_name': 'Цветков', 'first_name': 'Максим', 'site_1': 'https://github.com/KsamNole'}
        self.check(data)

    def test_result_habr_post(self):
        data = {'last_name': 'Цветков', 'first_name': 'Максим', 'site_1': 'https://habr.com/ru/users/pureacetone/'}
        self.check(data)

    def test_result_linkedin_post(self):
        data = {'last_name': 'Цветков', 'first_name': 'Максим',
                'site_1': 'https://www.linkedin.com/in/arkadii-aristov-a9559288/'}
        self.check(data)

    def test_result_codeforces_post(self):
        data = {'last_name': 'Цветков', 'first_name': 'Максим', 'site_1': 'https://codeforces.com/profile/Um_nik'}
        self.check(data)
