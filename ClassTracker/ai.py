import requests
import json

#description = 'Provides an understanding of fundamental and advanced concepts of the C# programming language. The emphasis will be on creating industry standard programs using current programming design software. Students will learn basic programming concepts such as sequence, iteration and decision structures; variables and constants; and functions and advanced concepts such as searches, sorts, collections, dictionaries, arrays, and linked lists. Classes, inheritance, polymorphism, connecting to databases, and multiform projects will also be utilized. Students will apply these skills in a hands-on environment. Students will practice skills such as team building, work ethic, communications, documentation, and adaptability.'
def generate_skills_from_description(description):
    api_token = "AIzaSyDcJnHjaHnFW_Se9wJtrQ5b3Vn3dCxYx2M"
    url = f"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={api_token}"
    headers = {'Content-Type': 'application/json'}
    prompt_text = f"Use the attached course description to create 3-5 buzzwords that could be used on a resume and return them as comma separated values:\n{description}"

    data = {
        "prompt": {
            "text": prompt_text
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    if 'candidates' in response_json and len(response_json['candidates']) > 0:
        output_text = response_json['candidates'][0]['output']

        extracted_skills = [
            skill.strip('*').strip().replace(',', '')
            for skill in output_text.split('\n')
            if skill.strip('*').strip().replace(',', '')
        ]

        return extracted_skills
    else:
        return []