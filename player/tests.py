from django.test import TestCase, Client
from .models import PlayerRun

# Create your tests here.
class PlayerRunTestCase(TestCase):

    def test_kph_returns_correctly(self):
        pr = PlayerRun(
            distance = 30,
            time = 120,
            mass = 100
        )
        pr.save()
        self.assertEqual(pr.kph, 15)

    def test_calories_returns_correclty(self):
        pr = PlayerRun(
            distance = 30,
            time = 120,
            mass = 100
        )
        pr.save()
        self.assertEqual(pr.calories, 39.16406700000001)


class PlayerRunViewsTestCase(TestCase):
    def test_index_gets_all_player_runs(self):
        pr = PlayerRun(distance=10, time=10, mass=100)
        pr.save()
        number_of_prs = PlayerRun.objects.count()

        c = Client()
        response = c.get('/')
        runs = response.context['runs']
        self.assertEqual(len(runs), number_of_prs)

    def test_save_get_will_get_the_save_screen(self):
        c = Client()
        response = c.get('/save')
        self.assertEqual('player/save.html', response.templates[0].name)

    def test_save_post_will_add_a_new_pr(self):
        number_of_prs_before = PlayerRun.objects.count()
        c = Client()
        response = c.post(
            '/save',
            {'distance': '10', 'time': '10', 'mass': '100'}
        )
        number_of_prs_after = PlayerRun.objects.count()
        self.assertEqual(number_of_prs_before + 1, number_of_prs_after)
