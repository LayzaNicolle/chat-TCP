Protocolo de Comunicação – Mini Chat TCP

Este documento descreve todas as regras de comunicação entre cliente e servidor, incluindo comandos aceitos, respostas possíveis e exemplos de uso. O cliente deve seguir rigorosamente este protocolo para garantir funcionamento correto.

1. Estrutura Geral

A comunicação ocorre via TCP.
Cada mensagem enviada do cliente para o servidor é uma linha finalizada com \n.
O servidor também envia respostas sempre como linhas separadas.

2. Registro de Apelido

O cliente deve registrar um apelido como primeira ação após conectar.

Comando
NICK <apelido>

Regras

O apelido não pode estar em uso.

O apelido não pode ser vazio.

Respostas possíveis
SYSTEM: New User. Welcome, <apelido>!


Ou, em caso de erro:

SYSTEM: ERROR: nick already in use. Choose another.


Se o cliente enviar qualquer outro comando antes do NICK, o servidor responde:

SYSTEM: Please register first with: NICK your_nick

3. Mensagens
3.1. Broadcast (mensagem pública)

Enviar mensagem para todos os usuários conectados.

Formato
MSG <mensagem>

Resposta server → clientes

Para todos os clientes (exceto o remetente):

FROM <apelido> [all]: <mensagem>

3.2. Mensagem Direta (privada)

Enviar mensagem somente para um alvo específico.

Formato
MSG @<apelido_destino> <mensagem>

Respostas possíveis

Se o destinatário existir:

O destinatário recebe:

FROM <apelido_remetente> [dm]: <mensagem>


Se o destinatário não existir:

SYSTEM: ERROR: user <apelido_destino> not found or delivery failed.

4. Listar usuários conectados
Comando
WHO

Resposta
SYSTEM: Connected users: <lista_de_usuarios>


Exemplo:

SYSTEM: Connected users: ana, joao, pedro

5. Encerrar conexão
Comando
QUIT

Resposta
SYSTEM: Goodbye!


Ao sair, os demais usuários recebem:

SYSTEM: User <apelido> left.

6. Eventos de Sistema
Quando um novo usuário entra

Todos os outros clientes recebem:

SYSTEM: User <apelido> joined.

Quando o usuário perde a conexão inesperadamente

Todos recebem:

SYSTEM: User <apelido> left.

7. Erros Gerais
Comando desconhecido
SYSTEM: Unknown command. Use: MSG, WHO, QUIT

Tentativa de apelido duplicado
SYSTEM: ERROR: nick already in use. Choose another.

Mensagem privada para usuário inexistente
SYSTEM: ERROR: user <apelido> not found or delivery failed.