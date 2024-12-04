import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '2348081175695',
  message: 'You just received a credit alert'
}).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`)
});

job.on('failed', (err) => console.log('Notification job failed'));
job.on('complete', (res) => console.log('Notification job completed'));