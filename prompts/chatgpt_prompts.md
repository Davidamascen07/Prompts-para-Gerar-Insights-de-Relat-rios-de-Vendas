1. Consolidação de Bases de Dados
"Consolide os dados de vendas de diferentes bases fornecidas por terceiros, garantindo a padronização de colunas (como SKU, invoice_id, quantity, total_price), unificando os formatos de data e moeda e removendo duplicidades. Identifique possíveis inconsistências entre as bases."

2. Transformação de Dados em Informações Relevantes
"Transforme os dados de vendas em insights úteis para a fabricante, incluindo:

Receita total gerada por região e site.
Tendências de vendas por país e por período (mensal e semanal).
Identificação de mercados com maior demanda para priorizar fabricação e estratégias regionais."
"Com base nos dados históricos, crie uma previsão da demanda para cada produto (SKU) por região, ajudando a orientar a produção e o planejamento estratégico da fabricante."

3. Identificação dos Produtos Mais Populares
"Liste os produtos mais populares globalmente (SKU), mostrando:

Quantidade total vendida.
Receita gerada.
Países ou regiões onde esses produtos têm maior aceitação."
"Classifique os produtos por popularidade em cada site e país de entrega, destacando os cinco mais vendidos em cada categoria."

https://chatgpt.com/share/6775afde-593c-8005-b766-09239e0d51d6

4. Otimização do Transporte e Logística
"Calcule o tempo médio de transporte (delivery_time) por país ou região, identifique os maiores atrasos e gargalos logísticos, e sugira estratégias para reduzir esses tempos e melhorar a eficiência."

"Determine o custo médio de transporte por região e avalie quais países ou regiões apresentam maior custo-benefício para otimização logística."

"Com base nos dados, analise a eficiência logística até o momento da venda, incluindo:

Comparação entre o número de pedidos processados e entregues em diferentes regiões.
Identificação de regiões onde a entrega é mais ágil.
Propostas para reduzir custos logísticos e melhorar a rede de distribuição."
5. Insights Gerais das Vendas
"Resuma os principais insights gerais do arquivo CSV, incluindo:
Soma total do valor das vendas (total_price).
Quantidade total de produtos vendidos (quantity).
Número de transações únicas (invoice_id)."
6. Análise de Vendas por Produto, País e Site
"Identifique os produtos mais vendidos (SKU), mostrando o top 5 com:

Quantidade total vendida.
Receita gerada por cada um."
"Calcule a receita total (total_price) por país de entrega (delivery_country)."

"Apresente o número de transações realizadas em cada site (site)."

7. Análise de Descontos
"Quantifique as transações que utilizaram cupons de desconto (discount_coupon)."

"Determine o valor médio dos descontos aplicados e liste os cupons mais utilizados, mostrando suas frequências e o desconto total concedido."

8. Segmentação por Clientes
"Liste os 10 maiores compradores (buyer_name) com base no total de compras (total_price)."

"Quantifique as transações feitas por compradores com menos de 30 anos de idade (considerando buyer_birth_date)."

"Agrupe os compradores por país de entrega (delivery_country), mostrando o total de compras realizadas em cada um."

9. Análise Temporal
"Crie uma análise temporal das vendas diárias com base em date, incluindo:
Um gráfico que mostre a soma de total_price e a quantidade de produtos vendidos.
Identificação dos meses e dias da semana com maior volume de vendas.
Quantificação das transações e receitas totais por mês."

10. Preços e Desempenho
"Determine o preço médio por unidade (unit_price) para cada produto (SKU)."

"Identifique os produtos com os maiores descontos aplicados (discount_value) e suas respectivas quantidades vendidas."

"Analise a correlação entre os preços unitários (unit_price) e as quantidades vendidas (quantity)."

11. Análise de Dados Faltantes ou Inválidos
"Liste todas as linhas do arquivo CSV que possuem valores ausentes ou inválidos."

"Verifique transações com quantity igual a 0 ou com total_price inconsistente com unit_price x quantity e liste os IDs das notas fiscais (invoice_id) com problemas."

12. Relatórios e Visualizações
"Crie uma tabela resumo com as vendas totais (total_price) agrupadas por site (site) e país de entrega (delivery_country)."

"Gere um gráfico de barras com as 5 maiores receitas por produto (SKU)."

"Destaque os 3 principais países de entrega (delivery_country) em termos de quantidade de produtos vendidos."