# 💰 App terminal Bank
Um programa para executar no terminal simulando de forma simples operações bancárias.

## requisitos funcionais

* RF001: O sistema deve permitir o cadastro de novos usuários (cliente), solicitando nome, CPF (servirá como login) e senha.
* RF002: O sistema deve impedir o cadastro de dois usuários com o mesmo CPF.
* RF003: O sistema deve permitir que um usuário cadastrado faça login usando CPF e senha.
* RF004: O sistema deve bloquear o acesso se o login (CPF ou senha) estiver incorreto.
* RF005: O sistema deve permitir que o usuário logado consulte seu saldo. O saldo inicial de um novo usuário é R$ 0,00.
* RF006: O sistema deve permitir que o usuário logado realize um depósito em sua própria conta.
* RF007: O sistema deve permitir que o usuário logado realize um saque de sua própria conta.
* RF008: O sistema não deve permitir um saque se o valor solicitado for maior que o saldo disponível.
* RF009: O sistema deve salvar os dados dos usuários e seus saldos em um arquivo.
* RF010: O sistema deve carregar os dados dos usuários e seus saldos do arquivo ao ser iniciado.

## requisitos não funcionais
* RNF001 (Usabilidade): O sistema deve ser operado via console (terminal) e apresentar um menu de opções claro e objetivo.
* RNF002 (Segurança): O acesso às operações de consulta, saque e depósito deve ser restrito ao usuário autenticado (logado).
* RNF003 (Extensibilidade): O sistema deve ser projetado de forma que facilite uma futura migração para uma interface web.
---

### Utilizar as seguintes estruturas:

* if/else e/ou swicth/elif 
* while/do..while e/ou for 
* subprogramas 
* matrizes/listas 
* cadeia de caracteres/string 
* estruturas(registros/dicionários/tuplas) 
* arquivos

