from django.test import TestCase
from core.models import CategoryModel, Tags
# Create your tests here.

class CategoryModelTest(TestCase):
    def create_category(self, name='product', slug='product'):
        return CategoryModel.objects.create(name=name, slug=slug)


    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, CategoryModel))
        self.assertEqual(w.__str__(), w.name)

class TagsModelTest(TestCase):
    def create_tags(self, name='tag1'):
        return Tags.objects.create(name=name)

    def test_tag_creation(self):
        t = self.create_tags()
        self.assertTrue(isinstance(t, Tags))
        self.assertEqual(t.__str__(), t.name)

