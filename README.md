# Projeto Sprint 5 – Desenvolvimento e Implantação de Dashboard Interativo em Nuvem

## 1. Introdução
Este projeto foi desenvolvido como parte da Sprint 5, com o objetivo de consolidar competências práticas em **engenharia de software**, **ciência de dados** e **desenvolvimento de aplicações web**.  
A proposta consiste na criação de um **dashboard interativo** utilizando a biblioteca **Streamlit**, com visualizações gráficas elaboradas por meio de **Plotly Express**, e sua posterior implantação em ambiente de nuvem através da plataforma **Render**.

A iniciativa busca proporcionar experiência aplicada em:
- Gerenciamento de ambientes virtuais em Python  
- Estruturação de repositórios Git e GitHub  
- Desenvolvimento de aplicações web interativas  
- Implantação de sistemas em serviços de nuvem  

---

## 2. Objetivos
Os objetivos centrais do projeto são:
- Desenvolver um aplicativo web funcional e acessível via navegador.  
- Implementar visualizações interativas de dados (histogramas e gráficos de dispersão).  
- Aplicar boas práticas de versionamento e documentação de software.  
- Demonstrar capacidade de integração entre ferramentas de análise de dados e plataformas de hospedagem em nuvem.  

---

## 3. Estrutura do Repositório
A organização dos arquivos segue padrões recomendados para projetos de software:
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml


---

## 4. Metodologia
O desenvolvimento do projeto foi estruturado em etapas sequenciais:

1. **Configuração inicial**: criação de repositório GitHub, ambiente virtual Python e instalação das bibliotecas necessárias (`pandas`, `plotly-express`, `streamlit`).  
2. **Análise exploratória de dados (EDA)**: elaboração de visualizações preliminares em Jupyter Notebook para compreensão do conjunto de dados.  
3. **Desenvolvimento do aplicativo web**: implementação do arquivo `app.py` com funcionalidades interativas, incluindo cabeçalhos, botões e gráficos.  
4. **Implantação em nuvem**: configuração do serviço Render, definição de comandos de build e start, e disponibilização pública do aplicativo.  

---

## 5. Funcionalidades do Aplicativo
O aplicativo web contempla:
- Um cabeçalho explicativo.  
- Um histograma interativo gerado com Plotly Express.  
- Um gráfico de dispersão interativo.  
- Elementos de interação (botões ou caixas de seleção) que permitem ao usuário escolher a visualização desejada.  

---

## 6. Execução Local
Para executar o projeto em ambiente local:

# Clonar o repositório
git clone
https://github.com/AdrianaSoares/projeto5vehicles.git

# Criar e ativar ambiente virtual
python -m venv vehicles_env
source vehicles_env/bin/activate   # Linux/Mac
vehicles_env\Scripts\activate      # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar o aplicativo
streamlit run app.py


## 7. Implantação em Nuvem
O aplicativo foi implantado na plataforma **Render**, garantindo acessibilidade pública.  
O acesso pode ser realizado através do seguinte endereço:  
👉 https://projeto5vehicles-2.onrender.com

---

## 8. Conjunto de Dados
O dataset utilizado (`vehicles_us.csv`) contém informações sobre anúncios de vendas de veículos nos Estados Unidos.  
Embora este seja o conjunto de dados sugerido, o projeto permite substituição por qualquer arquivo CSV compatível.  

---

## 9. Critérios de Avaliação
O projeto será considerado satisfatório quando atender aos seguintes requisitos:
- Presença dos arquivos obrigatórios no repositório.  
- Aplicativo acessível via navegador.  
- Implementação de cabeçalho, histograma, gráfico de dispersão e elementos de interação.  

---

## 10. Conclusão
Este projeto representa uma aplicação prática dos conhecimentos adquiridos em desenvolvimento de software e ciência de dados, demonstrando a capacidade de integrar ferramentas de análise, bibliotecas de visualização e plataformas de nuvem em um fluxo de trabalho completo.  


