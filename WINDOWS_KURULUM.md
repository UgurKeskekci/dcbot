# Windows için Discord Müzik Botu Kurulum Rehberi

Bu rehber, Discord müzik botunuzu Windows üzerinde çalıştırmak için gerekli adımları içerir.

## Ön Gereksinimler

1. **Python Yükleme**
   - [Python web sitesinden](https://www.python.org/downloads/windows/) en son Python sürümünü indirin (Python 3.8 veya üzeri önerilir).
   - Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın!
   - Kurulum tamamlandıktan sonra komut istemini açın ve `python --version` komutunu çalıştırarak Python'un doğru kurulduğunu doğrulayın.

2. **FFmpeg Yükleme**
   - [FFmpeg web sitesinden](https://ffmpeg.org/download.html) FFmpeg'in Windows sürümünü indirin.
   - İndirdiğiniz dosyayı bir klasöre çıkarın (örneğin: `C:\FFmpeg`).
   - FFmpeg'i sistem PATH'inize ekleyin:
     1. Windows arama çubuğunda "Ortam Değişkenleri" yazın ve "Sistem ortam değişkenlerini düzenle" seçeneğine tıklayın.
     2. "Gelişmiş" sekmesinde, "Ortam Değişkenleri" butonuna tıklayın.
     3. "Sistem değişkenleri" bölümünde, "Path" değişkenini bulun ve "Düzenle" butonuna tıklayın.
     4. "Yeni" butonuna tıklayın ve FFmpeg'in bin klasörünün yolunu ekleyin (örneğin: `C:\FFmpeg\bin`).
     5. "Tamam" butonlarına tıklayarak tüm pencereleri kapatın.
     6. Komut istemini yeniden başlatın ve `ffmpeg -version` komutunu çalıştırarak FFmpeg'in doğru kurulduğunu doğrulayın.

## Bot Kurulumu

1. **Dosyaları İndirin veya Kopyalayın**
   - Bot dosyalarını (main.py, requirements.txt, vb.) bilgisayarınıza kopyalayın.

2. **Bot Token'ını Ayarlayın**
   - `.env` dosyasını açın ve `TOKEN=your_discord_bot_token_here` satırındaki "your_discord_bot_token_here" kısmını Discord Developer Portal'dan aldığınız gerçek bot token'ı ile değiştirin.

3. **Otomatik Kurulum ve Çalıştırma**
   - Hazırladığımız `start_bot.bat` dosyasını çift tıklayarak çalıştırın. Bu betik:
     - Gerekli paketleri otomatik olarak yükleyecek
     - SSL sertifika sorunlarını düzeltmeye çalışacak
     - Bot'u başlatacak

   Veya aşağıdaki adımları manuel olarak izleyebilirsiniz:

4. **Manuel Kurulum (İsteğe Bağlı)**
   - Komut istemini açın ve bot dosyalarının bulunduğu klasöre gidin.
   - Gerekli paketleri yükleyin:
     ```
     pip install -r requirements.txt
     ```
   - SSL sertifika sorunlarını çözmek için SSL düzeltme betiğini çalıştırın:
     ```
     python fix_ssl_windows.py
     ```
   - Bot'u başlatın:
     ```
     python main.py
     ```

## SSL Sertifika Sorunları

Windows'ta SSL sertifika sorunlarıyla karşılaşırsanız:

1. `fix_ssl_windows.py` betiğini çalıştırın:
   ```
   python fix_ssl_windows.py
   ```

2. Bu işe yaramazsa, aşağıdaki komutları deneyin:
   ```
   pip install --upgrade certifi
   pip install --upgrade yt-dlp
   ```

3. Internet Explorer (veya Microsoft Edge) tarayıcısını açın ve herhangi bir HTTPS sitesine gidin. Windows, sistem sertifikalarını güncellemeyi deneyecektir.

4. Güvenlik yazılımınızın SSL denetimini geçici olarak devre dışı bırakmayı deneyin.

## Bot Kullanımı

Bot çalıştıktan sonra, Discord sunucunuzda aşağıdaki komutları kullanabilirsiniz:

- `!join` - Bulunduğunuz ses kanalına katılır.
- `!leave` - Ses kanalından ayrılır.
- `!play [youtube-url]` - Belirtilen YouTube URL'sinden müzik çalar.
- `!pause` - Çalan müziği duraklatır.
- `!resume` - Duraklatılmış müziği devam ettirir.
- `!stop` - Müziği durdurur.
- `!clear [miktar]` - Belirtilen sayıda mesajı siler (varsayılan: 5).

## Sorun Giderme

Herhangi bir sorunla karşılaşırsanız:

1. `TROUBLESHOOTING.md` dosyasını kontrol edin.
2. FFmpeg'in doğru kurulu olduğundan ve PATH'e eklendiğinden emin olun.
3. Discord Developer Portal'da botunuzun "MESSAGE CONTENT INTENT" seçeneğinin açık olduğundan emin olun.
4. Botunuzun Discord sunucunuza doğru izinlerle davet edildiğinden emin olun. 