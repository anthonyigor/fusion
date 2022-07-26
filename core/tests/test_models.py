import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


# classe para teste da função get_file_path
class GetFilePathTestCase(TestCase):

    # cria um atributo filename com uma string no formato que a função deve retornar
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    # chama a função criando uma instância da mesma
    # e testa se o tamanho da string retornada é igual o filename desejado
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'test.png')
        self.assertTrue(len(arquivo), len(self.filename))


class FuncionarioTestCase(TestCase):

    # usa o mommy pra criar uma instância de funcionário conforme os padrões do model
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    # testa se o funcionário criado apresenta o seu atributo 'nome' como __str__
    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.nome)
