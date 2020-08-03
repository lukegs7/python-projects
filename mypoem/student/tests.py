from django.test import TestCase

# Create your tests here.


from django.test import TestCase, Client
from .models import Student
from django.test import Client


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name='the5fire', sex=1, email='nobody@the5fire.com', profession='程序员', qq='123123',
                               phone='123123')

    def test_create_and_sex_show(self):
        student = Student.objects.create(name='huying', sex=1, email='nobody@dd.com', profession='程序员',
                                         qq='3333', phone='2222')
        self.assertEqual(student.sex_show, '男', '性别字段和内容不一致')

    def test_filter(self):
        Student.objects.create(name='huying', sex=1, email='nobody@dd.com', profession='程序员',
                               qq='3333', phone='2222')
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在名称为{}的一条记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        print(response.content)
        self.assertEqual(response.status_code, 200, 'status code must be 200！')

    def test_post_student(self):
        client = Client()
        data = dict(name='test_for_post',
                    sex=1,
                    email='333@dd.com',
                    profession='程序员',
                    qq='3333',
                    phone='3322')
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302')
        response = client.get('/')
        print(response.content)
        self.assertEqual(b'test_for_post' in response.content, 'response content must contain `test_for_post`')
