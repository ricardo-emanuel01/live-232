"""
Uma introdução a testes
3A --> Arrange, Act, Assert

Utilizando uma abordagem simplificada pra atuar com unittest e coverage
"""

"""
input é uma função python já testada e funcional, portanto nossos testes
não devem focar nessa parte do código e sim no que pode haver um erro
de implementação propriamente dito, que no nosso caso seria a função de
conversão.
"""
temperatura = input(
    'Digite uma temperatura em graus Fahrenheit para ser convertida para Celsius: '
)

temperatura_convertida = ((float(temperatura) - 32) / 9) * 5

print(
    f'{temperatura} graus Fahrenheit é igual '
    f'a {round(temperatura_convertida, 2)} graus Celsius!'
)
