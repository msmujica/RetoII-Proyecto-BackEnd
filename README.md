# API (FastAPI + Postgres) — Setup con Docker

Este proyecto levanta una API FastAPI y una base de datos PostgreSQL usando Docker Compose.

---

## Requisitos

- Docker
- Docker Compose (plugin `docker compose`)

---

## Credenciales de PostgreSQL (Docker)

La API se conecta a Postgres con estos valores:

```txt
POSTGRES_USER = "root"
POSTGRES_PASSWORD = "root"
POSTGRES_HOST = "db"
POSTGRES_PORT = "5432"
POSTGRES_DB = "tareas"
```

---

## Levantar el proyecto

En la carpeta donde está el `docker-compose.yml` ejecutá:

```bash
docker compose up --build
```

La API queda disponible en:

- http://localhost:8000

---

## Cargar la base de datos (tablas + datos de prueba)

En este repo hay un archivo `postgre.sql` con las sentencias SQL.  

---

## Datos de prueba (incluidos en postgre.sql)

Se crea un usuario de prueba:

- Email: `martin@example.com`
- Password: `1234`

Y una tarea de ejemplo para ese usuario.