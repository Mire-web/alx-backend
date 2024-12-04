import { createQueue } from "kue";

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (let job of jobs) {
    const jobb = queue.create('push_notification_code_3', job).save(err => {
      if (!err) console.log(`Notification job created: ${jobb.id}`)
	});
    jobb.on('failed', (err) => console.log(`Notification job ${jobb.id} failed: `, err));
	jobb.on('complete', () => console.log(`Notification job ${jobb.id} completed`));
	jobb.on('progress', (progress, err) => console.log(`Notification job ${jobb.id} ${progress}% complete`));
  }
}

export default createPushNotificationsJobs;
