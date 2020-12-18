import shutil
import psutil

#report an error if CPU usage is over 80%
#	report an error if available disk space is lower than 20%
#	report an error if available memory is less than 500MB
#	report an error if hostname "localhost" cannot be resolved to "127.0.0.1"
#	emails if there are any issues.
#	install and use "stress" to test the functionality.
#	set up a cron job to run health_check.py every 60 seconds.
#	import shutil
#	import psutil