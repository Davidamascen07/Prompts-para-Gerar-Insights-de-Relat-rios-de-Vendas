import pandas as pd

# Carregar o arquivo CSV
file_path = 'C:/projeto/dio desafio/criando-prompts-inteligentes/data/processed_data/Meganium_Sales_data cvs.csv'

# Tentar ler o CSV com o delimitador correto (no caso ';')
sales_data = pd.read_csv(file_path, delimiter=';')

# Exibir as primeiras linhas e as colunas para verificar a estrutura dos dados
print("Primeiras linhas do dataset:")
print(sales_data.head())

# Verificar os nomes das colunas para garantir que tudo esteja correto
print("\nNomes das colunas:")
print(sales_data.columns)

# Agrupar os dados por 'delivery_country' e calcular total de quantidade e total de vendas
summary_by_country = sales_data.groupby('delivery_country').agg(
    total_quantity=('quantity', 'sum'),
    total_sales=('total_price', 'sum')
).reset_index()

# Ordenar o relatório pela quantidade total de forma decrescente
summary_by_country_sorted = summary_by_country.sort_values(by='total_quantity', ascending=False)

# Exibir o resumo final
print("\nRelatório Resumido por País de Entrega (Ordenado por Quantidade Total):")
print(summary_by_country_sorted)

# Salvar o relatório gerado em um arquivo CSV
output_file_path = 'C:/projeto/dio desafio/criando-prompts-inteligentes/data/scrips_data/relatorio_por_pais.csv'
summary_by_country_sorted.to_csv(output_file_path, index=False)

# Caso prefira exportar para Excel:
output_excel_path = 'C:/projeto/dio desafio/criando-prompts-inteligentes/data/scrips_data/relatorio_por_pais.xlsx'
summary_by_country_sorted.to_excel(output_excel_path, index=False)

print(f"\nRelatório gerado e salvo em:\n- CSV: {output_file_path}\n- Excel: {output_excel_path}")
