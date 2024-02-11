from fastapi import FastAPI, HTTPException
import models
import db


api = FastAPI()


@api.get('/menu')
async def get_menu():
    return db.menu


@api.post("/menu")
async def add_menu_item(dish: models.Dish):
    db.menu.append(dish)
    return dish


@api.put('/menu/{dish_name}')
async def update_menu_item(dish_name: str, dish: models.Dish):
    for i in range(len(db.menu)):
        if db.menu[i].name == dish_name:
            db.menu[i] = dish
            return dish
    raise HTTPException(status_code=404, detail='dish not found')


@api.delete('/menu/{dish_name}')
async def delete_menu_item(dish_name: str):
    for i in range(len(db.menu)):
        if db.menu[i].name == dish_name:
            deleted = db.menu.pop(i)
            return deleted
    raise HTTPException(status_code=404, detail="dish not found")


@api.get('/orders')
async def get_orders():
    return db.orders


@api.get('/orders/{client_name}')
async def get_client_orders(client_name: str):
    client = 0
    for i in db.clients:
        if i.name == client_name:
            client = i
            break
    if client == 0:
        raise HTTPException(status_code=404, detail='client not found')
    client_orders = []
    for i in db.orders:
        if i.client == client:
            client_orders.append(i)
    return client_orders


@api.post('/orders')
async def create_order(order: models.Order):
    for i in order.dishes:
        if not (i in db.menu):
            raise HTTPException(status_code=404, detail='dish not in menu')
    db.orders.append(order)
    return order


@api.put('/orders/{order_name}')
async def update_order_status(order_id: int, status: models.Status):
    for i in range(len(db.orders)):
        if db.orders[i].id == order_id:
            db.orders[i].status = status
            return db.orders[i]
    raise HTTPException(status_code=404, detail="order not found")


@api.get('/clients')
async def get_clients():
    return db.clients


@api.post('/clients')
async def register_client(client: models.Client):
    db.clients.append(client)
    return client


@api.put("/clients/{client_name}")
def update_client_info(client_name: str, client: models.Client):
    for i in range(len(db.clients)):
        if db.clients[i].name == client_name:
            db.clients[i] = client
            return client
    raise HTTPException(status_code=404, detail='client not found')


