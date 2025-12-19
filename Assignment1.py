from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyB5YXurHlI8hfCPSgQt3J8oxzXRmptZE0Y")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["""Write an engaging blog introduction explaining the basics of large language models (LLMs) for software engineers.""",
    
    """Create a compelling product description based on the following bullet points:
     - Wireless noise-cancelling headphones
     - 40-hour battery life
     - Bluetooth 5.3""",
   
    """Write a short science-fiction story (300–400 words) based on this opening line:
    "The last human on Earth received a message saying: I'm not alone."
    Include a clear beginning, middle, and end, with a surprising twist."""
    
    ] ,
    config=types.GenerateContentConfig(
        temperature=0.1,
        top_p=0.9,
        max_output_tokens=1000
    )
)

print(response.text)