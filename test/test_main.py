"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="-1")
    def test_idade_m1(self, _mock_input):
        """Testa se o programa imprime "Impossível!" quando o usuário digita -1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )

    @patch("builtins.input", return_value="0")
    def test_idade_0(self, _mock_input):
        """
        Testa se o programa imprime "Você não pode dirigir um carro."
        quando o usuário digita 0
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )

    @patch("builtins.input", return_value="17")
    def test_idade_17(self, _mock_input):
        """
        Testa se o programa imprime "Você não pode dirigir um carro."
        quando o usuário digita 17
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )

    @patch("builtins.input", return_value="18")
    def test_idade_18(self, _mock_input):
        """
        Testa se o programa imprime "Essa idade é cheia de mudanças!"
        quando o usuário digita 18
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )

    @patch("builtins.input", return_value="20")
    def test_idade_20(self, _mock_input):
        """
        Testa se o programa imprime "Não esqueça de votar na próxima eleição."
        quando o usuário digita 20
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )

    @patch("builtins.input", return_value="65")
    def test_idade_65(self, _mock_input):
        """
        Testa se o programa imprime "Essa idade é cheia de mudanças!"
        quando o usuário digita 65
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )

    @patch("builtins.input", return_value="70")
    def test_idade_70(self, _mock_input):
        """Testa se o programa imprime "Vá descansar." quando o usuário digita 70"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn(
            "Você não pode dirigir um carro.", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "Não esqueça de votar na próxima eleição.",
            captured_output.getvalue().strip(),
        )
        self.assertIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn(
            "Essa idade é cheia de mudanças!", captured_output.getvalue().strip()
        )
