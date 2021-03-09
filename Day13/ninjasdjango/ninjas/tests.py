from django.test import TestCase
from django.urls import reverse
from .models import Developer, Skill
from .views import level

class DeveloperModelTests(TestCase):
    def test_200_index(self):
        url = reverse('ninjas:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_200_details(self):
        dev = Developer(Name='Michael', Experience=9, Country='Australia')
        dev.save()
        url = reverse('ninjas:details', args=(dev.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_404_details(self):
        url = reverse('ninjas:details', args=(1,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_all_dev(self):      
        dev = Developer(Name='Michael', Experience=9, Country='Australia')
        dev.save()
        dev_list = Developer.objects.all()
        assert len(dev_list) == 1

class SkillModelTests(TestCase):

    def test_create_skill(self):
        dev = Developer(Name='Michael', Experience=9, Country='Australia')
        dev.save()
        skill = dev.skill_set.create(Skill_name='Hadoop', Skill_level="Beginner")
        assert skill.Skill_name == 'Hadoop'

    def test_skill_of_dev(self):
        dev = Developer(name='Michael', Experience=9, Country='Australia')
        dev.save()
        dev.skill_set.create(Skill_name='Hadoop', Skill_level="Beginner")
        dev.skill_set.create(Skill_name='Apache Spark', Skill_level="Beginner")
        dev_skill_list = dev.skill_set.all()
        assert len(dev_skill_list) == 2

    def test_level_up(self):
        dev = Developer(Name='Michael', Experience=1, Country='Australia')
        dev.save()
        dev.skill_set.create(Skill_name='Hadoop', Skill_level="Beginner")
        dev.skill_set.create(Skill_name='Apache Spark', Skill_level="Beginner")
        select = dev.skill_set.get(pk=1)
        select.Skill_level = "Advanced"
        select.save()
        skill = dev.skill_set.all() 
        assert skill[0].Skill_level == "Advanced"
