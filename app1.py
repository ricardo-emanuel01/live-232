"""
É possível testar nossas funções mais simples utilizando o módulo
doctest da biblioteca padrão do Python.
Este módulo lê a docstring da função, da classe, do método e etc
testa no interpretador Python e diz se a saída real é exatamente
igual à saída esperada, por isso acrescentei a casa decimal na saída
Caso fosse uma comparação do número esperado com o número real não
seria necessário representar a casa decimal, pois 32.0 == 32 no Python.
"""

"""
É possível utilizar o doctest da seguinte forma:
> python -m doctest <file_name>.py

Para conseguirmos o coverage é necessário instalar o coverage com
algum gerenciador de pacotes:
> pip install coverage

E então é possível executar:
> python -m coverage run -m doctest <file_name>.py
esse comando gera um arquivo .coverage na pasta, caso alguem queira
um relatório de coverage é possível com o comando:
> coverage report
E pra conseguir um .html para verificar exatamente onde os testes estão cobrindo
e onde não estão:
> coverage html
E abrir html.index em algum navegador.
"""

def conversaoF_C(temperatura: float) -> float:
    """
    Examples
        >>> conversaoF_C(32)
        0.0

        >>> conversaoF_C(-40)
        -40.0
    """
    return round((((temperatura - 32) / 9) * 5), 2)


def conversaoC_F(temperatura: float) -> float:
    """
    Examples
        >>> conversaoC_F(-40)
        -40.0

        >>> conversaoC_F(0)
        32.0
    """
    return round((temperatura / 5 * 9 + 32), 2)