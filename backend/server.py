import os
import hashlib
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in-memory cache for translations
translation_cache = {}

LANGUAGE_NAMES = {
    "pt-BR": "Brazilian Portuguese",
    "pt-PT": "Portuguese",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ja": "Japanese",
    "ko": "Korean",
}

class TranslateRequest(BaseModel):
    text: str
    target_locale: str
    context: Optional[str] = "surfboard shaper directory listing"

class TranslateResponse(BaseModel):
    original: str
    translated: str
    locale: str
    cached: bool = False

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.post("/api/translate", response_model=TranslateResponse)
async def translate(req: TranslateRequest):
    # Skip translation for English locales
    if req.target_locale.startswith("en"):
        return TranslateResponse(
            original=req.text,
            translated=req.text,
            locale=req.target_locale,
            cached=True
        )
    
    # Check cache first
    cache_key = hashlib.md5(f"{req.text}:{req.target_locale}".encode()).hexdigest()
    if cache_key in translation_cache:
        return TranslateResponse(
            original=req.text,
            translated=translation_cache[cache_key],
            locale=req.target_locale,
            cached=True
        )
    
    # Get target language name
    target_lang = LANGUAGE_NAMES.get(req.target_locale, req.target_locale)
    
    try:
        from emergentintegrations.llm.chat import LlmChat, UserMessage
        
        api_key = os.environ.get("EMERGENT_LLM_KEY")
        
        chat = LlmChat(
            api_key=api_key,
            session_id=f"translate-{cache_key}",
            system_message=f"You are a professional translator. Translate the given text to {target_lang}. Only respond with the translation, nothing else. Preserve any formatting, line breaks, and special characters. Keep proper nouns (names of people, places, businesses) unchanged."
        ).with_model("openai", "gpt-4.1-mini")
        
        user_message = UserMessage(
            text=f"Translate this text from a {req.context}:\n\n{req.text}"
        )
        
        translated = await chat.send_message(user_message)
        translated = translated.strip()
        
        # Cache the result
        translation_cache[cache_key] = translated
        
        return TranslateResponse(
            original=req.text,
            translated=translated,
            locale=req.target_locale,
            cached=False
        )
    except Exception as e:
        print(f"Translation error: {e}")
        # Return original text on error
        return TranslateResponse(
            original=req.text,
            translated=req.text,
            locale=req.target_locale,
            cached=False
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
