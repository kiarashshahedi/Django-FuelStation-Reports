import base64

with open("/home/puddin/Desktop/FUEL-DJANDO/fuel_inspection/static/fonts/vazir.ttf", "rb") as font_file:
    encoded_string = base64.b64encode(font_file.read()).decode('utf-8')

# Save the encoded string to a file or print it
with open("encoded_font.txt", "w") as text_file:
    text_file.write(encoded_string)

print("Font encoded and saved to encoded_font.txt")
