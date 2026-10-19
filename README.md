
# TP2 - Application FastAPI

Première application Python avec FastAPI exposant une route GET `/`.

## 1. Lancer l'application

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer le serveur :

```bash
uvicorn main:app --reload
```

## 2. Tester l'application

Ouvrir http://127.0.0.1:8000/ dans un navigateur.

Résultat attendu :

```json
{
  "message": "it works !"
}
```

On peut également tester l'application via la documentation interactive :
http://127.0.0.1:8000/docs

Cliquer sur `GET /`, puis `Try it out` et `Execute`.
La réponse doit avoir le statut HTTP `200 OK`.
