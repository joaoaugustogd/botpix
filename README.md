# 🤖 Botpix – Assistente Inteligente para Pix Automático

Este projeto implementa uma automação em Python que utiliza Inteligência Artificial para interpretar mensagens relacionadas ao **Pix Automático**. A solução identifica a intenção do usuário e extrai entidades relevantes como beneficiário, valor, data, tipo de pagamento e muito mais.

O motor de IA usado é o **Google Gemini**, integrando compreensão de linguagem natural com regras personalizadas para uma extração precisa e contextual.

---

## 👤 Autor

**João Augusto**  
Designer Pleno | Especialista em UX e automações com IA  
📍 Brasil

---

## 🧠 Principais Funcionalidades

- Interpretação inteligente de mensagens sobre:
  - Cadastro de Pix Automático
  - Agendamento e cancelamento
  - Consulta de agendamentos
  - Problemas de pagamento
  - Dúvidas sobre regras, limites ou pagamentos em geral

- Extração de entidades personalizadas:
  - Beneficiário
  - Conta
  - Valor
  - Data
  - Tipo de pagamento
  - ID da transação

- Arquitetura modular com uso de expressões regulares
- Integração simples com bots, apps bancários, CRMs ou assistentes virtuais

---

## 📂 Estrutura do Projeto

---

## 🚀 Como funciona

### 🔍 Classificação de Intenção

O modelo do **Google Gemini** interpreta a intenção do usuário com base no texto enviado. As intenções mapeadas atualmente são:

- ``ENTENDER_PIX_AUTOMATICO`
  - ``COMO_CADASTRAR_PIX`
  - ``COMO_AGENDAR_PIX`
  - ``CONSULTAR_AGENDAMENTOS_PIX`
  - ``CANCELAR_AGENDAMENTO_PIX`
  - ``PROBLEMA_PAGAMENTO`
  - ``LIMITES_PIX_AUTOMATICO`
  - ``REGRAS_PIX_AUTOMATICO`
  - ``DUVIDA_OUTROS_PAGAMENTOS`
  - ``NAO_RECONHECIDA`

---


🧾 Extração de Entidades

A extração usa expressões regulares para mapear as entidades mais comuns nas mensagens dos usuários.

📥 Exemplo de Uso
from extractor import agente_extrator_entidades_pagamentos

mensagem = "Quero agendar um Pix automático de R$ 250,00 para o João no dia 20/05"
intencao = "COMO_AGENDAR_PIX"

entidades = agente_extrator_entidades_pagamentos(mensagem, intencao)

print(entidades)
# Saída esperada:
# {
#   "beneficiario": "João",
#   "valor": 250.0,
#   "data": "20/05"
# }


📦 Instalação

Clone o repositório
git clone https://github.com/seu-usuario/botpix.git

Acesse o diretório
cd botpix

(Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Instale as dependências
pip install -r requirements.txt

------

🔗 Integração com o Google Gemini

from google.generativeai import GenerativeModel

model = GenerativeModel('gemini-pro')
mensagem = "Quero cancelar o Pix automático que cadastrei para pagar a conta da Claro"
response = model.generate_content("Classifique a intenção da mensagem: " + mensagem)
print(response.text)

