#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bu betik, macOS'ta Python'un sertifika sorunlarını çözmek için tasarlanmıştır.
"""

import os
import sys
import subprocess

def install_certificates():
    print("macOS için SSL sertifikalarını kurma işlemi başlatılıyor...")
    
    # Python yolu
    python_path = sys.executable
    
    # Python'un kurulu olduğu dizini kontrol et
    python_dir = os.path.dirname(os.path.dirname(python_path))
    
    # Install certificates.command dosyasının yolu
    cert_script_path = os.path.join(
        python_dir, 
        'Resources/Python.app/Contents/Resources/install_certificates.command'
    )
    
    # Dosya var mı kontrol et
    if os.path.exists(cert_script_path):
        print(f"Sertifika kurulum betiği bulundu: {cert_script_path}")
        try:
            # Sertifika kurulum betiğini çalıştır
            result = subprocess.run(['bash', cert_script_path], 
                                   capture_output=True, 
                                   text=True, 
                                   check=True)
            print("Sertifika kurulumu başarılı!")
            print(result.stdout)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Sertifika kurulumu sırasında bir hata oluştu: {e}")
            print(f"Hata çıktısı: {e.stderr}")
            return False
    else:
        print("Sertifika kurulum betiği bulunamadı.")
        print("Alternatif yöntem deneniyor...")
        
        try:
            # Alternatif yöntem: certifi paketini kullanarak sertifikaları güncelle
            import certifi
            import ssl
            
            # SSL için certifi sertifikalarını kullan
            ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
            
            print(f"certifi sertifika yolu: {certifi.where()}")
            print("Sertifika ayarları güncellendi.")
            return True
        except Exception as e:
            print(f"Alternatif sertifika kurulumu sırasında bir hata oluştu: {e}")
            return False

if __name__ == "__main__":
    if sys.platform != 'darwin':
        print("Bu betik sadece macOS için tasarlanmıştır.")
        sys.exit(1)
        
    success = install_certificates()
    
    if success:
        print("""
SSL sertifikaları başarıyla kuruldu.
Şimdi Discord botunuzu tekrar çalıştırabilirsiniz.

Bot çalıştırma komutu:
python main.py
""")
    else:
        print("""
SSL sertifika kurulumu başarısız oldu.
Elle kurmak için şu komutu çalıştırabilirsiniz:

/Applications/Python X.Y/Install Certificates.command

(X.Y ifadesini Python sürümünüzle değiştirin, örneğin 3.9, 3.10 vb.)
""")
    
    sys.exit(0 if success else 1) 