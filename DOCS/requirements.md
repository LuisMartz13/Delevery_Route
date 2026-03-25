# Requirements

## Historias de Usuario

### Must

1. Como administrador quiero crear pedidos para registrar entregas.

Given datos válidos  
When envío POST /orders  
Then el sistema guarda el pedido con estado "pending"

---

2. Como administrador quiero consultar un pedido por ID para ver su información.

Given un ID existente  
When envío GET /orders/{id}  
Then el sistema devuelve los datos del pedido

---

3. Como administrador quiero actualizar el estado de un pedido para controlar la entrega.

Given un pedido existente  
When envío PUT /orders/{id}/status  
Then el sistema cambia el estado del pedido

---

4. Como administrador quiero ver todos los pedidos para tener control general.

Given pedidos registrados  
When envío GET /orders  
Then el sistema devuelve la lista de pedidos

---

### Should

5. Validar que los datos del pedido no estén vacíos.

6. Mostrar mensaje de error si el pedido no existe.

---

### Could

7. Eliminar pedidos.

---

### Won’t

8. Autenticación de usuarios en este MVP.
