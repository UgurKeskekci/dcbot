# Discord Müzik Botu

Bu bot, Discord sunucunuzda YouTube üzerinden müzik çalmanızı sağlar.

## Kurulum

1. Python 3.8 veya daha yeni bir sürümü yükleyin.
2. Bu repoyu bilgisayarınıza indirin.
3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. FFmpeg'i yükleyin:
   - Windows: [FFmpeg indirme sayfası](https://ffmpeg.org/download.html)
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

5. Discord Developer Portal'dan bir bot oluşturun:
   - [Discord Developer Portal](https://discord.com/developers/applications)'a gidin.
   - "New Application" butonuna tıklayın.
   - Botunuza bir isim verin ve "Create" butonuna tıklayın.
   - Soldaki menüden "Bot" sekmesine gidin ve "Add Bot" butonuna tıklayın.
   - "Reset Token" butonuna tıklayarak bot tokeninizi alın ve güvenli bir yerde saklayın.
   - "MESSAGE CONTENT INTENT" seçeneğini açmayı unutmayın.

6. Bot tokeninizi `.env` dosyasına ekleyin:
   ```
   TOKEN=your_discord_bot_token_here
   ```

7. Botunuzu Discord sunucunuza davet edin:
   - Developer Portal'da "OAuth2" > "URL Generator" sekmesine gidin.
   - "Scopes" kısmında "bot" seçeneğini işaretleyin.
   - "Bot Permissions" kısmında "Send Messages", "Connect", "Speak", "Manage Messages" gibi gerekli izinleri seçin.
   - Oluşturulan URL'yi kopyalayın ve tarayıcınızda açın.
   - Botunuzu eklemek istediğiniz sunucuyu seçin ve "Authorize" butonuna tıklayın.

## Kullanım

Botunuzu çalıştırmak için:
```bash
python main.py
```

### Komutlar

- `!join` - Bulunduğunuz ses kanalına katılır.
- `!leave` - Ses kanalından ayrılır.
- `!play [youtube-url]` - Belirtilen YouTube URL'sinden müzik çalar.
- `!pause` - Çalan müziği duraklatır.
- `!resume` - Duraklatılmış müziği devam ettirir.
- `!stop` - Müziği durdurur.
- `!clear [amount]` - Belirtilen sayıda mesajı siler (varsayılan: 5).

## Gereksinimler

- Python 3.8+
- discord.py
- python-dotenv
- yt-dlp
- PyNaCl
- FFmpeg

## Sorun Giderme

1. **Ses gelmiyor**: FFmpeg'in doğru kurulduğundan emin olun ve PATH değişkenlerinize eklendiğini kontrol edin.
2. **Bot komutlara yanıt vermiyor**: MESSAGE CONTENT INTENT'in açık olduğundan emin olun.
3. **Bağlantı hataları**: Internet bağlantınızı kontrol edin ve YouTube'un erişilebilir olduğundan emin olun. 