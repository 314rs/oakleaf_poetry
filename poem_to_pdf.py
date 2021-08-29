import os
try:
    from fpdf import FPDF
except:
    print("fpdf not found")
    try:
        print("installing fpdf...")
        os.system("pip install fpdf")
        print("success")
        from fpdf import FPDF
    except:
        print("installation of fpdf failed")

def poem_to_pdf(text, mode=1, orientation="P", font_size=24):
    lines = text.splitlines()
    pdf = FPDF(orientation, "mm", "A4")
    pdf.add_page()
    pdf.set_font("Courier", "B", font_size)
    lines_broken = list()
    for line in lines:
        mylen = len(line)
        i = 0
        while i < mylen:
            lines_broken.append(line[i:i+35])
            i += 35
    pdf.set_y(297/2-len(lines_broken)*10/2)
    for line in lines_broken:
        pdf.cell(190, 10 , line, 0, 1, "C")
    
    return pdf