try:
    from fpdf import FPDF
except:
    print("fpdf not found.\nPlease install fpdf (pip install fpdf)")
    




def poem_to_pdf(text, mode=0, orientation="P", font_size=24):
    lines = list(text.splitlines())
    lines_final = list()
    pdf = FPDF(orientation, "mm", "A4")
    pdf.add_page()
    pdf.set_font("Courier", "B", font_size)

    if mode == 1:
        for line in lines:
            if line == "":
                lines_final.append({"line":"", "font_size": 20})
            else:
                font_size = 1
                pdf.set_font_size(font_size)
                while pdf.get_string_width(line) < pdf.w-20:
                    font_size += 1
                    pdf.set_font_size(font_size)
                lines_final.append({"line":line, "font_size":font_size-1})

    elif mode == 2:
        font_size = 1
        pdf.set_font_size(font_size)
        maxline=max(lines, key=pdf.get_string_width)
        while pdf.get_string_width(maxline) < pdf.w - 20 :
            font_size += 1
            pdf.set_font_size(font_size)
        font_size -= 1
        for line in lines:
            lines_final.append({"line":line, "font_size":font_size})
    
    else:
        for line in lines:
            current = line
            remaining = -1
            done = 0
            if line == "":
                lines_final.append({"line":"", "font_size":font_size})
            while len(current):
                while (pdf.get_string_width(current) > pdf.w - 20):
                    remaining -= 1
                    current = line[done:remaining]
                done += len(current)
                lines_final.append({"line":current, "font_size":font_size})
                current = line[done:len(line)]
                remaining = 0

    lines_height = 0
    for line in lines_final:
        lines_height += line["font_size"] * 0.353
    pdf.set_y((pdf.h-(lines_height%(pdf.h-20)))/2)
    for line in lines_final:
        pdf.set_font_size(line["font_size"])
        pdf.cell(pdf.w-20, line["font_size"] * 0.353 , line["line"], 0, 1, "C")
    return pdf

if __name__ == "__main__":

    text="roses are red\n\
violets are blue\n\
this is a poem\n\
thank you\n"
#\n\n\nthis_is_a_very_long_line_please_do_not_cut_a_word\n\
#end"
    pdf = poem_to_pdf(text, 3, "p", 100)
    pdf.output("testpoem.pdf")