from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados ={
            'nome': 'Jeremias',
            'email': 'jeremias@hotmail.com',
            'assunto' : 'Meu assunto',
            'mensagem' : 'Minhas mensagem'
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code,302)

    def test_form_invalix(self):
        dados = {
            'nome': 'Jeremias',
            'assunto': 'Meu assunto'
        }

        request = self.client.post(reverse_lazy('index'),data=dados)
        self.assertEquals(request.status_code,200)