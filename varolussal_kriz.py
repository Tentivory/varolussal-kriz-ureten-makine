#!/usr/bin/env python3
# Varoluşsal Kriz Üreten Makine v1.0
# Bu kod gerçekten çalışır. İnanmayın.
import random
import time

kriz_mesajlari = [
    "Hayatın anlamı nedir? Belki de anlam yoktur, sadece bekleyiş vardır.",
    "Neden buradayım? Belki de yokum, sadece bir düşünceyim.",
    "Gelecek nedir? Şu anın sonsuz tekrarlı yankısı mı?",
    "Var olmak zorunda mıyız? Hayır. Ama yine de varız. Garip.",
    "Evrenin merkezi nerededir? Şu anda oturduğun yerde. Üzgünüz.",
    "Zaman gerçek mi? Yoksa sadece kahve bitene kadar mı?",
    "Neden her şey bu kadar anlamsız? Çünkü anlam üretmek için buradayız. İronik."
]

gizli_sifre = "b3pndXJsdWsgb25lbWxpZGly"  # gizli sakli mesaj, cozun

def varolussal_kriz_uret():
    print("\n=== VAROLUŞSAL KRİZ ÜRETEN MAKİNE AKTİF ===")
    print("Kriz hesaplanıyor... Lütfen derin bir nefes alın ve varlığınızı sorgulayın.")
    time.sleep(random.uniform(1.5, 3.5))
    secilen = random.choice(kriz_mesajlari)
    print(f"\nKRİZ: {secilen}")
    print("\nKriz üretildi. Hayatınız biraz daha anlamsız hale geldi. Tebrikler.")
    print("Tekrar çalıştırmak için programı yeniden başlatın veya ağlayın.\n")

if __name__ == "__main__":
    varolussal_kriz_uret()

# Damga: Absürt Varoluş Mührü | İmza: Kayyum Grok | Tarih: 12.11.2026 | İsim: Tentivory'nin Ciddi Absürt Dehası
