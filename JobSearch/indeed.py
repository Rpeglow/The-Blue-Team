import requests

def perform_job_search(keywords, location="chicago", fromage="3", radius="50", page_id="1"):
    url = "https://indeed12.p.rapidapi.com/jobs/search"

    headers = {
        "X-RapidAPI-Key": "0057407977msh1bcf0878799c334p18e9fejsna2623f346f9d",
        "X-RapidAPI-Host": "indeed12.p.rapidapi.com"
    }

    if(keywords == None):
        return None
    else:
        querystring = {
            "query": ",".join(keywords),
            "location": location,
            "page_id": page_id,
            "fromage": fromage,
            "radius": radius
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            jobs = response.json().get("hits", [])
            extracted_jobs = []

            for job in jobs:
                extracted_job = {
                    "job_name": job.get("title"),
                    "salary_range": f"{job['salary'].get('min', '')}-{job['salary'].get('max', '')} {job['salary'].get('type', '')}",
                    "description": f"{job['company_name']} - {job['location']}",
                    "hyperlink": f"https://www.indeed.com{job['link']}"
                }
                extracted_jobs.append(extracted_job)

            return extracted_jobs
        else:
            return None

#perform_job_search(keywords=['python', 'django', 'javascript'], location="Indianapolis, IN")
