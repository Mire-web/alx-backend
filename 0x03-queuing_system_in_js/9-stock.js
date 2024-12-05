import express from 'express';
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const app = express();

client.on('error', err => console.log('Redis not connected to server')).on('connect', () => console.log('Redis connected to server'));

const getAsync = promisify(client.get).bind(client);

const listProducts = [
{"itemId": 1, "itemName": "Suitcase 250", "price": 50, "initialAvailableQuantity": 4},
{"itemId": 2, "itemName": "Suitcase 450", "price": 100, "initialAvailableQuantity": 10},
{"itemId": 3, "itemName": "Suitcase 650", "price": 350, "initialAvailableQuantity": 2},
{"itemId": 4, "itemName": "Suitcase 1050", "price": 550, "initialAvailableQuantity": 5},
]

function reserveStockById(itemId, stock) {
  client.set(itemId, stock, print);
}

function getItemById(id) {
  for (let item of listProducts) {
    if (item.itemId === id){
      return item
    }
  }
}

async function getCurrentReservedStockById(itemId) {
  return await getAsync(itemId);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
//   console.log(req.params.itemId);
  const result = getItemById(Number(req.params.itemId));
  if (!result) return res.json({"status": "Product not found"});
  const stock = await getCurrentReservedStockById(Number(req.params.itemId));
  const current = {...result, "currentQuantity": stock != null ? Number(req.params.itemId) : result.initialAvailableQuantity}
  res.json(result);
});

app.get('/reserve_product/:itemId', (req, res) => {
  const result = getItemById(Number(req.params.itemId));
  if (!result) return res.json({"status": "Product not found"});
  if (result.initialAvailableQuantity < 1) return res.json({"status": "Not enough stock avialiable", "itemId": result.itemId});
  reserveStockById(result.itemId, result.initialAvailableQuantity);
  return res.json({"status": "Reservation confirmed", "itemId": result.itemId});
})

app.listen(3000);
