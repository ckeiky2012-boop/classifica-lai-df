\# ClassificaLAI-DF


\## 1. Descrição Geral


O ClassificaLAI-DF é uma solução automatizada desenvolvida para identificar, entre pedidos de acesso à informação classificados como públicos, aqueles que contêm dados pessoais e que, portanto, deveriam ser classificados como não públicos.

O projeto foi desenvolvido para o 1º Hackathon em Controle Social – Desafio Participa DF, na categoria \*\*Acesso à Informação\*\*, conforme o Edital nº 10/2025 da Controladoria-Geral do Distrito Federal (CGDF).

A solução contribui para a proteção de dados pessoais e para a correta aplicação da Lei de Acesso à Informação (Lei nº 12.527/2011) e da Lei Geral de Proteção de Dados (Lei nº 13.709/2018).

---

\## 2. Problema

Pedidos de acesso à informação marcados como públicos podem conter, de forma indevida, dados pessoais como nome, CPF, telefone ou endereço de e-mail. A identificação manual desses casos é suscetível a falhas e demanda esforço administrativo significativo.

---

\## 3. Objetivo


Desenvolver um modelo automatizado capaz de identificar a presença de dados pessoais em textos de pedidos de acesso à informação, apoiando a correta classificação dessas solicitações.

---

\## 4. Base de Dados

O modelo utiliza exclusivamente dados sintéticos disponibilizados pela Controladoria-Geral do Distrito Federal para o desafio, criados especificamente para fins de teste, conforme previsto no edital. Nenhum dado pessoal real é utilizado.

---

\## 5. Abordagem Técnica

A solução utiliza uma abordagem baseada em regras e expressões regulares (Regex), permitindo a identificação automática de padrões textuais associados a dados pessoais, tais como:

\- CPF (com ou sem formatação)

\- Endereços de e-mail

\- Telefones


Essa abordagem foi escolhida por sua simplicidade, transparência, facilidade de auditoria e rápida execução.

---

\## 6. Estrutura do Projeto


classifica-lai-df/

├── data/

├── src/

│   ├── detector.py

│   └── main.py

├── requirements.txt

└── README.md

7\. Requisitos


Python 3.9 ou superior


\## 8. Instalação



A solução utiliza apenas bibliotecas padrão do Python, não sendo necessária a instalação de dependências adicionais.



Opcionalmente, pode-se criar um ambiente virtual com o comando:



python -m venv venv



\## 9. Execução

Para executar o modelo, utilize o seguinte comando no diretório raiz do projeto:

python src/main.py

O programa solicitará a entrada de um texto correspondente a um pedido de acesso à informação.

\## 10. Saída


Após a análise do texto informado, o sistema retorna uma das seguintes mensagens:

Resultado: O pedido CONTÉM dados pessoais

Resultado: O pedido NÃO contém dados pessoais

\## 11. Conformidade com o Edital

Esta solução atende integralmente aos requisitos da categoria Acesso à Informação, permitindo avaliação objetiva por métricas de desempenho e análise da documentação técnica, conforme estabelecido no Edital nº 10/2025 do 1º Hackathon em Controle Social – Desafio Participa DF.

\## 12. Considerações Finais

O ClassificaLAI-DF apresenta uma solução simples, automatizada e auditável para apoiar a proteção de dados pessoais no contexto do acesso à informação pública, contribuindo para o fortalecimento da transparência responsável no Distrito Federal.



