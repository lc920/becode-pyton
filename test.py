devise = (input("Votre devise est E ou $ ?"))

if devise == "E": 
    montant_e = float(input("Quel est votre montant en euros ? :"))
    taux_dollars = 1.09
    montant_dollars = montant_e * taux_dollars 
    print(f"{montant_e} euros équivalent a {montant_dollars} dollars")
elif devise == "$": 
     montant_dollars = float(input("Quel est votre montant en dollars ? :"))
     taux_euro = 0.91
     montant_e = montant_dollars / taux_euro
     print(f"{montant_dollars} dollars équivalent a {montant_e} euros")
     
else: 
     print("choix de devises non valide")

