import gradio as gr
import google.generativeai as genai
import os
import re

# Configure Gemini API
genai.configure(api_key="AIzaSyBUhtWn65oJHF4Q7k7B9QBTIhuJvIIwNHw")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def process_pix_request(message):
    # Identify intent
    intent_prompt = f"""Identifique a intenção principal do seguinte texto: "{message}".
    A intenção deve ser uma das seguintes categorias:
    - ENTENDER_PIX_AUTOMATICO
    - COMO_CADASTRAR_PIX
    - COMO_AGENDAR_PIX
    - CONSULTAR_AGENDAMENTOS_PIX
    - CANCELAR_AGENDAMENTO_PIX
    - PROBLEMA_PAGAMENTO
    - LIMITES_PIX_AUTOMATICO
    - REGRAS_PIX_AUTOMATICO
    - DUVIDA_OUTROS_PAGAMENTOS
    - NAO_RECONHECIDA
    Retorne apenas o nome da categoria da intenção."""
    
    try:
        intent_response = model.generate_content(intent_prompt)
        intent = intent_response.text.strip()
        
        # Extract entities
        entities = {}
        message = message.lower()
        
        if intent in ["ENTENDER_PIX_AUTOMATICO", "COMO_CADASTRAR_PIX", "COMO_AGENDAR_PIX", "CANCELAR_AGENDAMENTO_PIX"]:
            beneficiario_match = re.search(r"(?:para|de)\s*(a|o|os|as)\s*(.*?)(?:,|\s|$|\.)", message)
            if beneficiario_match:
                entities["beneficiario"] = beneficiario_match.group(2).strip()
            
            valor_match = re.search(r"(?:valor|de)\s*(r\$?\s*[\d.,]+)", message)
            if valor_match:
                try:
                    entities["valor"] = float(valor_match.group(1).replace("r$", "").replace(" ", "").replace(",", "."))
                except ValueError:
                    pass
                    
            data_match = re.search(r"(?:para|em)\s*([\d/.-]+)", message)
            if data_match:
                entities["data"] = data_match.group(1).strip()
        
        # Generate response
        response_prompt = ""
        if intent == "ENTENDER_PIX_AUTOMATICO":
            response_prompt = "Explique o que é o Pix automático de forma clara e concisa."
        elif intent == "COMO_CADASTRAR_PIX":
            beneficiario = entities.get("beneficiario", "o beneficiário")
            response_prompt = f"Como posso cadastrar o Pix automático para {beneficiario}? Forneça um guia passo a passo."
        elif intent == "COMO_AGENDAR_PIX":
            beneficiario = entities.get("beneficiario", "o beneficiário")
            data = entities.get("data", "a data desejada")
            valor = entities.get("valor", "o valor")
            response_prompt = f"Como agendo um Pix para {beneficiario} no valor de R$ {valor} para {data}?"
        elif intent == "PROBLEMA_PAGAMENTO":
            response_prompt = "Descreva o problema que você está enfrentando com o pagamento para que eu possa ajudar melhor."
        else:
            response_prompt = "Por favor, especifique melhor sua dúvida sobre Pix Automático para que eu possa ajudar."
            
        final_response = model.generate_content(response_prompt)
        return final_response.text
        
    except Exception as e:
        return f"Desculpe, ocorreu um erro ao processar sua solicitação: {str(e)}"

# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as interface:
    gr.Markdown("""
    # 🏦 Assistente Pix Automático
    
    Olá! Sou seu assistente virtual especializado em Pix Automático. Como posso ajudar?
    """)
    
    with gr.Row():
        with gr.Column(scale=4):
            txt_input = gr.Textbox(
                label="Digite sua mensagem",
                placeholder="Ex: Como faço para agendar um Pix de R$ 100 para João?",
                lines=3
            )
        with gr.Column(scale=1):
            btn_send = gr.Button("Enviar", variant="primary")
            
    txt_output = gr.Textbox(
        label="Resposta",
        lines=8,
        interactive=False
    )
    
    btn_send.click(
        fn=process_pix_request,
        inputs=txt_input,
        outputs=txt_output
    )

# Launch the interface
if __name__ == "__main__":
    interface.launch(share=True)