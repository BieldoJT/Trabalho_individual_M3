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


Tarefas

tarefas_concluidas = tabela['Tarefas Concluídas']

total_tarefas_concluidas = soma_informacao(tarefas_concluidas)

media_diaria_tarefas_concluidas =media_informacao(tarefas_concluidas)

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando as barras das horas trabalhadas por dia
plt.bar(dias, tarefas_concluidas, color='pink')

# Adicionando a linha da média diária
plt.axhline(y=media_diaria_tarefas_concluidas, color='purple', linestyle='--', label=f'Média tarefas por dia: {media_diaria_tarefas_concluidas}')

# Adicionando título e rótulos
plt.title('Tarefas por dia')
plt.xlabel('Dias da semana')
plt.ylabel('Tarefas concluidas')

# Adicionando a legenda
plt.legend()

# Rotacionando os rótulos dos dias para melhor visualização
plt.xticks(rotation=45)

# Mostrando o gráfico
plt.tight_layout()
plt.show()

print(f'O total de tarefas concluidas é: {total_tarefas_concluidas}')

Produtividade Diária (Tarefas Concluídas por Hora)

produtividade = round(tarefas_concluidas/horas_trabalhadas,2)*100

media_produtividade =media_informacao(produtividade)

# Criando o gráfico
plt.figure(figsize=(10, 6))

plt.plot(dias,produtividade,color='#a5d141')
plt.axhline(y=media_produtividade, color='purple', linestyle='--', label=f'Media de Produtividade: {media_produtividade}%')

# Adicionando título e rótulos
plt.title('Produtividade Diária')
plt.xlabel('Dias da semana')
plt.ylabel('Produtividade (%)')
plt.legend()


plt.grid(True)
plt.tight_layout()
plt.show()


Efetividade solução de bugs
Considerando que a correção de bugs também é uma tarefa, podemos ver a efetividade. A efetividade é a relação da quantidade de bugs resolvidos em relação as horas trabalhadas.


efetividade = round(bugs_corrigidos/horas_trabalhadas,2)*100


media_efetividade = media_informacao(efetividade)


fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotando a efetividade
ax1.plot(dias, efetividade, label='Efetividade (%)', color='b')
ax1.axhline(y=media_efetividade, color='r', linestyle='--', label=f'Média de Efetividade {media_efetividade:.2f}%')
ax1.set_xlabel('Dias da semana')
ax1.set_ylabel('Efetividade (%)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Criando um segundo eixo y para as horas trabalhadas
ax2 = ax1.twinx()
ax2.bar(dias, horas_trabalhadas, alpha=0.6, color='g', label='Horas Trabalhadas')
ax2.set_ylabel('Horas Trabalhadas', color='g')
ax2.tick_params(axis='y', labelcolor='g')

fig.tight_layout()
fig.suptitle('Solução de bugs', y=1.03)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


ax1.grid(True)

plt.show()

Correlação entre Horas trabalhadas, Bugs Corrigidos e Tarefas Concluídas



# Calcular a matriz de correlação
corr = tabela[['Horas Trabalhadas', 'Bugs Corrigidos', 'Tarefas Concluídas']].corr()

# Plotar o gráfico de calor da matriz de correlação
plt.figure(figsize=(10, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlação')

plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.show()
