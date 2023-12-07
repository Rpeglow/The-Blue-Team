import requests

def perform_job_search(keywords, location="chicago", fromage="3", radius="50", page_id="1"):
    """
    Perform a job search on Indeed API.

    Args:
        keywords (list): List of keywords to search for.
        location (str, optional): Location to search for jobs. Defaults to "chicago".
        fromage (str, optional): Number of days since the job was posted. Defaults to "3".
        radius (str, optional): Radius in miles from the specified location. Defaults to "50".
        page_id (str, optional): Page number of the search results. Defaults to "1".

    Returns:
        list: List of dictionaries containing extracted job information.
            Each dictionary contains the following keys:
            - job_name (str): Name of the job.
            - salary_range (str): Salary range of the job.
            - description (str): Description of the job.
            - hyperlink (str): Hyperlink to view the job on Indeed.

        None: If the API request fails or no jobs are found.
    """
    url = "https://indeed12.p.rapidapi.com/jobs/search"

    headers = {
        "X-RapidAPI-Key": "0057407977msh1bcf0878799c334p18e9fejsna2623f346f9d",
        "X-RapidAPI-Host": "indeed12.p.rapidapi.com"
    }

    # If no keywords provided, return None
    if(keywords == None):
        return None
    # If keywords provided, perform job search
    else:
        # Convert keywords to string
        querystring = {
            "query": ",".join(keywords),
            "location": location,
            "page_id": page_id,
            "fromage": fromage,
            "radius": radius
        }

        # Perform API request
        response = requests.get(url, headers=headers, params=querystring)

        # If API request successful, extract job information
        if response.status_code == 200:
            jobs = response.json().get("hits", [])
            extracted_jobs = []

            # Loop through jobs and extract job information
            for job in jobs:
                # If salary information is not provided, set salary range to N/A
                min_salary = job['salary'].get('min')
                max_salary = job['salary'].get('max')

                salary_range = f"{min_salary}-{max_salary} {job['salary'].get('type')}" if min_salary is not None and max_salary is not None else "N/A"

                # Add extracted job information to list
                extracted_job = {
                    "job_name": job.get("title"),
                    "salary_range": salary_range,
                    "description": f"{job['company_name']} - {job['location']}",
                    "hyperlink": f"https://www.indeed.com/viewjob?jk={(job['link'].split('?')[0]).replace('/job/', '')}"
                }
                extracted_jobs.append(extracted_job)

            return extracted_jobs
        else:
            return None

#perform_job_search(keywords=['C# programming', 'Databases'], location="Indianapolis, IN")
