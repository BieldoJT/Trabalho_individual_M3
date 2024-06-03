import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#tabela = pd.read_excel('Pasta.xlsx')

data = {
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
    'Horas Trabalhadas': [6, 7, 8, 6, 7, 5, 4],
    'Bugs Corrigidos': [3, 2, 1, 4, 3, 2, 1],
    'Tarefas Concluídas': [5, 4, 6, 4, 5, 3, 2]
}
tabela = pd.DataFrame(data)
tabela

def soma_informacao(info):
  return info.sum()

def media_informacao(info):
  return round(info.mean(),2)

     
Horas trabalhadas

dias = tabela['Dia']
horas_trabalhadas = tabela['Horas Trabalhadas']

#total de horas trabalhadas
total_horas_trabalhadas = soma_informacao(horas_trabalhadas)


#media de horas trabalhadas por dia
media_horas_trabalhadas =  media_informacao(horas_trabalhadas)

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando as barras das horas trabalhadas por dia
plt.bar(dias, horas_trabalhadas, color='skyblue')

# Adicionando a linha da média diária
plt.axhline(y=media_horas_trabalhadas, color='red', linestyle='--', label=f'Média Diária {media_horas_trabalhadas} horas')

# Adicionando título e rótulos
plt.title('Horas trabalhadas por dia')
plt.xlabel('Dias da semana')
plt.ylabel('Horas trabalhadas')

# Adicionando a legenda
plt.legend()

# Rotacionando os rótulos dos dias para melhor visualização
plt.xticks(rotation=45)

# Mostrando o gráfico
plt.tight_layout()
plt.show()
print(f'O total de horas trabalhadas é :{total_horas_trabalhadas} horas')

Bugs

bugs_corrigidos = tabela['Bugs Corrigidos']

total_bugs_corrigidos = soma_informacao(bugs_corrigidos)

media_diaria_bugs_corrigidos = media_informacao(bugs_corrigidos)

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando as barras das horas trabalhadas por dia
plt.bar(dias, bugs_corrigidos, color='orange')

# Adicionando a linha da média diária
plt.axhline(y=media_diaria_bugs_corrigidos, color='blue', linestyle='--', label=f'Média de Correção por dia: {media_diaria_bugs_corrigidos} correções')

# Adicionando título e rótulos
plt.title('Bugs corrigiddos por dia')
plt.xlabel('Dias da semana')
plt.ylabel('Bugs Corrigidos')

# Adicionando a legenda
plt.legend()

# Rotacionando os rótulos dos dias para melhor visualização
plt.xticks(rotation=45)

# Mostrando o gráfico
plt.tight_layout()


plt.show()

print(f'O total de bugs corrigidos é: {total_bugs_corrigidos}')
