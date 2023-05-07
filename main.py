from io import BytesIO
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import Response
from PIL import Image, ImageDraw, ImageFont

app = FastAPI()


def gen_png(x, y, z):
    size = (256, 256)
    font_color = (255, 255, 255, 255)
    font_size = 25
    im = Image.new("RGBA", size, (255, 255, 255, 0))
    fontpath = Path.cwd().joinpath("ubuntu.ttf")
    font = ImageFont.truetype(str(fontpath), font_size)
    draw = ImageDraw.Draw(im)
    text = f"x = {x}\ny = {y}\nz = {z}"
    draw.text((128, 128), text, font=font, anchor="mm", fill=font_color, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.rectangle((0, 0, 255, 255), outline=(0, 0, 255, 255), width=1)
    return im


@app.get("/tile")
@app.get("/tile/{x}/{y}/{z}")
async def tile(x: int, y: int, z: int):
    image = BytesIO()
    img = gen_png(x, y, z)
    img.save(image, format="PNG")
    image.seek(0)
    return Response(content=image.read(), media_type="image/png")



