from flask import Flask
from unittest import TestCase
from app import app
from flask import session
from flask_testing import TestCase
# from forex_python.converter import CurrencyRates, CurrencyCodes
# from forex_python.converter import CurrencyRates, CurrencyCodes


from flask_testing import TestCase


class FlaskTests(TestCase):
    def setUp(self):
       
        self.client = app.test_client()
        app.config['TESTING'] = True

    

    def testing_base_route(self):
        with app.test_client() as client:
        
            response = client.get('/')
            print(response)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/users')


class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    
    def testing_user_indv_route(self):
        with app.test_client() as client:
        
            response = client.get('/users/1')
            print(response)
            self.assert_template_used('user_page.html')
            self.assertEqual(response.status_code, 200)

    def testing_user_route(self):
        with app.test_client() as client:
        
            response = client.get('/users')
            print(response)
            self.assert_template_used('user.html')
            self.assertEqual(response.status_code, 200)

    def testing_new_user_route(self):
        with app.test_client() as client:
        
            response = client.get('/users/new')
            print(response)
            self.assert_template_used('new-user-form.html')
            self.assertEqual(response.status_code, 200)

    def testing_edit_user_route(self):
        with app.test_client() as client:
        
            response = client.get('/users/1/edit')
            print(response)
            self.assert_template_used('user_edit.html')
            self.assertEqual(response.status_code, 200)

    def testing_new_post_route(self):
        with app.test_client() as client:
        
            response = client.get('/users/1/posts/new')
            print(response)
            self.assert_template_used('new_post_page.html')
            self.assertEqual(response.status_code, 200)

    def testing_post_route(self):
        with app.test_client() as client:
        
            response = client.get('/posts/1')
            print(response)
            self.assert_template_used('post-page.html')
            self.assertEqual(response.status_code, 200)

    def testing_post_edit_route(self):
        with app.test_client() as client:
        
            response = client.get('/posts/1/edit')
            print(response)
            self.assert_template_used('post-edit.html')
            self.assertEqual(response.status_code, 200)

    def testing_post_delete_route(self):
        with app.test_client() as client:
        
            response = client.get('/posts/1/delete')
            print(response)
            self.assert_template_used('post-delete.html')
            self.assertEqual(response.status_code, 200)

    def testing_tag_route(self):
        with app.test_client() as client:
        
            response = client.get('/tags')
            print(response)
            self.assert_template_used('tag_page.html')
            self.assertEqual(response.status_code, 200)

    def testing_single_tag_route(self):
        with app.test_client() as client:
        
            response = client.get('/tags/1')
            print(response)
            self.assert_template_used('tag.html')
            self.assertEqual(response.status_code, 200)

    def testing_tag_edit_route(self):
        with app.test_client() as client:
        
            response = client.get('/tags/1/edit')
            print(response)
            self.assert_template_used('tag_edit.html')
            self.assertEqual(response.status_code, 200)

    def testing_tag_delete_route(self):
        with app.test_client() as client:
        
            response = client.get('/tags/1/delete')
            print(response)
            self.assert_template_used('tag_delete.html')
            self.assertEqual(response.status_code, 200)



    
    
 
    

