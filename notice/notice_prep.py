from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
# import random
import datetime
from datetime import date



def create_notice(dept,Subject,content,desig,Date,Subject_docx) :
  template = DocxTemplate(Subject_docx)
  context = {
      'dept': dept,
      'date': Date,
      'Subject': Subject,
      'content': content,
      'desig': desig,
  }
  template.render(context)
  template.save('Subject1.docx')



def create_table(table_content,dept,desig):
  #row[0] = subject , row[1] = time
  template = DocxTemplate('Subjectt.docx')
  table_contents = []
  subject_column = []
  date_column = []
  for row in table_content :
    table_contents.append({
          'Subjectname': row[0],
          'Date': row[1],
          })
    subject_column.append(row[0])
    date_column.append(row[1])
  context = {
      'dept': dept,
      'date': date.today(),
      'Subject': Subject,
      'table_contents': table_contents,
      'desig': desig,
  }  
  template.render(context)
  template.save('Subjectt1.docx')

