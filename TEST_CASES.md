# Casos de Teste - Mini Chat TCP

Este documento descreve os principais casos de teste do Mini Chat TCP, com cenários, ações e resultados esperados.

---

## 1. Broadcast com múltiplos clientes

**Cenário:**  
Três clientes conectados ao servidor.

**Ação:**  
Cliente A envia:  
Olá pessoal


**Resultado Esperado:**  
Clientes B e C recebem a mensagem:  
FROM A [all]: Olá pessoal


---

## 2. Mensagem direta para usuário existente

**Cenário:**  
Cliente B está conectado com o nick `maria`.

**Ação:**  
Cliente A envia:  
/msg maria oi


**Resultado Esperado:**  
Somente Maria recebe a mensagem:  
FROM A [dm]: oi


---

## 3. Mensagem direta para usuário inexistente (erro)

**Cenário:**  
Não existe nenhum usuário conectado com o nick `desconhecido`.

**Ação:**  
Cliente A envia:  
/msg desconhecido oi


**Resultado Esperado:**  
Servidor responde ao remetente:  
SYSTEM: ERROR: user desconhecido not found.


---

## 4. Tentativa de apelido duplicado

**Cenário:**  
Cliente A entra com o apelido `ana`.

**Ação:**  
Cliente B tenta entrar com o mesmo apelido `ana`.

**Resultado Esperado:**  
Servidor responde ao Cliente B:  
SYSTEM: ERROR: nick already in use. Choose another.


---

## Observações Gerais

- Todos os testes devem ser realizados com o servidor rodando (`python server.py`).  
- Use terminais diferentes para simular múltiplos clientes (`python client.py`).  
- Verifique se cada cliente está registrando corretamente o apelido antes de enviar mensagens



