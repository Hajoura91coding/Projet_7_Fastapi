# Projet_7
![image](https://github.com/Hajoura91coding/Projet_7_Fastapi/assets/60748328/1ad6716a-a494-408a-8d34-9cef4cc6087f)

API : Application Programming Interface
L'objectif d'un API est d'ajouter un logiciel intermédiaire entre deux applications pour qu'elles puissent communiquer entre elles par des requêtes et des réponses. 

FastAPI est un logiciel framework pour construire des APIs avec Python.

## Comment l'installer ?


```
pip install fastapi[all]
```

## Créer un script basic python avec Fastapi

```
from fastapi import FastAPI
app = FastAPI

@app.get('/')
def base():
  return "Hello World"
```
Maintenant il faut lancer le serveur grace à cette commande dans le terminal

```
uvicorn main:app -reload
```

![image](https://github.com/Hajoura91coding/Projet_7_Fastapi/assets/60748328/ec88d48b-9167-48d2-ad08-b57eb719d783)

http://127.0.0.1:8000/ 👈Lien du site en locale avec la reponse de la requête de l'API

![image](https://github.com/Hajoura91coding/Projet_7_Fastapi/assets/60748328/5159e454-c1f2-45c7-bba6-4718625b03bd)

Vous pouvez en apprendre plus en cliquant ici : 
https://levelup.gitconnected.com/fastapi-fundamentals-getting-faster-with-fastapi-866545b841ca
