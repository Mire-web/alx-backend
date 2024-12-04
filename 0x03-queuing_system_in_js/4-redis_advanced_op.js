import { createClient, print } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));

const hash_list = [['Portland', 50], ['Seattle', 80], ['New York', 20], ['Bogota', 20], ['Cali', 40], ['Paris', 2]];

for (const [field, value] of hash_list){
  await client.hset('HolbertonSchools', field, value, print);
}

client.hgetall('HolbertonSchools', (err, res) => {
  if (err){
    console.error(err);
  }
  else
    console.log(res);
});

client.quit();
