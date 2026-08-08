# miniguia-estudos-notebooklm-telemetria
Caderno Temático criado com IA sobre Análise de Telemetria no iRacing usando Python.
# Caderno Temático: Análise de Telemetria no Automobilismo Virtual com Python

Este repositório contém um Miniguia de Estudos focado em **Fundamentos de Análise de Telemetria no Automobilismo Virtual (iRacing) utilizando Python**. O material foi estruturado e refinado utilizando o **NotebookLM** da Google como ferramenta de aprendizagem ativa, parte de um Desafio de Projeto da plataforma DIO.

## Contexto e Objetivos
Como entusiasta de simulação de corridas (sim racing) e usuário ativo do iRacing com cockpit próprio, meu objetivo com este caderno foi unir uma paixão pessoal aos meus estudos de desenvolvimento de software. 

Os objetivos principais de estudo foram:
- Entender como os dados físicos (telemetria) são gerados e extraídos do simulador iRacing.
- Compreender a lógica de estruturação de dados de alta frequência.
- Identificar como a linguagem **Python** (especificamente com a biblioteca Pandas) pode ser aplicada para limpar, processar e analisar esses dados, simulando a atuação de um Engenheiro de Dados de uma equipe real de automobilismo.

## Curadoria de Fontes
Para treinar a Inteligência Artificial, realizei a curadoria de 4 fontes abrangendo tanto a teoria do automobilismo quanto a engenharia de software:

1. **[Introdução ao Pandas no Python (Hashtag Treinamentos)](https://www.hashtagtreinamentos.com/introducao-ao-pandas-python):** Base teórica para o tratamento de DataFrames em Python.
2. **[Como a telemetria vai revolucionar a pilotagem (Academia do Kart)](https://academiadokart.com.br/dicas-de-pilotagem/post/telemetria/):** Conceitos práticos de pilotagem baseada em dados.
3. **[Documentação Oficial do FastF1 (GitHub)](https://github.com/theOehrly/Fast-F1):** Lógica analítica aplicada pelas equipes de Fórmula 1 usando bibliotecas em Python.
4. **[iRacing Telem, APIs & SDKs (Byte Insight)](https://byteinsight.co.uk/2023/12/iracing-telemetry-apis-sdks/):** Documentação técnica sobre a extração nativa de arquivos `.ibt` via PyIrSDK.

## Engenharia de Prompts e "Cicatrizes" (Troubleshooting)
Durante o processo de geração do resumo estruturado, foi necessário realizar refinamentos iterativos para garantir o rigor técnico do material. 

**Prompt Inicial:**
> "Atue como um Engenheiro de Dados especialista em e-sports e Automobilismo Virtual. Com base exclusivamente nas fontes fornecidas, elabore um resumo estruturado e direto ao ponto..."

**A "Cicatriz" (Troubleshooting):**
Na primeira resposta, a IA misturou o contexto dos dados comerciais do artigo base de Pandas com os dados do simulador, utilizando um exemplo focado em vendas `(ex: vendas_df.loc[vendas_df['Freio'] > 0])`. No automobilismo, não há "vendas" cruzadas com "freios".

**O Refinamento (Prompt 2):**
> "A sua resposta anterior ficou excelente na estrutura, mas notei que na explicação do comando 'loc[]' você utilizou o termo 'vendas_df', que é um resquício de exemplos comerciais de Pandas. Reescreva apenas a seção de 'Comandos de engenharia de dados do Pandas aplicados', substituindo qualquer referência a vendas por nomes de variáveis adequados ao contexto de automobilismo (exemplo: telemetria_df). Mantenha o rigor técnico."

Com esse refinamento, consegui forçar a IA a se adaptar perfeitamente ao contexto técnico desejado, substituindo os termos genéricos e gerando o Miniguia correto abaixo.

---

## Miniguia de Estudo

### 1. Resumo Estruturado
**O que é a telemetria e qual sua importância na pilotagem:**
- **Definição técnica:** Consiste na captação de dados fundamentais durante as voltas, registrando canais vitais como traçado, velocidade e inputs de pedais.
- **Eliminação do "achismo":** Substitui intuições por dados numéricos confiáveis para a tomada de decisão.
- **Análise comparativa:** Permite colocar lado a lado as próprias voltas ou comparar desempenho com outros competidores.

**Extração de dados do iRacing:**
- Os dados são salvos em arquivos `.ibt` no diretório local do simulador através do atalho *Alt-L*.
- Estes arquivos podem ser convertidos para softwares como MoTeC, ou lidos programaticamente via SDK.

**Python e Pandas na Análise de Dados:**
- **Aquisição (PyIrSDK):** Ponte em Python para ler os arquivos `.ibt`.
- **Tratamento (Pandas):** Converte logs massivos em *DataFrames*.
- **Comandos aplicados (Corrigido):**
  - `describe()`: Gera resumos estatísticos (ex: picos de velocidade).
  - `loc[]`: Filtra dados específicos, como zonas de frenagem (`telemetria_df.loc[telemetria_df['Freio'] > 0]`).
  - `groupby()`: Agrupa métricas para extrair dados consolidados volta a volta.
- Esta lógica espelha arquiteturas de alta performance de escuderias reais (ex: biblioteca FastF1).

### 2. Glossário
- **Arquivos .ibt:** Arquivos nativos de telemetria gravados na pasta local do iRacing, contendo dados brutos de simulação.
- **DataFrame:** Principal estrutura de dados do Pandas, organizada em linhas e colunas rotuladas, ideal para manipular dados físicos de pista.
- **FastF1:** Biblioteca Python desenvolvida para acessar e analisar dados de cronometragem e telemetria da Fórmula 1.
- **PyIrSDK:** Biblioteca SDK em Python para extrair dados do simulador iRacing e ler arquivos físicos.
- **Telemetria:** Medição e captação de dados cruciais de pista para fundamentar decisões e aprimorar a pilotagem.

### 3. Prompts Reutilizáveis (Para Revisão Futura)
Para expandir os estudos práticos, estruturarei os testes técnicos futuros utilizando os seguintes prompts:

1. **Análise de Desempenho (Pandas):** "Atue como um Engenheiro de Dados de Automobilismo Virtual. Eu tenho um DataFrame do Pandas chamado `telemetria_df` contendo dados de sensores de uma sessão do iRacing extraídos via PyIrSDK... Escreva um script em Python que utilize o método `.loc[]` para isolar todas as zonas de frenagem ativa (> 10%) e aplique `.groupby('Volta')` para calcular a velocidade mínima de contorno de curva..."
2. **Visualização Gráfica (Matplotlib):** "Atue como um Engenheiro de Telemetria... Gere um script em Python usando Pandas e Matplotlib para plotar um gráfico de comparação de telemetria entre dois pilotos alinhando as voltas pelo eixo de 'Distancia'. O gráfico deve conter subplots de Velocidade, Acelerador e Freio..."
3. **Feature Engineering:** "Atue como um Cientista de Dados especialista em e-sports... Escreva funções em Python que recebam um DataFrame de telemetria e retornem novas colunas calculadas: uma métrica de consistência de aceleração, o percentual de Full Throttle por volta e o preenchimento de pequenos valores nulos (NaN) usando `.ffill()`."
