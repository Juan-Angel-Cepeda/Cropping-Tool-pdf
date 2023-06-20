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

def is_rotated(width,height):
    if width > height:
        return True
    else:
        return False
    

def verify_size(page):
    
    width = page.mediabox.width
    height = page.mediabox.height
    for paper_size, dimensions in PAPER_SIZES.items():
        if abs(dimensions[0] - width) < 200 and abs(dimensions[1] - height) < 100:
            return dimensions
    
    print("LETTER")
    return [612,791]
    
        
    
def cortar_contenido(path):
    
    document = PDF.PdfReader(path)
    writer = PDF.PdfWriter()
    pages = document.pages

    for page in pages:
        
        if is_rotated(page.mediabox.width,page.mediabox.height):
            page.rotate(-90)            
        
        page_dimensions = verify_size(page)
        blank_page = writer.add_blank_page(*page_dimensions)
        blank_page.merge_page(page)
            
        #page.mediabox = PDF.generic.RectangleObject([0,0,blank_page.mediabox.width,blank_page.mediabox.height])
        
    with open("JUAREZ-2016-3460-ED-INFR-JUA-04.pdf", "wb") as fp:
        writer.write(fp)


cortar_contenido(r"C:\Users\USER\Downloads\3460 ED INFR JUA\04.pdf")

