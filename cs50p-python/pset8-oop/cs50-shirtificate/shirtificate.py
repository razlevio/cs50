from fpdf import FPDF, enums

def main():
    name = get_name()
    name = f"{name} took CS50"
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", size=50)
    pdf.cell(0, 60, txt="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.image("shirtificate.png", w=pdf.epw)
    pdf.set_font("helvetica", size=28)
    pdf.set_text_color(255,255,255)
    pdf.text(txt=name, x=60, y=130)
    pdf.output("shirtificate.pdf")

def get_name():
    return input("Name: ").strip().title()


if __name__ == "__main__":
     main()
