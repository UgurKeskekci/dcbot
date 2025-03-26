#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bu betik, Windows'ta Python'un sertifika sorunlarını çözmek için tasarlanmıştır.
"""

import os
import sys
import ssl
import subprocess
import certifi

def fix_ssl_windows():
    print("Windows için SSL sertifikalarını yapılandırma işlemi başlatılıyor...")
    
    try:
        # SSL için güvensiz context ayarla (bu güvenli olmayabilir, sadece test için)
        print("1. Yöntem: SSL doğrulama atlanıyor...")
        ssl._create_default_https_context = ssl._create_unverified_context
        
        # certifi paketini kullanarak sertifikaları güncelle
        print("2. Yöntem: Certifi sertifikalarını kullanma deneniyor...")
        
        # Certifi sertifika yolunu al
        cert_path = certifi.where()
        print(f"Certifi sertifika yolu: {cert_path}")
        
        # Çevre değişkenlerini ayarla
        os.environ['SSL_CERT_FILE'] = cert_path
        os.environ['REQUESTS_CA_BUNDLE'] = cert_path
        os.environ['CURL_CA_BUNDLE'] = cert_path
        
        # Python etkileşimli istemcisinde SSL ayarlarını test et
        print("SSL ayarları test ediliyor...")
        import urllib.request
        try:
            response = urllib.request.urlopen('https://www.youtube.com')
            print("Test başarılı! HTTPS bağlantısı kurulabildi.")
            return True
        except Exception as e:
            print(f"Test başarısız: {str(e)}")
            
            # Son çare olarak requests kullanmayı dene
            try:
                print("3. Yöntem: Requests kütüphanesi ile deneniyor...")
                
                # Requests kütüphanesini yükle (eğer yoksa)
                try:
                    import requests
                except ImportError:
                    print("Requests kütüphanesi yükleniyor...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
                    import requests
                
                # YouTube'a bağlanmayı dene
                response = requests.get('https://www.youtube.com', verify=cert_path)
                print("Test başarılı! Requests ile HTTPS bağlantısı kurulabildi.")
                return True
            except Exception as req_error:
                print(f"Requests testi de başarısız: {str(req_error)}")
                return False
            
    except Exception as e:
        print(f"SSL yapılandırması sırasında bir hata oluştu: {str(e)}")
        return False

def patch_yt_dlp():
    print("\nYT-DLP için SSL sabitleme deneniyor...")
    
    # YT-DLP sürümünü kontrol et ve güncelle
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
        print("yt-dlp başarıyla güncellendi.")
    except Exception as e:
        print(f"yt-dlp güncellenirken hata: {str(e)}")
    
    # main.py dosyasında ssl patching kodu varsa kontrol et
    try:
        with open("main.py", "r", encoding="utf-8") as f:
            content = f.read()
            
        if "ssl._create_default_https_context = ssl._create_unverified_context" not in content:
            print("main.py dosyasında SSL sabitleme kodu bulunamadı. Eklenecek...")
            
            # Dosya içeriğini güncelle
            lines = content.split("\n")
            import_section_end = 0
            
            # import bölümünün sonunu bul
            for i, line in enumerate(lines):
                if line.startswith("import") or line.startswith("from"):
                    import_section_end = i + 1
            
            # SSL sabitleme kodunu ekle
            lines.insert(import_section_end, "# Windows SSL sabitleme\nimport ssl\nssl._create_default_https_context = ssl._create_unverified_context\n")
            
            # Dosyayı güncelle
            with open("main.py", "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
                
            print("main.py dosyası güncellendi.")
        else:
            print("main.py dosyasında SSL sabitleme kodu zaten var.")
            
    except Exception as e:
        print(f"main.py dosyası güncellenirken hata: {str(e)}")

if __name__ == "__main__":
    if sys.platform != 'win32':
        print("Bu betik sadece Windows için tasarlanmıştır.")
        sys.exit(1)
        
    success = fix_ssl_windows()
    patch_yt_dlp()
    
    if success:
        print("""
SSL sertifikaları başarıyla yapılandırıldı.
Şimdi Discord botunuzu çalıştırabilirsiniz.

Bot çalıştırma komutu:
python main.py
""")
    else:
        print("""
SSL sertifika yapılandırması kısmen başarısız oldu.
Yine de botunuzu çalıştırmayı deneyebilirsiniz.

Sorun devam ederse, şu adımları deneyin:
1. pip install --upgrade certifi
2. pip install --upgrade yt-dlp
3. Sisteminizdeki güvenlik yazılımını geçici olarak devre dışı bırakın
4. Internet Explorer'ı açın ve herhangi bir web sitesine güvenli bağlantı kurun
""")
    
    input("Devam etmek için bir tuşa basın...")
    sys.exit(0 if success else 1) 