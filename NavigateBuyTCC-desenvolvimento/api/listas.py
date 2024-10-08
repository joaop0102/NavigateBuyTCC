import json
import os

project_root = os.path.dirname(os.path.abspath(__file__))

# Categoria Acessorios
Acessorios1_path = os.path.join(project_root, 'scrapy', 'americanas',  'data',  'acessorio.json')
Acessorios2_path = os.path.join(project_root, 'scrapy', 'centauro',  'data',  'acessorio.json')
Acessorios3_path = os.path.join(project_root, 'scrapy', 'marisa',  'data',  'acessorio.json')
Acessorios4_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Acessorios.json')
Acessorio5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Acessorio.json')
Acessorio6_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Acessorio.json')
Acessorio7_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Acessorio.json')
Acessorio8_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Acessorio.json')

# Categoria Bebes
bbs1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'bebes.json')
bbs2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Bebes.json')
bbs3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Bebes.json')
bbs4_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Bebes.json')
bbs5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Bebes.json')
bbs6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Bebes.json')
bbs7_path = os.path.join(project_root, 'scrapy', 'oboticario', 'data', 'Bebes.json')

# Categoria Beleza
blz1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'beleza.json')
blz2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Beleza.json')
blz3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Beleza.json')
blz4_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Beleza.json')
blz5_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Beleza.json')
blz6_path = os.path.join(project_root, 'scrapy', 'oboticario', 'data', 'Beleza.json')
blz7_path = os.path.join(project_root, 'scrapy', 'ultrafarma', 'data', 'beleza.json')

# Categoria Decoracao
decoracao1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'decoracao.json')
decoracao2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Decoracao.json')
decoracao3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Decoracao.json')
decoracao4_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Decoracao.json')
decoracao5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Decoracao.json')
decoracao6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Decoracao.json')
decoracao7_path = os.path.join(project_root, 'scrapy', 'marisa', 'data', 'decoracao.json')

# Categoria Eletrodomestico
eletrodomestico1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'eletrodomestico.json')
eletrodomestico2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Eletrodomestico.json')
eletrodomestico3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Eletrodomestico.json')
eletrodomestico4_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Eletrodomestico.json')
eletrodomestico5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Eletrodomestico.json')
eletrodomestico6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Eletrodomestico.json')

# Categoria Esporte
esporte1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'esporte.json')
esporte2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Esporte.json')
esporte3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Esporte.json')
esporte4_path = os.path.join(project_root, 'scrapy', 'centauro', 'data', 'esporte.json')
esporte5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Esporte.json')
esporte6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Esporte.json')

# Categoria Informatica
informatica1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'informatica.json')
informatica2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Informatica.json')
informatica3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Informatica.json')
informatica4_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Informatica.json')
informatica5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Informatica.json')
informatica5_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Informatica.json')

# Categoria Lazer
lazer1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'lazer.json')
lazer2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Lazer.json')
lazer3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Lazer.json')
lazer4_path = os.path.join(project_root, 'scrapy', 'centauro', 'data', 'lazer.json')
lazer5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Lazer.json')
lazer6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Lazer.json')

# Categoria Mercado e Farmacia
mf1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'MF.json')
mf2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Mercado_Farmacia.json')
mf3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Mercado_Farmacia.json')
mf4_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Mercado_Farmacia.json')
mf5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Mercado_Farmacia.json')
mf6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Mercado_Farmacia.json')

# Categoria Papelaria
papel1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'papelaria.json')
papel2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Papelaria.json')
papel3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Papelaria.json')
papel4_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Papelaria.json')
papel1_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Papelaria.json')
papel1_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Papelaria.json')

# Categoria Pets
pets1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'pet.json')
pets2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Pets.json')
pets3_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Pets.json')
pets4_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Pets.json')
pets5_path = os.path.join(project_root, 'scrapy', 'oboticario', 'data', 'Pets.json')

# Categoria Roupas
roupas1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'roupa.json')
roupas2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Roupas.json')
roupas3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Roupas.json')
roupas4_path = os.path.join(project_root, 'scrapy', 'centauro', 'data', 'roupa.json')
roupas5_path = os.path.join(project_root, 'scrapy', 'kalunga', 'data', 'Roupas.json')
roupas6_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Roupas.json')
roupas7_path = os.path.join(project_root, 'scrapy', 'marisa', 'data', 'roupa.json')
roupas8_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Roupa.json')

# Categoria Sapato
sapato1_path = os.path.join(project_root, 'scrapy', 'americanas', 'data', 'sapato.json')
sapato2_path = os.path.join(project_root, 'scrapy', 'casasbahia', 'data', 'Sapato.json')
sapato3_path = os.path.join(project_root, 'scrapy', 'CEA', 'data', 'Sapato.json')
sapato4_path = os.path.join(project_root, 'scrapy', 'centauro', 'data', 'sapato.json')
sapato5_path = os.path.join(project_root, 'scrapy', 'magazineJP', 'data', 'Sapato.json')
sapato6_path = os.path.join(project_root, 'scrapy', 'mercadolivre', 'data', 'Sapato.json')

# Categoria Remedios
remedios1_path = os.path.join(project_root, 'scrapy', 'ultrafarma', 'data', 'medicamentos.json')



# Acessorios
try:
    with open(Acessorios1_path, 'r', encoding='utf-8') as f1, \
        open(Acessorios2_path, 'r', encoding='utf-8') as f2, \
        open(Acessorios3_path, 'r', encoding='utf-8') as f3, \
        open(Acessorios4_path, 'r', encoding='utf-8') as f4, \
        open(Acessorio5_path, 'r', encoding='utf-8')as f5, \
        open(Acessorio6_path, 'r', encoding='utf-8') as f6, \
        open(Acessorio7_path, 'r', encoding='utf-8') as f7, \
        open(Acessorio8_path, 'r', encoding='utf-8') as f8:
        
        acessorios1 = json.load(f1)
        acessorios2 = json.load(f2)
        acessorios3 = json.load(f3)
        acessorios4 = json.load(f4)
        acessorios5 = json.load(f5)
        acessorios6 = json.load(f6)
        acessorios7 = json.load(f7)
        acessorios8 = json.load(f8)
    
    if isinstance(acessorios1, dict) and \
        isinstance(acessorios2, dict) and \
        isinstance(acessorios3, dict) and \
        isinstance(acessorios4, dict) and \
        isinstance(acessorios5, dict) and \
        isinstance(acessorios6, dict) and \
        isinstance(acessorios7, dict) and \
        isinstance(acessorios8, dict):
        data = {**acessorios1, **acessorios2, **acessorios3, **acessorios4, **acessorios5, **acessorios6,
                **acessorios7, **acessorios8}
    elif isinstance(acessorios1, list) and \
        isinstance(acessorios2, list) and \
        isinstance(acessorios3, list) and \
        isinstance(acessorios4, list) and \
        isinstance(acessorios5, list) and \
        isinstance(acessorios6, list) and \
        isinstance(acessorios7, list) and \
        isinstance(acessorios8, list):
        data = acessorios1 + acessorios2 + acessorios3 + acessorios4 + acessorios5 + acessorios6 + acessorios7 + acessorios8
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Acessorios.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Bebes
try:
    with open(bbs1_path, 'r', encoding='utf-8') as f1, \
        open(bbs2_path, 'r', encoding='utf-8') as f2, \
        open(bbs3_path, 'r', encoding='utf-8') as f3, \
        open(bbs4_path, 'r', encoding='utf-8') as f4, \
        open(bbs5_path, 'r', encoding='utf-8')as f5, \
        open(bbs6_path, 'r', encoding='utf-8') as f6, \
        open(bbs7_path, 'r', encoding='utf-8') as f7:
        
        bb1 = json.load(f1)
        bb2 = json.load(f2)
        bb3 = json.load(f3)
        bb4 = json.load(f4)
        bb5 = json.load(f5)
        bb6 = json.load(f6)
        bb7 = json.load(f7)
    
    if isinstance(bb1, dict) and \
        isinstance(bb2, dict) and \
        isinstance(bb3, dict) and \
        isinstance(bb4, dict) and \
        isinstance(bb5, dict) and \
        isinstance(bb6, dict) and \
        isinstance(bb7, dict):
        data = {**bb1, **bb2, **bb3, **bb4, **bb5, **bb6,
                **bb7}
    elif isinstance(bb1, list) and \
        isinstance(bb2, list) and \
        isinstance(bb3, list) and \
        isinstance(bb4, list) and \
        isinstance(bb5, list) and \
        isinstance(bb6, list) and \
        isinstance(bb7, list):
        data = bb1 + bb2 + bb3 + bb4 + bb5 + bb6 + bb7
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Bebes.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}") 


# Beleza
try:
    with open(blz1_path, 'r', encoding='utf-8') as f1, \
        open(blz2_path, 'r', encoding='utf-8') as f2, \
        open(blz3_path, 'r', encoding='utf-8') as f3, \
        open(blz4_path, 'r', encoding='utf-8') as f4, \
        open(blz5_path, 'r', encoding='utf-8')as f5, \
        open(blz6_path, 'r', encoding='utf-8') as f6, \
        open(blz7_path, 'r', encoding='utf-8') as f7:
        
        blz1 = json.load(f1)
        blz2 = json.load(f2)
        blz3 = json.load(f3)
        blz4 = json.load(f4)
        blz5 = json.load(f5)
        blz6 = json.load(f6)
        blz7 = json.load(f7)
    
    if isinstance(blz1, dict) and \
        isinstance(blz2, dict) and \
        isinstance(blz3, dict) and \
        isinstance(blz4, dict) and \
        isinstance(blz5, dict) and \
        isinstance(blz6, dict) and \
        isinstance(blz7, dict):
        data = {**blz1, **blz2, **blz3, **blz4, **blz5, **blz6,
                **blz7}
    elif isinstance(blz1, list) and \
        isinstance(blz2, list) and \
        isinstance(blz3, list) and \
        isinstance(blz4, list) and \
        isinstance(blz5, list) and \
        isinstance(blz6, list) and \
        isinstance(blz7, list):
        data = blz1 + blz2 + blz3 + blz4 + blz5 + blz6 + blz7 
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Beleza.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Decoracao
try:
    with open(decoracao1_path, 'r', encoding='utf-8') as f1, \
        open(decoracao2_path, 'r', encoding='utf-8') as f2, \
        open(decoracao3_path, 'r', encoding='utf-8') as f3, \
        open(decoracao4_path, 'r', encoding='utf-8') as f4, \
        open(decoracao5_path, 'r', encoding='utf-8')as f5, \
        open(decoracao6_path, 'r', encoding='utf-8') as f6, \
        open(decoracao7_path, 'r', encoding='utf-8') as f7:
        
        deco1 = json.load(f1)
        deco2 = json.load(f2)
        deco3 = json.load(f3)
        deco4 = json.load(f4)
        deco5 = json.load(f5)
        deco6 = json.load(f6)
        deco7 = json.load(f7)
    
    if isinstance(deco1, dict) and \
        isinstance(deco2, dict) and \
        isinstance(deco3, dict) and \
        isinstance(deco4, dict) and \
        isinstance(deco5, dict) and \
        isinstance(deco6, dict) and \
        isinstance(deco7, dict):
        data = {**deco1, **deco2, **deco3, **deco4, **deco5, **deco6, **deco7}
    elif isinstance(deco1, list) and \
        isinstance(deco2, list) and \
        isinstance(deco3, list) and \
        isinstance(deco4, list) and \
        isinstance(deco5, list) and \
        isinstance(deco6, list) and \
        isinstance(deco7, list):
        data = deco1 + deco2 + deco3 + deco4 + deco5 + deco6 + deco7
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Decoracao.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}") 


# Eletrodomestico
try:
    with open(eletrodomestico1_path, 'r', encoding='utf-8') as f1, \
        open(eletrodomestico2_path, 'r', encoding='utf-8') as f2, \
        open(eletrodomestico3_path, 'r', encoding='utf-8') as f3, \
        open(eletrodomestico4_path, 'r', encoding='utf-8') as f4, \
        open(eletrodomestico5_path, 'r', encoding='utf-8')as f5, \
        open(eletrodomestico6_path, 'r', encoding='utf-8') as f6:
        
        eletro1 = json.load(f1)
        eletro2 = json.load(f2)
        eletro3 = json.load(f3)
        eletro4 = json.load(f4)
        eletro5 = json.load(f5)
        eletro6 = json.load(f6)
    
    if isinstance(eletro1, dict) and \
        isinstance(eletro2, dict) and \
        isinstance(eletro3, dict) and \
        isinstance(eletro4, dict) and \
        isinstance(eletro5, dict) and \
        isinstance(eletro6, dict):
        data = {**eletro1, **eletro2, **eletro3, **eletro4, **eletro5, **eletro6}
    elif isinstance(eletro1, list) and \
        isinstance(eletro2, list) and \
        isinstance(eletro3, list) and \
        isinstance(eletro4, list) and \
        isinstance(eletro5, list) and \
        isinstance(eletro6, list):
        data = eletro1 + eletro2 + eletro3 + eletro4 + eletro5 + eletro6
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Eletrodomestico.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")



# Esporte
try:
    with open(esporte1_path, 'r', encoding='utf-8') as f1, \
        open(esporte2_path, 'r', encoding='utf-8') as f2, \
        open(esporte3_path, 'r', encoding='utf-8') as f3, \
        open(esporte4_path, 'r', encoding='utf-8') as f4, \
        open(esporte5_path, 'r', encoding='utf-8')as f5, \
        open(esporte6_path, 'r', encoding='utf-8') as f6:
        
        esp1 = json.load(f1)
        esp2 = json.load(f2)
        esp3 = json.load(f3)
        esp4 = json.load(f4)
        esp5 = json.load(f5)
        esp6 = json.load(f6)
    
    if isinstance(esp1, dict) and \
        isinstance(esp2, dict) and \
        isinstance(esp3, dict) and \
        isinstance(esp4, dict) and \
        isinstance(esp5, dict) and \
        isinstance(esp6, dict):
        data = {**esp1, **esp2, **esp3, **esp4, **esp5, **esp6}
    elif isinstance(esp1, list) and \
        isinstance(esp2, list) and \
        isinstance(esp3, list) and \
        isinstance(esp4, list) and \
        isinstance(esp5, list) and \
        isinstance(esp6, list):
        data = esp1 + esp2 + esp3 + esp4 + esp5 + esp6
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Esporte.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Informatica
try:
    with open(informatica1_path, 'r', encoding='utf-8') as f1, \
        open(informatica2_path, 'r', encoding='utf-8') as f2, \
        open(informatica3_path, 'r', encoding='utf-8') as f3, \
        open(informatica4_path, 'r', encoding='utf-8') as f4, \
        open(informatica5_path, 'r', encoding='utf-8')as f5:
        
        info1 = json.load(f1)
        info2 = json.load(f2)
        info3 = json.load(f3)
        info4 = json.load(f4)
        info5 = json.load(f5)
    
    if isinstance(info1, dict) and \
        isinstance(info2, dict) and \
        isinstance(info3, dict) and \
        isinstance(info4, dict) and \
        isinstance(info5, dict):
        data = {**info1, **info2, **info3, **info4, **info5}
    elif isinstance(info1, list) and \
        isinstance(info2, list) and \
        isinstance(info3, list) and \
        isinstance(info4, list) and \
        isinstance(info5, list):
        data = info1 + info2 + info3 + info4 + info5
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Informatica.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Lazer
try:
    with open(lazer1_path, 'r', encoding='utf-8') as f1, \
        open(lazer2_path, 'r', encoding='utf-8') as f2, \
        open(lazer3_path, 'r', encoding='utf-8') as f3, \
        open(lazer4_path, 'r', encoding='utf-8') as f4, \
        open(lazer5_path, 'r', encoding='utf-8')as f5, \
        open(lazer6_path, 'r', encoding='utf-8') as f6:
        
        laz1 = json.load(f1)
        laz2 = json.load(f2)
        laz3 = json.load(f3)
        laz4 = json.load(f4)
        laz5 = json.load(f5)
        laz6 = json.load(f6)
    
    if isinstance(laz1, dict) and \
        isinstance(laz2, dict) and \
        isinstance(laz3, dict) and \
        isinstance(laz4, dict) and \
        isinstance(laz5, dict) and \
        isinstance(laz6, dict):
        data = {**laz1, **laz2, **laz3, **laz4, **laz5, **laz6}
    elif isinstance(laz1, list) and \
        isinstance(laz2, list) and \
        isinstance(laz3, list) and \
        isinstance(laz4, list) and \
        isinstance(laz5, list) and \
        isinstance(laz6, list):
        data = laz1 + laz2 + laz3 + laz4 + laz5 + laz6
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Lazer.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Mercado e Farmacia
try:
    with open(mf1_path, 'r', encoding='utf-8') as f1, \
        open(mf2_path, 'r', encoding='utf-8') as f2, \
        open(mf3_path, 'r', encoding='utf-8') as f3, \
        open(mf4_path, 'r', encoding='utf-8') as f4, \
        open(mf5_path, 'r', encoding='utf-8')as f5, \
        open(mf6_path, 'r', encoding='utf-8') as f6:
        
        mf1 = json.load(f1)
        mf2 = json.load(f2)
        mf3 = json.load(f3)
        mf4 = json.load(f4)
        mf5 = json.load(f5)
        mf6 = json.load(f6)
    
    if isinstance(mf1, dict) and \
        isinstance(mf2, dict) and \
        isinstance(mf3, dict) and \
        isinstance(mf4, dict) and \
        isinstance(mf5, dict) and \
        isinstance(mf6, dict):
        data = {**mf1, **mf2, **mf3, **mf4, **mf5, **mf6}
    elif isinstance(mf1, list) and \
        isinstance(mf2, list) and \
        isinstance(mf3, list) and \
        isinstance(mf4, list) and \
        isinstance(mf5, list) and \
        isinstance(mf6, list):
        data = mf1 + mf2 + mf3 + mf4 + mf5 + mf6
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Mercado_Farmacia.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Papelaria
try:
    with open(papel1_path, 'r', encoding='utf-8') as f1, \
        open(papel2_path, 'r', encoding='utf-8') as f2, \
        open(papel3_path, 'r', encoding='utf-8') as f3, \
        open(papel4_path, 'r', encoding='utf-8') as f4:
        
        pap1 = json.load(f1)
        pap2 = json.load(f2)
        pap3 = json.load(f3)
        pap4 = json.load(f4)
    
    if isinstance(pap1, dict) and \
        isinstance(pap2, dict) and \
        isinstance(pap3, dict) and \
        isinstance(pap4, dict):
        data = {**pap1, **pap2, **pap3, **pap4}
    elif isinstance(pap1, list) and \
        isinstance(pap2, list) and \
        isinstance(pap3, list) and \
        isinstance(pap4, list):
        data = pap1 + pap2 + pap3 + pap4
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Papelaria.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Pets
try:
    with open(pets1_path, 'r', encoding='utf-8') as f1, \
        open(pets2_path, 'r', encoding='utf-8') as f2, \
        open(pets3_path, 'r', encoding='utf-8') as f3, \
        open(pets4_path, 'r', encoding='utf-8') as f4, \
        open(pets5_path, 'r', encoding='utf-8') as f5:
        
        pet1 = json.load(f1)
        pet2 = json.load(f2)
        pet3 = json.load(f3)
        pet4 = json.load(f4)
        pet5 = json.load(f5)
    
    if isinstance(pet1, dict) and \
        isinstance(pet2, dict) and \
        isinstance(pet3, dict) and \
        isinstance(pet4, dict) and \
        isinstance(pet5, dict):
        data = {**pet1, **pet2, **pet3, **pet4, **pet5}
    elif isinstance(pet1, list) and \
        isinstance(pet2, list) and \
        isinstance(pet3, list) and \
        isinstance(pet4, list) and \
        isinstance(pet5, list):
        data = pet1 + pet2 + pet3 + pet4 + pet5
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Pets.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Roupa
try:
    with open(roupas1_path, 'r', encoding='utf-8') as f1, \
        open(roupas2_path, 'r', encoding='utf-8') as f2, \
        open(roupas3_path, 'r', encoding='utf-8') as f3, \
        open(roupas4_path, 'r', encoding='utf-8') as f4, \
        open(roupas5_path, 'r', encoding='utf-8') as f5, \
        open(roupas6_path, 'r', encoding='utf-8') as f6, \
        open(roupas7_path, 'r', encoding='utf-8') as f7, \
        open(roupas8_path, 'r', encoding='utf-8') as f8:
        
        rou1 = json.load(f1)
        rou2 = json.load(f2)
        rou3 = json.load(f3)
        rou4 = json.load(f4)
        rou5 = json.load(f5)
        rou6 = json.load(f6)
        rou7 = json.load(f7)
        rou8 = json.load(f8)
    
    if isinstance(rou1, dict) and \
        isinstance(rou2, dict) and \
        isinstance(rou3, dict) and \
        isinstance(rou4, dict) and \
        isinstance(rou5, dict) and \
        isinstance(rou6, dict) and \
        isinstance(rou7, dict) and \
        isinstance(rou8, dict):
        data = {**rou1, **rou2, **rou3, **rou4, **rou5, **rou6, **rou7, **rou8}
    elif isinstance(rou1, list) and \
        isinstance(rou2, list) and \
        isinstance(rou3, list) and \
        isinstance(rou4, list) and \
        isinstance(rou5, list) and \
        isinstance(rou6, list) and \
        isinstance(rou7, list) and \
        isinstance(rou8, list):
        data = rou1 + rou2 + rou3 + rou4 + rou5 + rou6 + rou7 + rou8
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Roupa.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Sapato
try:
    with open(sapato1_path, 'r', encoding='utf-8') as f1, \
        open(sapato2_path, 'r', encoding='utf-8') as f2, \
        open(sapato3_path, 'r', encoding='utf-8') as f3, \
        open(sapato4_path, 'r', encoding='utf-8') as f4, \
        open(sapato5_path, 'r', encoding='utf-8') as f5, \
        open(sapato6_path, 'r', encoding='utf-8') as f6:
        
        sap1 = json.load(f1)
        sap2 = json.load(f2)
        sap3 = json.load(f3)
        sap4 = json.load(f4)
        sap5 = json.load(f5)
        sap6 = json.load(f6)
    
    if isinstance(sap1, dict) and \
        isinstance(sap2, dict) and \
        isinstance(sap3, dict) and \
        isinstance(sap4, dict) and \
        isinstance(sap5, dict) and \
        isinstance(sap6, dict):
        data = {**sap1, **sap1, **sap3, **sap4, **sap5, **sap6}
    elif isinstance(sap1, list) and \
        isinstance(sap2, list) and \
        isinstance(sap3, list) and \
        isinstance(sap4, list) and \
        isinstance(sap5, list) and \
        isinstance(sap6, list):
        data = sap1 + sap2 + sap3 + sap4 + sap5 + sap6
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Sapato.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")


# Remedios
try:
    with open(remedios1_path, 'r', encoding='utf-8') as f1:
        
        re1 = json.load(f1)
    
    if isinstance(re1, dict):
        data = {**re1}
    elif isinstance(re1, list):
        data = re1
    else:
        raise ValueError("Os arquivos JSON devem ser ambos listas ou ambos dicionários.")
    
    final_data = os.path.join(project_root, 'Medicamentos.json')
    with open(final_data, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print("Os arquivos foram unidos com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: O arquivo não foi encontrado - {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON - {e}")
except Exception as e:
    print(f"Ocorreu um erro - {e}")