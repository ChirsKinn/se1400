from PIL import Image
import io

def pixelate_image(image_stream, pixel_size=30):
    img = Image.open(image_stream)
    img = img.convert('RGB')  # just in case
    small = img.resize(
        (img.width // pixel_size, img.height // pixel_size),
        resample=Image.NEAREST
    )
    pixelated = small.resize(img.size, Image.NEAREST)
    
    output = io.BytesIO()
    pixelated.save(output, format='PNG')
    output.seek(0)
    return output
