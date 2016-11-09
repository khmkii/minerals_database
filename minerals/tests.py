from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral

# Create your tests here.


class MineralViewsTest(TestCase):
    def setUp(self):
        self.minerals = Mineral.objects.all()
        self.mineral = Mineral.objects.create(
            name="Unobtaininite",
            luster='Shiny',
            streak='Golden',
            category="Not of this earth",
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, "Macky's Minerals")
        self.assertIn(self.mineral, resp.context['minerals'])

    def test_mineral_view(self):
        resp = self.client.get(reverse('minerals:mineral',
                                       kwargs={'name': self.mineral.name}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals\mineral_detail.html')
        self.assertContains(resp, self.mineral.name)

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['mineral'] in self.minerals)
