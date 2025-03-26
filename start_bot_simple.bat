@echo off
echo Discord Muzik Botu Baslatiliyor...
echo ===============================

:: Python'un kurulu olup olmadığını kontrol et
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python bulunamadi! Lutfen Python'u yukleyin.
    echo https://www.python.org/downloads/windows/
    pause
    exit /b 1
)

:: FFmpeg Kurulum Rehberi
echo.
echo =======================================================
echo FFMPEG KURULUM REHBERI
echo =======================================================
echo.
echo Discord muzik botu icin FFmpeg gereklidir.
echo.
echo FFmpeg kurulum adimlari:
echo 1. https://ffmpeg.org/download.html adresine gidin
echo 2. "Windows Builds" linkine tiklayin
echo 3. "gyan.dev" veya "BtbN" gibi bir Windows build sitesi secin
echo 4. "ffmpeg-release-essentials.zip" dosyasini indirin
echo 5. Dosyayi herhangi bir klasore cikartin (ornek: C:\ffmpeg)
echo 6. Cikardiginiz klasordeki "bin" klasorunun tam yolunu kopyalayin
echo.
echo Simdi bu yolu Windows PATH'ine ekleyelim:
echo 1. Windows arama cubuguna "Ortam Degiskenleri" yazin
echo 2. "Sistem ortam degiskenlerini duzenle" secenegine tiklayin
echo 3. "Ortam Degiskenleri" butonuna tiklayin
echo 4. "Sistem degiskenleri" bolumunde "Path" degiskenini secin ve "Duzenle" butonuna tiklayin
echo 5. "Yeni" butonuna tiklayin ve kopyaladiginiz bin klasorunun yolunu ekleyin
echo 6. Tamam butonlarina basin ve tum pencereleri kapatin
echo.
echo PATH'e ekledikten sonra, yeni bir Komut Istemi veya PowerShell penceresi acin
echo ve "ffmpeg -version" komutunu calistirarak kurulumu dogrulayin.
echo.
echo FFmpeg'i kurduktan sonra bu betiği tekrar calistirin.
echo =======================================================
echo.

:: FFmpeg'in kurulu olup olmadığını kontrol et
where ffmpeg >nul 2>&1
if %errorlevel% neq 0 (
    echo UYARI: FFmpeg bulunamadi! 
    echo Muzik ozellikleri calismayabilir.
    echo.
    echo Yine de devam etmek istiyor musunuz? (Y/N)
    set /p choice=
    if /i not "%choice%"=="Y" (
        exit /b 1
    )
)

:: Bağımlılıkları kontrol et ve yükle
echo Bagimliliklar kontrol ediliyor ve yukleniyor...
pip install discord.py[voice] python-dotenv yt-dlp PyNaCl

echo.
echo Bot baslatiliyor...
echo Cikis yapmak icin Ctrl+C tusuna basin.
echo.

:: Botu başlat
python main.py

:: Hata durumunda
if %errorlevel% neq 0 (
    echo Bot calisirken bir hata olustu.
    echo.
    echo Olası sorunlar ve çözümleri:
    echo 1. FFmpeg kurulu değil veya PATH'e eklenmemiş
    echo 2. .env dosyasında geçerli bir Discord bot token'ı yok
    echo 3. Discord botunuzun "Message Content Intent" izni açık değil
    echo.
    pause
)

exit /b 0 