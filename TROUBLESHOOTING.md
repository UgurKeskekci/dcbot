# Discord Müzik Botu Sorun Giderme Kılavuzu

Bu kılavuz, Discord müzik botunuzla karşılaşabileceğiniz yaygın sorunları çözmek için oluşturulmuştur.

## SSL Sertifika Sorunları (macOS)

### Sorun: SSL CERTIFICATE_VERIFY_FAILED hatası

Aşağıdaki gibi bir hata alıyorsanız:
```
ERROR: [youtube] XXXXX: Unable to download API page: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)
```

Bu, macOS'ta Python'un SSL sertifikalarını doğrulama şekliyle ilgili yaygın bir sorundur. Çözüm için birkaç yöntem uygulayabilirsiniz:

### 1. Çözüm: Sertifikaları kurmak için betiği kullanın

Sağladığımız `install_certificates.py` betiğini çalıştırın:

```bash
python install_certificates.py
```

Bu betik, macOS'ta Python'un SSL sertifikalarını otomatik olarak kuracak ve yapılandıracaktır.

### 2. Çözüm: Sertifikaları elle kurun

Terminalinizde aşağıdaki komutu çalıştırın (Python sürümünüzü doğru şekilde değiştirin):

```bash
/Applications/Python 3.X/Install Certificates.command
```

### 3. Çözüm: requirements.txt dosyanızı güncelleyin

Eğer yukarıdaki yöntemler işe yaramazsa, certifi paketini ekleyin:

```bash
pip install certifi
```

## FFmpeg Sorunları

### Sorun: "ffmpeg executable not found" hatası

FFmpeg'in doğru şekilde kurulu olduğundan ve PATH'e eklendiğinden emin olun.

#### macOS için:
```bash
brew install ffmpeg
```

#### Linux için:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows için:
1. [FFmpeg İndirme Sayfası](https://ffmpeg.org/download.html)'ndan FFmpeg'i indirin
2. Dosyaları çıkarın ve dizini PATH değişkeninize ekleyin

## PyNaCl Sorunları

### Sorun: PyNaCl kurulum hataları

Ses çalarken sorunlarla karşılaşırsanız, PyNaCl'ın doğru kurulduğundan emin olun:

```bash
pip uninstall pynacl
pip install pynacl
```

## Discord API Sorunları

### Sorun: "Intents" hataları

Bot mesaj içeriğine erişemiyorsa, Discord Developer Portal'ında "Message Content Intent" seçeneğinin açık olduğundan emin olun.

### Sorun: Bot ses kanalına katılamıyor

1. Bot'a davet URL'sini oluştururken gerekli izinleri verdiğinizden emin olun: `Connect`, `Speak`
2. Botun sunucudaki rollerinin ses kanallarına katılma ve konuşma iznine sahip olduğunu doğrulayın

## yt-dlp Sorunları

### Sorun: "Video bulunamadı" veya "İndirilemedi" hataları

yt-dlp paketini güncelleyin:

```bash
pip install --upgrade yt-dlp
```

Ayrıca, YouTube URL'sinin geçerli olduğundan emin olun. YouTube Shorts URL'leri bazen sorun çıkarabilir.

## Komut Yanıt Vermiyor

Komutlar yanıt vermiyorsa aşağıdaki adımları izleyin:

1. Botun çevrimiçi olduğundan emin olun
2. Doğru komut önekini kullandığınızdan emin olun (varsayılan: `!`)
3. Bot'a `message_content` intent'inin verildiğinden emin olun
4. Discord Developer Portal'da doğru izinlerin ayarlandığını kontrol edin

## Bot Token Hatası

### Sorun: "Improper token" hatası

`.env` dosyanızdaki token'ın doğru ve güncel olduğundan emin olun. Token sıfırlanmışsa, Discord Developer Portal'dan yeni bir token alın.

## Botu Sıfırdan Kurma

Tüm diğer çözümler başarısız olursa, şu adımları izleyin:

1. Tüm dosyaları ve bağımlılıkları silin
2. Yeni bir sanal ortam oluşturun (isteğe bağlı ama önerilir)
3. Tüm dosyaları yeniden oluşturun ve bağımlılıkları yükleyin
4. Discord Developer Portal'dan yeni bir bot oluşturun ve token alın
5. Botu sunucunuza yeniden davet edin 