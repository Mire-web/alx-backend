import { createQueue } from "kue";

const black_list = ['4153518780', '4153518781'];
const queue = createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

function sendNotification(phoneNumber, message, job, done){
  job.progress(0, 100, job.data);
  if (black_list.includes(phoneNumber)){
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
	done(err);
  }
  else {
  job.progress(50, 100, job.data);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
  job.progress(100, 100, job.data);
  done();
  }
}
