import pytest
from ex2.pessoa import Pessoa
from ex2.vista import Vista
from ex2.controlador import Controlador
from ex2.modelo import Modelo


def test_guardar_pessoa_no_modelo():
    modelo = Modelo()
    pessoa = Pessoa("João", 25)

    modelo.guardar(pessoa)

    assert len(modelo.pessoas) == 1
    assert modelo.pessoas[0] == pessoa


def test_vista_perguntar(monkeypatch):
    inputs = iter(["Maria", "40"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    vista = Vista()
    pessoa = vista.perguntar()

    assert pessoa.nome == "Maria"
    assert pessoa.idade == 40


def test_controlador(monkeypatch):
    inputs = iter(["Carlos", "35"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controlador = Controlador()

    pessoa = controlador.modelo.pessoas[0]

    assert len(controlador.modelo.pessoas) == 1
    assert pessoa.nome == "Carlos"
    assert pessoa.idade == 35


def test_pessoa():
    p = Pessoa("Alice", 30)

    assert p.nome == "Alice"
    assert p.idade == 30
    assert str(p) == "Pessoa(nome=Alice, idade=30)"
