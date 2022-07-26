from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.views import IndexView


class IndexViewTestCase(TestCase):

    # cria dados válidos para um form teste
    def setUp(self):
        self.dados = {
            'nome': 'Luka Magic',
            'email': 'luka77@gmail.com',
            'assunto': 'qualquer assunto',
            'mensagem': 'qualquer mensagem',
        }

        # cria um cliente http
        self.cliente = Client()

    # faz uma requisição http por meio do cliente e passa os dados criados
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)  # testa se o status da requisição é igual a 302 (redirecionamento)

    def test_form_invalid(self):

        # cria dados incompletos para um form test
        dados = {
            'nome': 'Luka Magic',
            'email': 'luka77@gmail.com',
            'assunto': 'qualquer assunto',
        }

        # faz uma requisição http por meio do cliente e passa os dados criados
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)  # testa se o status da requisição é igual a 200 (ou seja, form inválido)
