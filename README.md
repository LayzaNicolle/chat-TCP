Mini Chat TCP

EQUIPE:

Layza Nicolle 
Bárbara Luiza
Matheus Pablo
Vinicius Simas

Este projeto implementa um sistema de chat simples utilizando sockets TCP, composto por um servidor e um cliente executados via terminal. O servidor gerencia conexões simultâneas, controla apelidos, realiza broadcast de mensagens e permite mensagens privadas. O cliente se conecta ao servidor, registra um apelido e envia mensagens conforme o protocolo definido.

Servidor

O servidor é responsável por aceitar múltiplas conexões, registrar apelidos, enviar mensagens de broadcast, enviar mensagens privadas, emitir erros e encerrar conexões corretamente.
O código do servidor está no arquivo server.py.

Cliente

O cliente se conecta ao servidor via terminal, registra um apelido, envia mensagens públicas e privadas, além de receber mensagens em tempo real.
O código do cliente está no arquivo client.py.

Documento do Protocolo

Todos os comandos e respostas seguem o que está descrito no arquivo PROTOCOLO.md.
O cliente deve seguir esse protocolo para se comunicar corretamente com o servidor.

Guia de Execução
Executar o servidor

Verifique se o Python 3 está instalado.

Abra o terminal na pasta do projeto.

Execute o servidor:

python server.py


O servidor iniciará e ficará aguardando conexões.

Conectar um cliente

Abra um novo terminal.

Acesse a pasta do projeto.

Execute o cliente:

python client.py


Quando solicitado, digite seu apelido.

Envie mensagens normalmente.

Conectar dois ou mais clientes

Com o servidor rodando, abra quantos terminais desejar.

Em cada terminal, execute:

python client.py


Escolha um apelido diferente para cada cliente.

Todos os clientes poderão enviar e receber mensagens entre si.

Exemplos de uso

Broadcast:
Enviar uma mensagem pública:

Olá a todos


Mensagem privada:
Enviar diretamente para outro usuário:

/msg joao tudo bem?

Casos de Teste

1. Broadcast com múltiplos clientes

Cenário:
Três clientes conectados ao servidor.

Ação:
Cliente A envia:

Olá pessoal


Resultado esperado:
Clientes B e C recebem a mensagem.

2. Mensagem direta para usuário existente

Ação:
Cliente A envia:

/msg maria oi


Resultado esperado:
Somente Maria recebe a mensagem privada.

3. Mensagem direta para usuário inexistente

Ação:
Cliente A envia:

/msg desconhecido oi


Resultado esperado:
Servidor responde:

ERRO: usuário não encontrado.

4. Tentativa de apelido duplicado

Ação:
Cliente A entra com apelido "ana".
Cliente B tenta entrar com o mesmo apelido.

Resultado esperado:
Servidor responde ao Cliente B:

ERRO: apelido já está em uso.