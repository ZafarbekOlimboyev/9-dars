from pdf2image import convert_from_path
from time import perf_counter
import asyncio

async def pdf_to_jpg(pdf_path, output_folder,pdf_number):
    await asyncio.sleep(0.001)
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        output_path = f"{output_folder}/{pdf_number}-mavzu_{i}.jpg"
        image.save(output_path, "JPEG")
        print(f"{pdf_number}-mavzu_{i}.jpg saved")

async def pdf_p(out_floder):
    start = perf_counter()
    tasks =[]
    for i in range(1,13):
        tasks.append(asyncio.create_task(pdf_to_jpg(f"pdfs/{i}-mavzu.pdf",out_floder,i)))

    for task in tasks:
        await task
    end = perf_counter()
    print(f"FINISH\n{end - start : .3f} sekund")

if __name__ == "__main__":
    asyncio.run(pdf_p("JPEGS_AS"))
