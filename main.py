import os
import asyncio
import discord
import ssl
import certifi
from discord.ext import commands
from dotenv import load_dotenv
import yt_dlp as youtube_dl

# Load environment variables
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot with prefix '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# YouTube DL options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # Bind to IPv4
}

ffmpeg_options = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
}

# SSL ayarını yap
ssl._create_default_https_context = ssl._create_unverified_context

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        
        try:
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
            
            if 'entries' in data:
                # Take first item from a playlist
                data = data['entries'][0]
                
            filename = data['url'] if stream else ytdl.prepare_filename(data)
            return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
        except Exception as e:
            print(f"Error extracting info: {str(e)}")
            raise e

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

@bot.command(name='join', help='Bot katılır ses kanalına')
async def join(ctx):
    if not ctx.message.author.voice:
        return await ctx.send("Bir ses kanalında değilsiniz!")
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    
    await channel.connect()
    await ctx.send(f"{channel} kanalına katıldım!")

@bot.command(name='leave', help='Bot ses kanalından ayrılır')
async def leave(ctx):
    if ctx.voice_client is None:
        return await ctx.send("Bir ses kanalında değilim!")
    
    await ctx.voice_client.disconnect()
    await ctx.send("Ses kanalından ayrıldım!")

@bot.command(name='play', help='YouTube linkinden müzik çalar')
async def play(ctx, url):
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            return await ctx.send("Bir ses kanalında değilsiniz!")
    
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    
    async with ctx.typing():
        try:
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
            await ctx.send(f'Şimdi çalıyor: {player.title}')
        except Exception as e:
            await ctx.send(f"Müzik çalınırken bir hata oluştu: {str(e)}")

@bot.command(name='pause', help='Müziği duraklatır')
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Müzik duraklatıldı!")
    else:
        await ctx.send("Şu anda müzik çalmıyor!")

@bot.command(name='resume', help='Duraklatılmış müziği devam ettirir')
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Müzik devam ediyor!")
    else:
        await ctx.send("Müzik duraklatılmadı!")

@bot.command(name='stop', help='Müziği durdurur')
async def stop(ctx):
    if ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused()):
        ctx.voice_client.stop()
        await ctx.send("Müzik durduruldu!")
    else:
        await ctx.send("Şu anda müzik çalmıyor!")

@bot.command(name='clear', help='Belirtilen sayıda mesajı siler')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)  # +1 to include the command itself
    await ctx.send(f"{amount} mesaj silindi!", delete_after=5)

# Run the bot with the token from .env file
bot.run(os.getenv('TOKEN')) 