from PIL import Image

def handle_uploaded_file(file):
# 导入图像
    img = Image.open(file)
    width,height = img.size

    # 生成的图片
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    # 像素转图片
    def get_char(r,g,b,alpha = 256):
        if alpha == 0:
            return ''
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1)/length
        return ascii_char[int(gray/unit)]

    # 生成图片
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += "\n"

    # 保存
    return txt
