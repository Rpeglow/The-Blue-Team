import requests
import json

def generate_skills_from_description(description):
    """
    This function uses an AI model to generate a list of skills from a given course description.

    Parameters:
    description (str): The course description from which to extract skills.

    Returns:
    list: A list of skills extracted from the course description. If no skills could be extracted, an empty list is returned.

    Usage:
    skills = generate_skills_from_description("This course covers basic concepts of programming...")
    """
    api_token = "AIzaSyDcJnHjaHnFW_Se9wJtrQ5b3Vn3dCxYx2M"
    url = f"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={api_token}"
    headers = {'Content-Type': 'application/json'}

    # The prompt text for the AI model
    prompt_text = f"Use the attached course description to create 3-5 buzzwords that could be used on a resume and return them as comma separated values:\n{description}"

    # The data for the POST request
    data = {
        "prompt": {
            "text": prompt_text
        }
    }
    # Send the POST request and get the response
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Parse the response JSON
    response_json = response.json()

    # If there are any candidates in the response
    if 'candidates' in response_json and len(response_json['candidates']) > 0:
        # Get the output text from the first candidate
        output_text = response_json['candidates'][0]['output']

        # Extract the skills from the output text
        extracted_skills = [
            skill.replace('*', '').strip().replace(',', '').title()
            for skill in output_text.split('\n')
            if skill.strip()
        ]

        # Return the extracted skills
        return extracted_skills
    else:
        # If no skills could be extracted, return an empty list
        return []