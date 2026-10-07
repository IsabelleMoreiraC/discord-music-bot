 # Discord Music Bot (yt-dlp + discord.py)

Um bot de música para Discord desenvolvido em Python, focado em alta compatibilidade e estabilidade na extração de áudio. Utiliza a biblioteca `discord.py` para a interface com a API do Discord e o `yt-dlp` para o processamento e extração de mídia do YouTube.

## 🚀 Funcionalidades

* Conexão automática a canais de voz.
* Pesquisa inteligente e reprodução via texto ou URL direta.
* Contorno de restrições de idade e bloqueios automatizados do YouTube utilizando autenticação baseada em sessão.
* Gestão autônoma de instâncias de reprodução (FFmpeg).

## 📋 Pré-requisitos

Antes de iniciar a instalação, certifique-se de que o seu ambiente atende aos seguintes requisitos:

1. **Python 3.8+** instalado no sistema.
2. **FFmpeg** instalado e devidamente configurado nas variáveis de ambiente (`PATH`) do seu sistema operacional. O FFmpeg é estritamente necessário para o processamento e codificação do fluxo de áudio.
3. Um token de Bot ativo gerado no [Discord Developer Portal](https://discord.com/developers/applications), com a intenção **Message Content Intent** habilitada.

## 🔧 Instalação e Configuração

### 1. Dependências do Projeto
Abra o seu terminal na raiz do projeto e instale as bibliotecas requeridas executando o seguinte comando:


pip install -U "discord.py[voice]" dave.py yt-dlp

    Nota Técnica: A extensão [voice] e o pacote dave.py são obrigatórios para habilitar os protocolos recentes de criptografia de voz exigidos pelo Discord. O yt-dlp deve ser mantido sempre em sua versão mais recente para evitar falhas de extração.

2. Autenticação do YouTube (cookies.txt)

Devido às rígidas políticas anti-bot do YouTube, o yt-dlp requer dados de sessão de um navegador real para operar com estabilidade e contornar erros como "Sign in to confirm you're not a bot".

    Efetue login no YouTube através de um navegador web (recomenda-se a utilização de uma conta dedicada para este fim).

    Utilize uma extensão de exportação de cookies (ex: Get cookies.txt LOCALLY no Chromium ou YT-DLP Cookie Exporter no Firefox).

    Exporte os dados no formato Netscape HTTP Cookie File.

    Salve o arquivo gerado com o nome exato de cookies.txt e posicione-o no mesmo diretório do arquivo main.py.

    ⚠️ Aviso de Segurança: O arquivo cookies.txt contém os dados de autenticação da sua conta do Google. Nunca adicione este arquivo ao controle de versão (git). Certifique-se de incluí-lo no seu .gitignore.

3. Configuração do Token

Abra o arquivo main.py e localize a variável de inicialização do bot. Substitua a string vazia pelo token de autenticação gerado no portal do Discord:
Python

TOKEN = "COLE_O_SEU_TOKEN_AQUI"

    ⚠️ Aviso de Segurança: Da mesma forma que os cookies, nunca exponha o seu Token em repositórios públicos.

💻 Uso

Para inicializar o serviço do bot, execute o script principal via terminal:

python main.py

Com o bot online e após conectar-se a um canal de voz no servidor, utilize os seguintes comandos no chat de texto:

    !play <termo de busca ou url>: Inicializa a extração e reproduz o áudio correspondente no canal de voz atual do usuário.

    !stop: Interrompe a reprodução ativa e desconecta o bot do canal de voz.

⚠️ Manutenção Comum

O ecossistema de extração de mídia do YouTube é altamente dinâmico. Caso o bot passe a apresentar erros de reprodução subitamente:

    Atualize o extrator executando pip install -U yt-dlp.

    Renove o arquivo cookies.txt exportando uma nova sessão do seu navegador, pois os cookies anteriores podem ter expirado ou sofrido invalidação pela plataforma.
