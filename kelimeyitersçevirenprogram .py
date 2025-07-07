#kelime çevirme programı

kelime = input("Kelime gir: ")
harf_listesi = list(kelime)      # String -> Liste
harf_listesi.reverse()           # Listeyi ters çevir
ters_kelime = "".join(harf_listesi)  # Liste -> String
print("Ters hali (listeyle):", ters_kelime)
