from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import typing
from uuid import uuid4

app = FastAPI(title="DeliveryRoute API")

# Base de datos en memoria
orders_db = {}

# MODELOS
class OrderCreate(BaseModel):
    customer_name: str
    address: str
    product: str

class Order(OrderCreate):
    id: str
    status: str

class OrderStatusUpdate(BaseModel):
    status: str


# ENDPOINTS

# Crear pedido
@app.post("/orders", response_model=Order)
def create_order(order: OrderCreate):
    order_id = str(uuid4())
    new_order = Order(
        id=order_id,
        status="pending",
        **order.dict()
    )
    orders_db[order_id] = new_order
    return new_order


# Listar pedidos
@app.get("/orders", response_model=typing.List[Order])
def get_orders():
    return list(orders_db.values())


# Obtener pedido por ID
@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]


# Cambiar estado
@app.put("/orders/{order_id}/status", response_model=Order)
def update_status(order_id: str, status_update: OrderStatusUpdate):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")

    orders_db[order_id].status = status_update.status
    return orders_db[order_id]