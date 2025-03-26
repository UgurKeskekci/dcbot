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

:: FFmpeg'in kurulu olup olmadığını kontrol et
where ffmpeg >nul 2>&1
if %errorlevel% neq 0 (
    echo UYARI: FFmpeg bulunamadi! 
    echo Muzik ozellikleri calismayabilir.
    echo FFmpeg'i indirip PATH'e eklemelisiniz.
    echo https://ffmpeg.org/download.html
    echo.
    echo Devam etmek istiyor musunuz? (Y/N)
    set /p choice=
    if /i not "%choice%"=="Y" (
        exit /b 1
    )
)

:: Bağımlılıkları kontrol et ve yükle
echo Bagimliliklar kontrol ediliyor...
python -c "import discord" >nul 2>&1
if %errorlevel% neq 0 (
    echo discord.py yuklenmiyor. Yukleniyor...
    pip install discord.py[voice]
)

python -c "import dotenv" >nul 2>&1
if %errorlevel% neq 0 (
    echo python-dotenv yuklenmiyor. Yukleniyor...
    pip install python-dotenv
)

python -c "import yt_dlp" >nul 2>&1
if %errorlevel% neq 0 (
    echo yt-dlp yuklenmiyor. Yukleniyor...
    pip install yt-dlp
)

python -c "import nacl" >nul 2>&1
if %errorlevel% neq 0 (
    echo PyNaCl yuklenmiyor. Yukleniyor...
    pip install PyNaCl
)

:: Windows için SSL sorunu giderme
echo.
echo Windows'ta SSL sertifika sorunlarini gidermek icin ek ayarlar yapiliyor...

:: Windows için SSL sabitleme dosyası
echo import os > fix_ssl.py
echo import ssl >> fix_ssl.py
echo import certifi >> fix_ssl.py
echo. >> fix_ssl.py
echo print("Windows icin SSL sertifika ayarlari guncelleniyor...") >> fix_ssl.py
echo # Varsayılan HTTPS context'i güncelle >> fix_ssl.py
echo ssl._create_default_https_context = ssl._create_unverified_context >> fix_ssl.py
echo print("SSL ayarlari guncellendi.") >> fix_ssl.py

:: SSL sabitleme betiğini çalıştır
python fix_ssl.py

echo.
echo Bot baslatiliyor...
echo Cikis yapmak icin Ctrl+C tusuna basin.
echo.

:: Botu başlat
python main.py

:: Hata durumunda
if %errorlevel% neq 0 (
    echo Bot calisirken bir hata olustu.
    echo Daha fazla bilgi icin TROUBLESHOOTING.md dosyasini kontrol edin.
    pause
)

exit /b 0 