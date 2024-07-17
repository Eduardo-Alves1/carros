import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv('.env')



def get_car_ai_bio(model, brand, year):
    GOOGLE_API_KEY = 'AIzaSyAgpKV3mXafs4M0ajhiZ9FG1XAjzfp6DPo'
    
    genai.configure(api_key= GOOGLE_API_KEY)

    generation = {
        'candidate_count': 1,
        'temperature': 1,
    }

    security = {
        'HARASSMENT': 'BLOCK_NONE',
        'HATE': 'BLOCK_NONE',
        'SEXUAL': 'BLOCK_NONE',
        'DANGEROUS': 'BLOCK_NONE',
    }


    model_ia = genai.GenerativeModel(model_name= "gemini-1.5-flash", generation_config= generation, safety_settings= security)

    prompt = '''Me mostre um descrição de vedas para o carro {} {} {} em apenas 250 caracteres. Fale coisas especificas desse modelo de carro.'''

    prompt = prompt.format(brand, model, year)
    response = model_ia.generate_content(prompt)

    return response.text