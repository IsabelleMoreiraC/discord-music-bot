import discord
import asyncio
import yt_dlp

def bot_start():

    # AVISO DE SEGURANÇA: Mantenha o token vazio no GitHub!
    TOKEN = ""  

    # Define as permissões básicas do bot
    intents = discord.Intents.default()
    intents.message_content = True  # Permite a leitura do conteúdo das mensagens

    # Instância principal do bot
    bot = discord.Client(intents=intents)
    
    # Dicionário para gerir as conexões de voz em múltiplos servidores
    voz_clients = {} 
    
    # Configurações de extração do yt-dlp
    yt_dl_options = {
        "format": "bestaudio/best",
        "cookiefile": "cookies.txt", # Lê o ficheiro de cookies para evitar bloqueios
        "noplaylist": True,          # Limita a reprodução a uma música por vez
        "nocheckcertificate": True,  # Ignora erros de certificados SSL
        "ignoreerrors": False,       # Para a execução se houver erro na extração
        "logtostderr": False,        # Oculta logs no terminal
        "quiet": True,               # Modo silencioso
        "no_warnings": True,         # Oculta avisos
        "default_search": "auto",    # Pesquisa o termo no YouTube se não for um link
        # Camufla o bot como um dispositivo móvel/TV para contornar verificações
        "extractor_args": {"youtube": {"client": "tv,android,ios"}} 
    }

    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    # Parâmetros do FFmpeg para processamento de áudio
    ffmpeg_options = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn -filter:a "volume=0.25"' # Remove o vídeo e ajusta o volume
    }

    @bot.event
    async def on_ready():
        print(f"{bot.user} está pronto para tocar!")

    @bot.event
    async def on_message(message):

        # Ignora mensagens enviadas por bots
        if message.author.bot:
            return
        
        # --- Comando !play ---
        if message.content.startswith("!play"):
            
            args = message.content.split()
            if len(args) < 2:
                await message.channel.send("Precisas de informar o nome da música ou o link!")
                return

            # Gestão da conexão ao canal de voz
            if message.guild.id in voz_clients and voz_clients[message.guild.id].is_connected():
                voice_client = voz_clients[message.guild.id]
            else:
                if not message.author.bot and message.author.voice and message.author.voice.channel:
                    voice_client = await message.author.voice.channel.connect()
                    voz_clients[message.guild.id] = voice_client
                else:
                    await message.channel.send("Precisas de estar num canal de voz para usar este comando.")
                    return

            search_query = " ".join(args[1:])
            print(f"A buscar: {search_query}")   

            loop = asyncio.get_event_loop()
            
            try:
                # Extrai as informações de forma assíncrona para não bloquear o bot
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(search_query, download=False))
            except Exception as e:
                await message.channel.send(f"Ocorreu um erro ao procurar a música: {e}")
                return

            if not data:
                await message.channel.send("Erro ao obter informações do vídeo.")
                return
            
            if "entries" in data and len(data["entries"]) > 0:
                data = data["entries"][0]
            
            song = data.get('url') 

            if not song:
                await message.channel.send("Erro ao processar o link direto do áudio.")
                return

            player = discord.FFmpegOpusAudio(song, **ffmpeg_options)

            # Para a reprodução atual se já houver algo a tocar
            if voice_client.is_playing():
                voice_client.stop()

            voice_client.play(player)
            await message.channel.send(f"A tocar agora: **{data.get('title', 'Música desconhecida')}**")

        # --- Comando !stop ---
        if message.content.startswith("!stop"):
            if message.guild.id in voz_clients:
                if voz_clients[message.guild.id].is_playing():
                    voz_clients[message.guild.id].stop()
                
                await voz_clients
