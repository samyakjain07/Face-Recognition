import birthdayFinder
import randomWish
import sendEmail
from PIL import Image, ImageDraw, ImageFont
import textwrap

a = birthdayFinder.checkBirthday()
# a = None
if a is None:
    print("Today there is no birthday")
else:
    print("Enter the pixel size for image X and Y ")
    x = int(input("Enter value of X "))
    y = int(input("Enter value of Y "))
    if x < 350 and y < 350:
        size = 10

    elif x < 600 and y < 600:
        size = 15
    elif x < 900 and y < 900:
        size = 20
    elif x < 1200 and y < 1200:
        size = 25
    elif x < 1500 and y < 1500:
        size = 30
    else:
        size = 35

    name = a[0]
    dob = a[1]
    email = a[2]

    message = f"Hello {name},\n {randomWish.random_wish}\n                    Have a great Day!!"
    w = 22
    text = textwrap.fill(message, w)

    img = Image.open('card.png')
    img2 = Image.open('Project 3 - WRITING ON IMAGE/portrait.jpeg')
    a = img2.resize((200, 200))
    print(a.size)

    new_image = img.resize((x, y))
    I1 = ImageDraw.Draw(new_image)

    myFont = ImageFont.truetype('KaushanScript-Regular.otf', size)

    # Add Text to an image
    I1.text((20, 70), text, font=myFont, fill=("white"))

    Image.Image.paste(new_image, a, (300, 200))
    new_image.save("Final.png")