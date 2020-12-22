import glob
import datetime
import reports
import emails
#   import os X
#	import datetime X
#	import reports (my reports.py) X
#	imports emails (my emails.py) X
#	use dunder main to call the generate_report function from reports.py
#	reports.generate_report(attachment, title, paragraph)
#	attachment = "/tmp/processed.pdf"
d = datetime.date.today().strftime("%m/%d/%Y")
GL = glob.glob("/home/koalatron9000/test/*.txt")
Processed_data = ""
PDF_title = "Processed update on {}".format(d)
Email_title = "Upload Completed - Online Fruit Store"
Email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
for each in GL:
    with open(each, "r") as f:
        ReadData = list(f)
        Processed_data += "Name: " + str(ReadData[0]).replace("\n","")+"<br/>"
        Processed_data += "Weight: " + str(ReadData[1]).replace("\n","")+"<br/><br/>"


if __name__ == "__main__":
    reports.generate_report("/home/koalatron9000/test/processed.pdf", PDF_title, Processed_data)
    message = emails.generate_email("automation@example.com", "user@example.com", Email_title, Email_body, "/path/to/file/")
    emails.send_email(message)