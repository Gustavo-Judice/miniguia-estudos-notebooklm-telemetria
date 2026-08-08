import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# PROJETO: Análise de Telemetria iRacing com Python e Pandas
# DESCRIÇÃO: Script para ler, limpar e analisar dados extraídos do iRacing (.ibt)
# ==============================================================================

def analisar_telemetria(caminho_arquivo):
    # NOTA: Em um cenário real, você usaria o PyIrSDK para ler o arquivo .ibt.
    # Aqui, como prova de conceito para o portfólio, estamos simulando a criação 
    # do DataFrame exato que o SDK nos devolveria.
    
    print("Carregando dados de telemetria...")
    
    # --- 1. SIMULAÇÃO DOS DADOS (Mock Data) ---
    # Gerando dados de sensores para 1 volta em um trecho de 1000 metros
    np.random.seed(42)
    distancia = np.linspace(0, 1000, 500)
    
    # Simulando a física: uma reta rápida seguida de uma frenagem forte
    velocidade = 250 - (distancia / 5) + np.sin(distancia/100)*30 
    
    # Simulando o input de pedais do piloto
    freio = np.where(velocidade > 200, 0, np.random.uniform(50, 100, 500))
    freio = np.where(distancia > 600, 0, freio) # Solta o freio no meio da curva
    freio = np.clip(freio, 0, 100)
    
    acelerador = np.where(freio > 0, 0, 100) # Pé embaixo onde não tem freio
    acelerador = np.where((distancia > 500) & (distancia < 700), 50, acelerador) # Controle de tração
    
    # Criando o DataFrame (a "planilha" do Pandas)
    telemetria_df = pd.DataFrame({
        'Volta': [1] * 500,
        'Distancia': distancia,
        'Velocidade': velocidade,
        'Acelerador': acelerador,
        'Freio': freio
    })
    
    print(f"Dados carregados com sucesso! Estrutura: {telemetria_df.shape[0]} medições.")
    
    # --- 2. ENGENHARIA DE DADOS E FILTRAGEM (Usando o que aprendemos no Miniguia) ---
    # Usando o .loc[] para isolar as zonas de frenagem ativa (> 10% de pressão)
    zonas_frenagem = telemetria_df.loc[telemetria_df['Freio'] > 10].copy()
    
    # Usando .groupby() para encontrar a velocidade mínima (Apex Speed) na curva
    analise_voltas = telemetria_df.groupby('Volta').agg(
        Velocidade_Minima_Apex=('Velocidade', 'min'),
        Velocidade_Maxima=('Velocidade', 'max'),
        Pico_Frenagem=('Freio', 'max')
    ).reset_index()
    
    print("\n--- Resumo de Desempenho por Volta ---")
    print(analise_voltas)
    
    # --- 3. VISUALIZAÇÃO GRÁFICA AVANÇADA (Estilo Telemetria FastF1) ---
    plt.figure(figsize=(12, 6))
    
    # Plotando a Velocidade (Linha azul)
    plt.plot(telemetria_df['Distancia'], telemetria_df['Velocidade'], 
             label='Velocidade (km/h)', color='#1f77b4', linewidth=2.5)
    
    # Preenchendo a área dos pedais (Gráfico de área para Freio e Acelerador)
    plt.fill_between(telemetria_df['Distancia'], 0, telemetria_df['Freio'], 
                     color='#d62728', alpha=0.4, label='Freio (%)')
    
    plt.fill_between(telemetria_df['Distancia'], 0, telemetria_df['Acelerador'], 
                     color='#2ca02c', alpha=0.4, label='Acelerador (%)')
    
    plt.title('Análise de Telemetria iRacing: Velocidade vs Pedais', fontsize=14, fontweight='bold')
    plt.xlabel('Distância Percorrida (metros)', fontsize=12)
    plt.ylabel('Intensidade (%) / Velocidade (km/h)', fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    # Salvando o gráfico gerado
    nome_arquivo_grafico = 'grafico_telemetria_resultado.pdf'
    plt.savefig(nome_arquivo_grafico)
    print(f"\nSucesso! Gráfico gerado e salvo como '{nome_arquivo_grafico}'")

if __name__ == "__main__":
    analisar_telemetria("dados_iracing.ibt")
