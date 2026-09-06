# Programa - Calculadora de Consumo Elétrico Inteligente
# Autor: Luis Gustavo dos Santos

# Entrada
Aparelho = input("Nome do aparelho: ")    
Potência = float(input("Digite a potência do aparelho (em watts): "))
Horas_dia = float(input("Digite a quantidade de horas de uso diário: "))

# Processamento
tarifa_kwh = 0.75
consumo_mensal = (Potência * Horas_dia * 30) / 1000 

# Saída
print(f"\nAparelho: {Aparelho}")
print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh/mês") 
print(f"Custo mensal estimado: R${consumo_mensal * tarifa_kwh:.2f}")    
