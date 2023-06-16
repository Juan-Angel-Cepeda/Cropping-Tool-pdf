import pypdf as PDF

PAPER_SIZES = {
    PDF.PaperSize.A0:[2384,3370],
    PDF.PaperSize.A1:[1684,2384],
    PDF.PaperSize.A2:[1191,1684],
    PDF.PaperSize.A3:[842,1191],
    PDF.PaperSize.A4:[595,842],
    PDF.PaperSize.A5:[420,595],
    PDF.PaperSize.A6:[298,420],
    PDF.PaperSize.A7:[210,298],
    PDF.PaperSize.A8:[147,210],
    PDF.PaperSize.C4:[649,918],
}

def is_rotated(width,heigth):
    if width > heigth:
        return True
    else:
        return False
    

def verify_size(page):
    width = page.mediabox.width
    height = page.mediabox.height
    for paper_size, dimensions in PAPER_SIZES.items():
        if abs(dimensions[0]-width) < 200 and abs(dimensions[1]-height)< 200:
            return dimensions
        
    
def cortar_contenido(path):
    
    document = PDF.PdfReader(path)
    writer = PDF.PdfWriter()
    pages = document.pages

    for page in pages:

        # Crea una nueva página en blanco del tamaño de una hoja A4
        page_dimensions = verify_size(page)
        if is_rotated(page.mediabox.width, page.mediabox.height):
            blank_page = writer.add_blank_page(*page_dimensions[::-1])
        else:
            blank_page = writer.add_blank_page(*page_dimensions)
        # Calcula la posición x,y para centrar el contenido de la página original en la nueva página
        x = (blank_page.mediabox.width - page.mediabox.width) / 2
        y = (blank_page.mediabox.height - page.mediabox.height) / 2
        # Agrega el contenido de la página original a la nueva página, centrado
        blank_page.merge_page(page)

    with open("pypdf-output-overgetting.pdf", "wb") as fp:
        writer.write(fp)


cortar_contenido(r"\\RegistrosNAS\NAS REGISTROS\D18FQT~X\JQE0LT~1\2003\CVXZFD~O\CK9T9U~3.PDF")
