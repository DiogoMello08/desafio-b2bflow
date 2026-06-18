# Desafio Técnico - Estágio Python | b2bflow

## Objetivo
Aplicação desenvolvida em Python para leitura de contatos armazenados no Supabase e envio de mensagens personalizadas via Z-API.
A mensagem enviada segue o formato:
Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

## Tecnologias Utilizadas

- Python 3.12
- Supabase
- Z-API
- Requests
- Python Dotenv

## Estrutura do Projeto
src/

├── config.py

├── database.py

├── whatsapp.py

└── main.py

run.py
.env.example
requirements.txt
README.md

## Configuração 
1. Clonar o projeto
git clone <repositorio>

2. Criar ambiente virtual
python -m venv venv

3. Ativar ambiente virtual
Windows
venv\Scripts\activate

4. Instalar dependências 
pip install -r requirements.txt

5. Configurar variáveis de ambiente 
Criar um arquivo .env com:

SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=

## Estrutura da Tabela 
Campo                Tipo
id                   integer
nome                 text
telefone             text

- Funcionalidades 
. Busca até 3 contatos cadastrados no Supabase.
. Personaliza a mensagem utilizando o nome do contato.
. Valida registros inválidos.
. Utiliza variáveis de ambiente para informações sensíveis.
. Implementa logs para acompanhamento da execução.
. Implementa tratamento básico de erros.

## Observações
Durante o desenvolvimento foram implementados:

- Logs para acompanhamento da execução.
- Validação básica dos contatos retornados pelo banco.
- Tratamento de erros na integração com o Supabase.
- Uso de variáveis de ambiente para proteger informações sensíveis.

## Execução
Para executar a aplicação:

```bash
python run.py
```
