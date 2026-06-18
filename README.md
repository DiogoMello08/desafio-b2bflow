# Desafio Técnico - Estágio Python | b2bflow

## Objetivo
Aplicação desenvolvida em Python que consulta contatos armazenados no Supabase e realiza o envio automatizado de mensagens personalizadas via WhatsApp utilizando a Z-API.
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

```text
desafio-b2bflow/
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── whatsapp.py
│   └── main.py
│
├── run.py
├── .env.example
├── requirements.txt
└── README.md
```

## Fluxo da Aplicação
1. Consulta contatos no Supabase.
2. Valida os registros retornados.
3. Personaliza a mensagem para cada contato.
4. Envia a mensagem via Z-API.
5. Registra logs de execução e possíveis falhas.

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
```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```
## Estrutura da Tabela
| Campo    | Tipo    |
|----------|---------|
| id       | integer |
| nome     | text    |
| telefone | text    |

## Funcionalidades
- Busca até 3 contatos cadastrados no Supabase.
- Personaliza a mensagem utilizando o nome do contato.
- Envia mensagens via WhatsApp utilizando a Z-API.
- Valida registros inválidos retornados pelo banco.
- Utiliza variáveis de ambiente para proteger informações sensíveis.
- Implementa logs para acompanhamento da execução.
- Implementa tratamento básico de erros.

## Resultado
Ao executar a aplicação:

1. Os contatos são consultados no Supabase.
2. Até 3 registros são processados.
3. A mensagem é personalizada com o nome do contato.
4. A mensagem é enviada para o WhatsApp através da Z-API.
5. O sistema registra logs de execução e possíveis falhas.

## Execução

```bash
python run.py
```
## Boas Práticas Implementadas

- Separação de responsabilidades em módulos.
- Uso de variáveis de ambiente para credenciais.
- Tratamento de exceções nas integrações externas.
- Registro de logs para monitoramento da execução.
- Estrutura preparada para expansão futura.