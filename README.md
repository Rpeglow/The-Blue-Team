# The-Blue-Team Project

The Blue Team Project is a collaborative Django web application that empowers users to search for courses and derive skill sets from course descriptions. The app consists of several modules, each serving a specific purpose: `course_entry`, `ClassTracker`, `JobSearch`, `ResumeBuilder`, and `UserInfo`.

## Installation

To set up and run the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/Rpeglow/The-Blue-Team.git
    ```

2. Navigate to the project directory:
    ```
    cd The-Blue-Team
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```
    python manage.py migrate
    ```

5. Start the server:
    ```
    python manage.py runserver
    ```

Access the application via `http://localhost:8000`. You can alternatively configure a different address in the server settings.

## Usage

Upon launching the application, start by creating a new user profile from the homepage. This profile will enable access to features such as course selection, skill generation, resume building, job search, and user information management.

### Course Entry Module

The `course_entry` module facilitates various aspects related to course handling:

- **Image Gallery:** Showcase images related to course content.
- **Image Details:** Display specific images linked to corresponding app pages.
- **About and FAQ Pages:** Provide information about the course entry module and frequently asked questions.

### ClassTracker Module

The `ClassTracker` module allows users to track courses and extract skills from their descriptions. It includes functionalities to:

- **View Course Data:** Explore available courses organized by various prefixes.
- **Search Course:** Look up specific courses by entering a prefix and class number.
- **Extract Skills:** Automatically generate skills from course descriptions.

### JobSearch Module

The `JobSearch` module facilitates job hunting by integrating job search functionalities:

- **Perform Job Search:** Users can search for job opportunities based on their acquired skills. The module fetches associated skills from user-selected courses and performs a job search using these skills and the user's location.
- **Job Listings:** Display a list of jobs matching the user's skills and location.

### ResumeBuilder Module

The `ResumeBuilder` module assists users in generating resumes based on their educational background, work experience, and acquired skills:

- **Build Resume:** Users can create resumes by adding their work history, education details, and skills obtained from the courses they've taken.
- **View Generated Resume:** Preview the generated resume containing user-provided information and extracted skills.

### UserInfo Module

The `UserInfo` module manages user information within the application:

- **User Creation:** Allows users to create new profiles by providing necessary information such as email, name, and location.
- **Confirmation Page:** After successful user creation, displays a confirmation page with the user's details.

Feel free to explore and utilize these modules to streamline course tracking, skill acquisition, job search, resume building, and user management processes!

---

#### Note:
Please refer to individual module documentation for detailed instructions and features.

For any issues or suggestions, please raise them in the repository's issue section.
