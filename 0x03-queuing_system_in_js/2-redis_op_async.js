import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value){
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName){
  const getAsync = promisify(client.get).bind(client);
  console.log(await getAsync(schoolName));
}

await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
