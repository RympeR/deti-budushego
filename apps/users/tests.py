from django.test import TestCase
from .models import MenuCategory


class MenuCategoryTestCase(TestCase):
    def setUp(self):
        parent_menu = MenuCategory.objects.create(
            name='test',
            name_ukr='test_ukr',
            link='https://gooogle.com',
            icon_class='test',
            display=True
        )
        self.child_menu = MenuCategory.objects.create(
            parent=parent_menu,
            name='test_child',
            name_ukr='test_child_ukr',
            link='https://gooogle.com',
            icon_class='test',
            display=True
        )

    def test_parent_name(self):
        self.assertEqual(self.child_menu.parent.name, 'test')
