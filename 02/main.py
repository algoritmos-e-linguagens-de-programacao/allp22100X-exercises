import sys

from a.problem_a import solution

# Leia a entrada padrão (stdin)
input_data = sys.stdin.read()

# Processamento adicional
lines = input_data.splitlines()
num_lines = len(lines)

# Exibe o conteúdo e o número de linhas
print("Conteúdo do arquivo:")
print(input_data)
print(f"Número de linhas: {num_lines}")
