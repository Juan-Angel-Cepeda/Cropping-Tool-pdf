import pypdf as PDF

def is_rotated(width,heigth):
    if width > heigth:
        return True
    else:
        return False

def rotar(path):
    document = PDF.PdfReader(path)
    writer = PDF.PdfWriter()
    pages = document.pages
    
    for page in pages:
        if(is_rotated(page.mediabox.width,page.mediabox.height)):
            page.rotate(-90)
        writer.add_page(page)
    
    with open("3938 SA PROG JUA- ROTADO created.pdf","xb") as fp:
        writer.write(fp)
    return 1

#rotar(r"C:\Users\USER\Downloads\3938 SA PROG JUA\04.pdf")