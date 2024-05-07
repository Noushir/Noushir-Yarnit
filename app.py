from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import os
from key import hfkey
# Define the request model
class MarketingContentRequest(BaseModel):
    format: str
    topic: str
    emotion: str = 'excited'  # Default value
    length: int = 150  # Default value

app = FastAPI()


# Set the token directly
os.environ['HF_TOKEN'] = hfkey

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")


# Load the Mistral 7B model
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
content_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

@app.post('/generate_marketing_content')
async def generate_marketing_content(request: MarketingContentRequest):
    try:
        # Validate input
        if not request.format or not request.topic:
            raise HTTPException(status_code=400, detail="Missing format or topic in the input")

        # Generate content using Mistral 7B
        prompt = f"Create a {request.emotion} {request.format} about {request.topic}:"
        response = content_generator(prompt, max_length=request.length, num_return_sequences=1)

        # Extract the generated text
        generated_text = response[0]['generated_text'].strip()

        # Return the generated content
        return {"text": generated_text}
    except Exception as e:
        # Handle exceptions
        raise HTTPException(status_code=500, detail=str(e))

