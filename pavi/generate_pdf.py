from reportlab.platypus import SimpleDocTemplate , Image , Paragraph , Spacer , PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch,mm
class PDF:
    def __init__(self , report_date):
        self.doc = SimpleDocTemplate(r'./pdf/Daily Control Compare Report - {}.pdf'.format(report_date) , pagesize = A4)
        self.title = "Daily Control Compare Report - Omnytraq"
        self.sample_style_sheet = getSampleStyleSheet()
        self.ele = []
        self.bodystyle = ParagraphStyle('bodyStyle',
                                   fontName="Helvetica",
                                   fontSize=12,
                                   alignment=4,
                                   spaceAfter=0)

    def addVerticalSpace(self):
        return Spacer(1 , inch * 0.25) 
    
    def addTitle(self , title):
        return Paragraph(title , self.sample_style_sheet['Title'])


    def firstPage(self , data):
        temp_ele_list = []
        temp_ele_list.append(self.addVerticalSpace())
        temp_ele_list.append(self.addVerticalSpace())
        temp_ele_list.append(self.addTitle("Omnytraq - Control Compare Report"))
        temp_ele_list.append(self.addVerticalSpace())
        #add the total summary and defenition
        temp_ele_list.append(Paragraph('Summary:' , self.sample_style_sheet['Heading3']))
        with open('control_compare_report_template.txt' , encoding= 'utf-8') as defenition_file:
            template = defenition_file.read()
            data_para = template.format(**data)
            defenition_data = Paragraph(data_para.replace('\n' , '<br/>') , self.bodystyle)
        temp_ele_list.append(defenition_data)
        temp_ele_list.append(PageBreak())

        self.ele = temp_ele_list + self.ele
           

    def header_footer_pagenumber(self , canvas , doc):
        #add header
        canvas.saveState()
        header = Image('header.jpg' , width = doc.width + doc.leftMargin + doc.rightMargin, height= inch * 1.25)
        header.drawOn(canvas, 0 , doc.height + doc.topMargin )
        #add footer
        footer = Image('footer.png' , doc.width + doc.leftMargin + doc.rightMargin , height=inch)
        footer.drawOn(canvas , 0,0)

        #add page number
        page_num = doc.page
        text = "Page-->{} of ".format(page_num)
        canvas.drawRightString(200*mm, 20*mm, text)
        #close the canvas
        canvas.restoreState()

    def generate_pdf(self):
        self.ele.append(Paragraph('taking the simple text'))
        self.doc.build(self.ele, onFirstPage=self.header_footer_pagenumber , onLaterPages=self.header_footer_pagenumber)




pdf = PDF('pai')
data = {'sds_sample_size' : 1 , 'sdp_sample_size' : 2 , 'spo2_datapoints' :3 , 'spo2_start_date':4 , 'spo2_end_date':5,
'spo2_duration':5 ,'hr_datapoints':6 , 'hr_start_date':7,'hr_end_date':8,'hr_duration':9,}
pdf.firstPage(data)
pdf.generate_pdf()