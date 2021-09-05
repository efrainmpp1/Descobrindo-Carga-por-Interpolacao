#importamos as duas bibliotecas necessarias
import numpy as np
import matplotlib.pyplot as plt

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

# Coleta 7 valores entre o intervalo todo da planilha

m = [2 ,  10 , 20 , 30 , 39 , 52 ,64]
carga8_8 = [ 0.373 , 50.014 , 411.9 , 1422 , 3226 ,7747 ,14416 ]
carga10_9 = [0.52  , 70.608 , 578.60 , 2010 , 4531 ,10885 ,20300 ]
carga12_9 = [0.628  , 85.317 , 696.30 , 2403 , 5443 ,13092 ,24320]
'''
#Coletando 7 valores de M que estejam proximos do valor estudado
m = [18 , 20 , 22 , 24 , 27 , 30 , 33 , 36 , 39 ]
carga8_8 = [289.3 , 411.9 , 559 , 711 , 1049 , 1422 , 1932 , 2481 , 3226 ]
carga10_9 = [411.9 , 578.6 , 784.5 , 1000 , 1487 , 2010 , 2716 , 3491 , 4531]
carga12_9 = [490.3 , 696.3 , 941.4 , 1196 , 1775 , 2403 , 3266 , 4197 , 5443]
'''
#Pede um modelo desejado e aplica a interpolação no ponto 
valor = int(input("Digite um Modelo desejado"))
teste = interpolacaoLagrange(valor , m , carga8_8)
teste2 = interpolacaoLagrange(valor , m , carga10_9)
teste3 = interpolacaoLagrange(valor , m , carga12_9)
print("Carga para M", valor)
print( "Classe 8.8 é " , teste)
print("Classe 10.9 é " ,teste2)
print("Classe 12.9 é " ,teste3)

# Intervalo de valores m a ser estudado
mReal = np.linspace(2, 64, 50) 
# utilizamos a função da interpolação para aplicar nos inumeros valores do intervalo estudado
c_8 = interpolacaoLagrange(mReal, m, carga8_8)
c_10 = interpolacaoLagrange(mReal, m, carga10_9)
c_12 = interpolacaoLagrange(mReal, m, carga12_9)

# Plotando as curvas de cada classe estudada
plt.plot(mReal , c_8 , label='8.8', linewidth=3 , color = 'b')
plt.plot(mReal , c_10 , label='10.9', linewidth=3 , color = 'r')
plt.plot(mReal , c_12 , label='12.9', linewidth=3 , color = 'g')

# Plotando uma linha vertical traçada no valor do modelo desejado
plt.axvline(x= valor, ymin=0, ymax=1000 , color = 'y')

#Colocando as informações no grafico
plt.title("Gráfico Carga por Tipo M de parafuso")
plt.ylabel('Carga (Nm)')
plt.xlabel('Tipo M')
plt.legend()

#Mostrar meu plot
plt.show()

input()