from fpdf import FPDF
import qrcode


def GenerateReport(Name, HCNo, DOB, Dose1Type, Dose1Date, Dose1Address, Dose2Type, Dose2Date, Dose2Address):
    # Generate and Save QR Code Image based on HC No
    img = qrcode.make(HCNo)
    img.save("QRCode.png")

    #Generate PDF and save it
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(200, 10, " Covid19 Vaccination Report ", align="C", ln=True)
    pdf.ln()
    pdf.set_font('Arial', '', 16)
    pdf.cell(40, 10, "Name: ")
    pdf.cell(120, 10, Name, ln=True)
    pdf.cell(40, 10, "HC No.: ")
    pdf.cell(80, 10, str(HCNo), ln=True)
    pdf.cell(40, 10, "Date of Birth: ")
    pdf.cell(40, 10, DOB, ln=True)
    pdf.cell(40, 10, "Dose1 Type: ")
    pdf.cell(40, 10, Dose1Type, ln=True)
    pdf.cell(40, 10, "Dose1 Date: ")
    pdf.cell(40, 10, Dose1Date, ln=True)
    pdf.cell(40, 10, "Dose1 Loc: ")
    pdf.cell(40, 10, Dose1Address, ln=True)
    pdf.cell(40, 10, "Dose2 Type: ")
    pdf.cell(40, 10, Dose2Type, ln=True)
    pdf.cell(40, 10, "Dose2 Date: ")
    pdf.cell(40, 10, Dose2Date, ln=True)
    pdf.cell(40, 10, "Dose2 Loc: ")
    pdf.cell(40, 10, Dose2Address, ln=True)

    #save PDF
    pdf.image('QRCode.png', 100, 25, 100)
    pdf.output('CovidReport.pdf')


GenerateReport("DeepVyas", 12345, "14-Oct-1997", "Pfizer", "1-Jul-2021", "University", "Pfizer", "29-Jul-2021", "Sagehill")

