# Ticket Manager API

API de gestion de tickets pour une petite équipe informatique (bugs, problèmes techniques, demandes d'amélioration), développée avec Django + Django REST Framework, authentification JWT.

## Modèle de données

```
Category (1) ────< Ticket (N)
```

- **Category** : `id`, `name`, `description`
- **Ticket** : `id`, `title`, `description`, `priority` (LOW/MEDIUM/HIGH), `status` (OPEN/IN_PROGRESS/CLOSED), `created_at`, `category` (FK)

**Règle métier** : un ticket avec `priority = HIGH` doit avoir une `description` d'au moins 20 caractères.

## Installation

```bash
git clone <url-du-repo>
cd django-project-main
python -m venv venv
```

Activation de l'environnement virtuel :

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Installation des dépendances :

```bash
pip install -r requirements.txt
```

## Lancement du projet

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Le serveur démarre sur `http://127.0.0.1:8000/`.

## Accès

- Admin Django : `http://127.0.0.1:8000/admin/`
- Page HTML des tickets : `http://127.0.0.1:8000/tickets/`
- API : `http://127.0.0.1:8000/api/`

## Authentification JWT

Obtenir un token (avec un utilisateur créé via `createsuperuser` ou l'admin) :

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "<user>", "password": "<password>"}'
```

Réponse :

```json
{
  "access": "...",
  "refresh": "..."
}
```

Rafraîchir le token :

```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "<refresh_token>"}'
```

Utiliser le token sur les requêtes protégées :

```
Authorization: Bearer <access_token>
```

## Endpoints API

| Méthode | URL                       | Auth requise |
|---------|---------------------------|--------------|
| GET     | `/api/tickets/`           | Non          |
| GET     | `/api/tickets/{id}/`      | Non          |
| POST    | `/api/tickets/`           | Oui          |
| PUT     | `/api/tickets/{id}/`      | Oui          |
| PATCH   | `/api/tickets/{id}/`      | Oui          |
| DELETE  | `/api/tickets/{id}/`      | Oui          |
| GET     | `/api/categories/`        | Non          |
| POST    | `/api/categories/`        | Oui          |
| PUT     | `/api/categories/{id}/`   | Oui          |
| PATCH   | `/api/categories/{id}/`   | Oui          |
| DELETE  | `/api/categories/{id}/`   | Oui          |
| POST    | `/api/token/`             | Non          |
| POST    | `/api/token/refresh/`     | Non          |

La lecture (`GET`) est publique, les écritures (`POST`/`PUT`/`PATCH`/`DELETE`) nécessitent un token JWT valide (`IsAuthenticatedOrReadOnly`).

## Exemple de création de ticket

```bash
curl -X POST http://127.0.0.1:8000/api/tickets/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Erreur lors de la connexion JWT",
        "description": "Impossible de se connecter avec un token JWT valide, erreur 401 systématique.",
        "priority": "HIGH",
        "status": "OPEN",
        "category": 1
      }'
```

## Répartition du travail

| Personne | Partie                                     |
|----------|---------------------------------------------|
| Steven   | Modèles, migrations, Admin Django          |
| Julien   | API DRF (serializers, viewsets, routes), validation métier |
| Rima     | JWT, permissions, page HTML, README        |

## Tests

```bash
python manage.py test
```
