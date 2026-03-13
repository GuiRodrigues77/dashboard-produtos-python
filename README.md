#  Dashboard de Produtos - Streamlit

Oi! 👋 Seja bem-vindo ao meu projeto de **Dashboard de Produtos** feito em **Python** com **Streamlit**, **Pandas** e **Plotly**.  
Ele foi criado para analisar dados de produtos de forma rápida e interativa, a partir de um arquivo CSV.

---

## 💡 Funcionalidades

- Filtrar produtos individualmente ou visualizar todos juntos  
- Métricas rápidas: total de registros, quantidade total, média e produto mais vendido  
- Gráficos interativos:
  - Barra: quantidade por produto  
  - Pizza: distribuição percentual  
  - Linha: evolução das quantidades ao longo do dataset  
- Ranking de produtos (do mais vendido ao menos vendido)  
- Download dos dados filtrados em CSV  

---

## 🛠️ Como usar

1. Clone o repositório:

```bash
git clone https://github.com/GuiRodrigues77/dashboard-produtos-python

Entre na pasta do projeto:

cd Projeto-1

Instale as dependências:

pip install -r requirements.txt

Rode o dashboard:

python -m streamlit run app.py

O navegador vai abrir automaticamente com o dashboard. Se não abrir, copie o link que aparece no terminal (http://localhost:8501) e cole no navegador.

📁 Estrutura do projeto
Projeto-1/
│
├─ app.py                  # Código principal do dashboard
├─ requirements.txt        # Bibliotecas necessárias
├─ dados_exemplo.csv       # CSV de exemplo
├─ README.md               # Este arquivo
└─ .gitignore              # Arquivos a serem ignorados no Git
📝 Observações

O CSV precisa ter duas colunas: produto e quantidade

O dashboard aceita qualquer CSV com essas colunas, então você pode testar com os seus próprios dados

As cores dos gráficos são automáticas, garantindo que sempre fiquem bonitas e legíveis, independentemente dos produtos

🎯 Próximos passos (opcional)

Adicionar gráficos de comparação entre períodos

Permitir upload de múltiplos CSVs ao mesmo tempo

Melhorar filtros com múltiplos produtos simultaneamente

Obrigado por conferir! 🙏
Se testar o projeto, qualquer dúvida ou sugestão, pode me chamar. 🚀


---

Se você quiser, posso também **gerar um `dados_exemplo.csv` pequeno e pronto** para colocar no GitHub junto com esse README.  
Isso deixa o repositório **completo, pronto para portfólio**, e qualquer pessoa consegue testar sem precisar criar o CSV.  

Quer que eu faça isso?
