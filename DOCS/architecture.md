# Architecture

## Descripción general

El sistema DeliveryRoute API sigue una arquitectura en capas simple orientada a servicios.  
El objetivo es implementar un MVP funcional que permita gestionar pedidos y su estado de entrega mediante una API REST.

La arquitectura está diseñada para ser fácil de entender, mantener y escalar en futuras versiones del sistema.

El sistema permite:
- registrar pedidos
- consultar pedidos
- actualizar el estado de entrega
- visualizar información mediante endpoints HTTP

---

## Componentes principales

### Cliente
El cliente puede ser:
- navegador web
- Postman
- Swagger UI
- cualquier aplicación que consuma la API

El cliente envía solicitudes HTTP al servidor.

---

### API REST (FastAPI)
La API está construida utilizando FastAPI, un framework moderno de Python que permite crear APIs rápidas y bien documentadas.

Responsabilidades:
- recibir solicitudes HTTP
- validar datos de entrada usando Pydantic
- devolver respuestas en formato JSON
- exponer endpoints del sistema

---

### Lógica de negocio
Contiene las reglas principales del sistema.

Responsabilidades:
- crear pedidos
- consultar pedidos
- actualizar estado del pedido
- controlar flujo del sistema

---

### Almacenamiento en memoria
Para el MVP se utiliza almacenamiento temporal en memoria mediante un diccionario de Python.

Responsabilidades:
- guardar pedidos temporalmente
- permitir pruebas rápidas sin configurar base de datos

En futuras versiones puede reemplazarse por:
- MySQL
- PostgreSQL
- Oracle
- MongoDB

---

## Diagrama de arquitectura

```mermaid
flowchart TD

Client[Cliente / Usuario]
API[FastAPI REST API]
Service[Lógica de negocio]
DB[(Base de datos en memoria)]

Client --> API
API --> Service
Service --> DB
DB --> Service
Service --> API
API --> Client
