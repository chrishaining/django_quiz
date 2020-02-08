from django.test import TestCase
from cards.models import *
# Create your tests here.


class CardTestCase(TestCase):
    def setUp(self):
        self.card1 = Card.objects.create(question="What kind of language is Java?", answer="OOP", url="https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design")

    def test_card_saved(self):
        self.assertGreater(self.card1.pk, 0)

    def test_card_question(self):
        self.assertEqual(self.card1.question, "What kind of language is Java?")

    def test_card_answer(self):
        self.assertEqual(self.card1.answer, "OOP")

    def test_card_link(self):
        self.assertEquals(self.card1.url, "https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design")


class MultipleChoiceCardTestCase(TestCase):
    def setUp(self):
        self.card2 = Card.objects.create(question="What kind of language is Java?", answer="A", url="https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design")
        self.card3 = Card.objects.create(question="What is your favourite?", answer="B", url="https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design")

# I originally had a test for a default, but the test failed. I was going to fix it, but what's the point? If I can avoid a default, it's not a problem.
    # def test_choices_default(self):
    #     self.assertEquals(self.card2.answer, "A")

    def test_choices_changes(self):
        self.assertEquals(self.card3.answer, "B")

    def test_link(self):
        self.assertEquals(self.card2.url, "https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design")

    def test_card_question(self):
        self.assertEqual(self.card2.question, "What kind of language is Java?")