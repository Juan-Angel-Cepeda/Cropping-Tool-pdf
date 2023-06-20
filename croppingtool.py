import pypdf as PDF

PAPER_SIZES = {
    "A0":[2384,3370],
    "A1":[1684,2384],
    "A2":[1191,1684],
    "LETTER":[612,791],
    "LETTER_ROT":[791,612],
    "LEGAL":[612,1009],
    "LEGAL_ROT":[1009,612],
    "A3":[842,1191],
    "A4":[595,842],
    "A5":[420,595],
    "A6":[298,420],
    "A7":[210,298],
    "A8":[147,210],
    "C4":[649,918],
}

def is_rotated(width,heigth):
    if width > heigth:
        return True
    else:
        return False
    

def verify_size(page):
    width = page.mediabox.width
    height = page.mediabox.height
    print("ancho: ",width, "alto: ",height)
    for paper_size, dimensions in PAPER_SIZES.items():
        if(is_rotated(width,height)):
            if abs(dimensions[0]-width) < 20 and abs(dimensions[1]-height)< 200:
                print(dimensions)
                return dimensions
        else:
            if abs(dimensions[0]-width) < 200 and abs(dimensions[1]-height)< 20:
                print(dimensions)
                return dimensions
    
    print("default")
    return [612,791]
    
def cortar_contenido(path):
    
    document = PDF.PdfReader(path)
    writer = PDF.PdfWriter()
    pages = document.pages

    for page in pages:

        page_dimensions = verify_size(page)
        print("dimensiones verificadas: ", page_dimensions)
        if is_rotated(page.mediabox.width, page.mediabox.height):
            blank_page = writer.add_blank_page(*page_dimensions)
            blank_page.merge_page(page)
        else:
            blank_page = writer.add_blank_page(*page_dimensions)        
            blank_page.merge_page(page)

    with open("3460 ED INFR JUA.pdf", "wb") as fp:
        writer.write(fp)


cortar_contenido(r"C:\Users\USER\Downloads\3460 ED INFR JUA\04.pdf")
