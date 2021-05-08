from reportlab.platypus import SimpleDocTemplate , Image , Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch,mm
class PDF:
    def __init__(self , report_date):
        self.doc = SimpleDocTemplate(r'Daily Control Compare Report - {}.pdf'.format(report_date) , pagesize = A4)
        self.title = "Daily Control Compare Report - Omnytraq"
        self.ele = []
        

    def header_footer_pagenumber(self , canvas , doc):
        #add header
        canvas.saveState()
        header = Image('header.jpg' , width = doc.width + doc.leftMargin + doc.rightMargin, height= inch)
        header.drawOn(canvas, 0 , doc.height + doc.topMargin )
        #add footer
        footer = Image('footer.png' , doc.width + doc.leftMargin + doc.rightMargin , height=inch)
        footer.drawOn(canvas , 0,0)

        #add page number
        page_num = canvas.getPageNumber()
        text = "Page #{} of #{}".format(page_num , doc.page)
        canvas.drawRightString(200*mm, 20*mm, text)
        #close the canvas
        canvas.restoreState()

    def generate_pdf(self):
        self.ele.append(Paragraph('taking the simple text'))
        self.doc.build(self.ele, onFirstPage=self.header_footer_pagenumber , onLaterPages=self.header_footer_pagenumber)




pdf = PDF('pai')
pdf.generate_pdf()