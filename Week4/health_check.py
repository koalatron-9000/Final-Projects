import shutil
import psutil
import socket
import emails

#report an error if CPU usage is over 80%
#	report an error if available disk space is lower than 20%
#	report an error if available memory is less than 500MB
#	report an error if hostname "localhost" cannot be resolved to "127.0.0.1"
#	emails if there are any issues.
#	install and use "stress" to test the functionality.
#	set up a cron job to run health_check.py every 60 seconds.
#	import shutil X
#	import psutil X

email_to = "automation@example.com"
email_from = "username@example.com"
email_body = "Please check your system and resolve the issue as soon as possible."

def available_disk():
    disk_usage = shutil.disk_usage("/")
    free_disk_percent = disk_usage.free/disk_usage.total * 100
    return free_disk_percent > 20

def cpu_usage():
    cpu = psutil.cpu_percent(0.5)
    return cpu < 80

def memory_check():
    ram = psutil.virtual_memory()
    free_ram = ram.available
    threshold = 500*1024*1024
    return free_ram > threshold

def check_host():
    h = socket.gethostbyname("localhost")
    return h == "127.0.0.1"


if available_disk() != True:
    email_subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(email_from, email_to, email_subject, email_body, "")
    emails.send_email()
if cpu_usage() != True:
    email_subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(email_from, email_to, email_subject, email_body, "")
    emails.send_email(message)
if memory_check() != True:
    email_subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(email_from, email_to, email_subject, email_body, "")
    emails.send_email(message)
if check_host() != True:
    email_subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(email_from, email_to, email_subject, email_body, "")
    emails.send_email(message)