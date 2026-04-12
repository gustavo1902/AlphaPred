# AlphaPred: Detector de Oportunidades em Mercados de Previsão

O AlphaPred é um pipeline quantitativo de dados projetado para identificar ineficiências e erros de precificação em mercados de previsão institucionais e descentralizados, como Polymarket e Kalshi. O sistema compara as probabilidades implícitas (consenso de mercado) com estimativas probabilísticas algorítmicas, isolando o desvio padrão (**Edge** ou **Alpha**) para expor oportunidades de arbitragem em eventos macroeconômicos e políticos.

## Arquitetura do Sistema

O projeto é estruturado como um pipeline de extração, transformação e carregamento (ETL), acoplado a uma API REST para distribuição dos dados.

*   **Ingestão de Dados:** Conexão direta com as APIs públicas de plataformas de previsão para captura de eventos ativos e volumes de negociação.
*   **Processamento e Normalização:** Tratamento de strings, formatação de arrays de preços e conversão de cotações em probabilidades matemáticas.
*   **Motor de Cálculo (Alpha Engine):** Avaliação da probabilidade do mercado contra modelos internos, gerando sinais direcionais (STRONG_BUY, SELL, etc.).
*   **Armazenamento de Estado:** Salvamento autônomo dos resultados no arquivo `data/signals.json`.
*   **Distribuição:** Servidor FastAPI que expõe os dados estáticos para consumo de frontends (ex: Radar Econômico).
*   **Orquestração Automática:** Utilização do GitHub Actions para rodar o pipeline em intervalos programados, garantindo dados sempre atualizados sem necessidade de servidor rodando 24/7 para a coleta.

---

## Estrutura do Repositório

A base de código segue princípios de modularidade, separando as regras de negócios da infraestrutura de entrega:

*   `/.github/workflows/`: Configurações de automação e CI/CD. Contém as rotinas que engatilham o script de extração e atualizam o repositório.
*   `/api/`: Contém a aplicação FastAPI (`main.py`) e regras de roteamento HTTP, responsável por servir o endpoint `/signals`.
*   `/dashboard/`: Estruturas de visualização e lógicas de filtros por tipos de eventos.
*   `/data/`: Diretório de armazenamento de estado. Mantém o artefato consolidado `signals.json`.
*   `/scripts/`: Scripts de execução de rotinas, como o `run_pipeline.py`, que orquestra a coleta e salvamento dos dados.
*   `/src/`: Core da aplicação. Contém as lógicas de integração (conectores Kalshi/Polymarket) e módulos de parsing de dados.
*   `/tests/`: Suíte de testes unitários para garantir a integridade de funções matemáticas críticas, como a `compute_alpha`.
*   `render.yaml` / `requirements.txt`: Especificações de infraestrutura as code (IaC) e mapeamento de dependências Python para o deploy na nuvem.

---

## Stack Tecnológica

*   **Linguagem Principal:** Python 3.x
*   **Framework Web / API:** FastAPI, Uvicorn
*   **Integração HTTP:** Requests
*   **Serialização de Dados:** JSON, Pydantic
*   **Infraestrutura e Deploy:** GitHub Actions (ETL Automation), Render (Hosting da API)

---

## Inicialização e Execução Local

Para rodar o ambiente de desenvolvimento em sua máquina e realizar testes nas funções de coleta e cálculo:

### 1. Instalação
Clone o repositório e instale as dependências necessárias:

```bash
git clone https://github.com/seu-usuario/AlphaPred.git
cd AlphaPred
pip install -r requirements.txt
```

### 2. Coleta de Dados
Este comando aciona os extratores, processa as cotações atuais e atualiza o arquivo signals.json localmente.

```bash
PYTHONPATH=. python scripts/run_pipeline.py
```

### 3. Servidor API
Inicie o servidor local. A API ficará disponível em `http://localhost:8000`.

```bash
uvicorn api.main:app --reload
```

---

## Execução de Testes

Para garantir que o motor de cálculo está operando com precisão matemática, execute a suíte de testes:

```bash
pytest tests/
```