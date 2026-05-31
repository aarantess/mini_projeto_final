import pandas as pd
import os

# --- CONFIGURAÇÃO DE AMBIENTE ---
# Definindo caminhos de forma dinâmica para evitar erros de diretório
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_entrada = os.path.join(diretorio_atual, "Base Varejo.csv")
arquivo_saida = os.path.join(diretorio_atual, "df_limpo.csv")

# =========================================================
# SPRINT 1: CARREGAMENTO E EXPLORAÇÃO
# =========================================================
# Lendo a base com separador ';' conforme identificado na análise initial.
df = pd.read_csv(arquivo_entrada, sep=';')

# Removendo colunas fantasmas (Unnamed) que surgem de delimitadores extras no CSV
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(f"--- RELATÓRIO INICIAL ---")
print(f"Total de registros lidos: {len(df)}")
print(f"Colunas identificadas: {df.columns.tolist()}")
print("\nTipos de dados detectados:\n", df.dtypes)
print("-" * 30)

# =========================================================
# SPRINT 2: PADRONIZAÇÃO DE TIPOS (REGRAS DE NEGÓCIO)
# =========================================================
# REGRA OBRIGATÓRIA: Transformar a coluna DATA para datetime
df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True, errors='coerce')

# Convertendo IDs para string para evitar operações matemáticas acidentais
colunas_id = ['CO_ID', 'CL_ID', 'PR_ID']
df[colunas_id] = df[colunas_id].astype(str)

# Padronizando textos para evitar duplicatas por diferença de caixa (Ex: Alimentos vs alimentos)
df['PR_CAT'] = df['PR_CAT'].str.upper().str.strip()

# =========================================================
# SPRINT 3: TRATAMENTO DE DADOS (NULOS E DUPLICATAS)
# =========================================================
print(f"--- PROCESSO DE LIMPEZA ---")

# Lógica Condicional (If/Else) para Categorias conforme requisito de avaliação
# Usamos uma função lambda para preencher vazios ou erros como "Sem Categoria"
df['PR_CAT'] = df['PR_CAT'].apply(lambda x: "Sem Categoria" if pd.isna(x) or x == "#N/D" else x)

# Validação de Regra de Negócio: O código da compra (CO_ID) deve ser válido
# De acordo com o dicionário, são números de nota fiscal
df = df[df['CO_ID'].str.isnumeric()]

# Removendo duplicatas exatas para não inflar os números de vendas
total_antes = len(df)
df = df.drop_duplicates()

print(f"Registros duplicados removidos: {total_antes - len(df)}")

# Removendo linhas onde o nome do produto é nulo (dado crítico)
df = df.dropna(subset=['PR_NOME'])

print(f"Base final após limpeza: {len(df)} registros.")
print("-" * 30)

# =========================================================
# SPRINT 4: MÉTRICAS ESTATÍSTICAS (CL_FHL)
# =========================================================
print(f"--- PERFIL DOS CLIENTES (FILHOS) ---")
# Calculando métricas da coluna de número de filhos
col_filhos = df['CL_FHL'].dropna()

print(f"Contagem Total de registros: {col_filhos.count()}")
print(f"Média de filhos: {col_filhos.mean():.2f}")
print(f"Mediana: {col_filhos.median()}")
print(f"Moda: {col_filhos.mode()}")
print(f"Desvio Padrão: {col_filhos.std():.2f}")
print(f"Valor Máximo: {col_filhos.max()} | Mínimo: {col_filhos.min()}")

# =========================================================
# SPRINT 5: ANÁLISE DE AGRUPAMENTOS
# =========================================================
print(f"\n--- INSIGHTS DE VENDAS ---")

# Agrupamento 1: Quais categorias mais vendem?
vendas_por_cat = df.groupby('PR_CAT').size().sort_values(ascending=False)
print("Volume por Categoria:\n", vendas_por_cat)

# Agrupamento 2: Comportamento por Gênero
vendas_por_genero = df['CL_GENERO'].value_counts(normalize=True) * 100
print("\nParticipação por Gênero (%):\n", vendas_por_genero.round(2))

# =============================================================================
# SPRINT 6: RELATÓRIO FINAL E INSIGHTS (CONCLUSÃO)
# =============================================================================
print("\n" + "="*60)
print("                RELATÓRIO DE INSIGHTS DO PROJETO                ")
print("="*60)

# Tópicos baseados na análise da base limpa de 733.447 registros
print(f"""
1. LIDERANÇA DE CATEGORIA:
   A categoria 'ALIMENTOS' é o principal motor de vendas, com 384.197 itens,
   representando aproximadamente 52,38% do volume total da base tratada.

2. PERFIL FAMILIAR DO CLIENTE:
   A maioria absoluta dos clientes não possui filhos (Moda e Mediana = 0),
   embora a média seja de 1,15 filhos devido à dispersão dos dados.

3. PARTICIPAÇÃO POR GÊNERO:
   O público feminino (F) possui uma participação ligeiramente superior,
   com 52,14% das compras, contra 47,86% do público masculino (M).

4. EFICIÊNCIA DO PROCESSO ETL:
   A limpeza de dados foi crítica para o BI, removendo 96.553 duplicatas
   (11,63% da base original), evitando uma inflação artificial nos números.

5. INTEGRIDADE DE CATEGORIZAÇÃO:
   O tratamento de erros e nulos (como '#N/D') permitiu recuperar e
   padronizar 3.228 registros sob a etiqueta 'Sem Categoria'.

6. QUALIDADE DA BASE:
   Optou-se pela remoção de registros sem nome de produto para garantir
   que a análise de mix de produtos fosse baseada apenas em dados íntegros.
""")
print("="*60)

# =========================================================
# SPRINT 6: FINALIZAÇÃO
# =========================================================
# Exportando a base tratada para uso posterior em BI
df.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')
print(f"\nArquivo df_limpo exportado com sucesso!")