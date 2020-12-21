from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os

#this will take the .txt files in "/supplier-data/descriptions/"
#	it will use the name and weight lines from each text file.
#	it will build this into a PDF file.
#	must have a function called "generate_report"
#	PDF file must be named "processed.pdf"
#	import reportlab X

#d = datetime.date.today().strftime("%m/%d/%y")
#print("Today is {}".format(d))

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])