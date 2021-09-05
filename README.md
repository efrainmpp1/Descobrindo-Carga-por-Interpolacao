# Problema
Para saber qual carga é suportada por um parafuso, utiliza-se uma planilha com os valores noramtizados observando o modelo do parafuso e suas classes de qualidade conforme norma
DIN 267, da para acessar a tabela clicando AQUI.Entretanto nem todos os modelos de parafuso estão tabelados, e em nosso estudo estavamos buscando as configurações de um parafuso M32 na qual não se encontra.Para isso, criamos um algoritmo em Python para através de dados coletados, consiga projetar uma função e retornar valores de carga de acordo com o modelo desejado.

## Usando Interpolação de Lagrange no Python
Com os dados oficiais da tabela, utilizaremos da Interpolação de Lagrange para achar os valores de carga de acordo com o polinomio de Lagrange traçado pelos dados oferecidos.
A formula do Polinimoio de Lagrange é dada pela seguinte imagem:

![Lagrange](http://2.bp.blogspot.com/-Q1sDUtfTd9c/VW3Qd2cqjmI/AAAAAAAAAdY/a3jUwqMWJWY/s1600/polinomio%2Binterpolador%2Blagrange%2Bgrau%2Bn.png) 

Representando essa expressao para o Python, definimos uma função que recebe como parametro um ponto e retorna  o polinomio aplicado nesse ponto.

```python
#Definindo nossa função Interpolação de Lagrange
def interpolacaoLagrange(a,x,y):
  npontos = len(x)
  S = 0
  for i in range(0,npontos):
    L = 1
    for j in range(0,npontos):
      if j != i :
        L = L*(a - x[j]) / (x[i] - x[j])
    S = S + (y[i]*L)
  return S
```

## Gráficos
Após usar a função Interpoladora de Lagrange para retornar varios valores de carga em vetores categorizados por classe do material, plotamos os Gráficos e obtivemos os seguintes resultados para o caso geral, ou seja, utilizando de alguns valores dentre os modelos M2 até M64 :

![GraficoGeral]()

Essa é uma forma de analisar como o grafico se comporta, mas para ter resultados mais precisos para o parafuso estudado, coletamos os dados próximos ao modelo desejado(de M18 até M39).Com isso plotamos o grafico:

![GraficoSeleto]()

## Resultados
Com uma aplicação da função Interpolação no nosso modelo, printamos 3 resultados que estãp referentes as 3 classes de material do estudo.
```
Carga para M 32
Classe 8.8 é  1737.8607589319377
Classe 10.9 é  2445.6397763852565
Classe 12.9 é  2935.196741771693
```

## Ambiente Virtual
Nesse repositório, criei um ambiente e rodei o código nele.Nele vem instalado as bibliotecas de Matplotlib e Numpy.

