from PIL import Image
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

image = Image.open("/path/to/your/image.png")
response = client.generate_content(
    model="gemini-pro-vision",
    contents=[image, "Describe this image."]
)
print(response.text)