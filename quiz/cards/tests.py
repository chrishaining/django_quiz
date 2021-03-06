from django.test import TestCase
from cards.models import *
# Create your tests here.


class CardTestCase(TestCase):
    def setUp(self):
        self.card1 = Card.objects.create(question="What kind of language is Java?", answer="OOP")

    def test_card_saved(self):
        self.assertGreater(self.card1.pk, 0)

    def test_card_question(self):
        self.assertEqual(self.card1.question, "What kind of language is Java?")

    def test_card_answer(self):
        self.assertEqual(self.card1.answer, "OOP")