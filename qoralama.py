import pdfkit
def web_to_pdf(url):
    for i in range(1,13):
        pdfkit.from_url(url+str(i),f"pdfs/{i}-mavzu.pdf")
        print(i," - Lesson saved.")
    return 1
url = "https://multimediya.uz/e-kitob/index.php?mavzu="
print(web_to_pdf(url))