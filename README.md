# Blog Website

## Overview

This is a Django-based blog website where users can create, edit, and delete blog posts. The site includes features for user account management, including password reset using email and profile editing. The homepage displays a list of blogs with a pagination , to make a smooth user experience.

## Features

- **Homepage**: Displays a list of blogs with a "new" label for posts created within the last day. 
- **Pagination**: Shows two blogs per page for easy navigation.
- **User Authentication**:
  - Login and logout .
  - User profiles with customizable fields:
    - Profile image
    - Links to social media (Facebook, LinkedIn, Instagram, Twitter)
- **Password Management**:
  - Change password .
  - Password reset using email (valid for one hour and can only be used once).
- **Blog Management**:
  - Create, edit, and delete blogs.
  - Each blog includes:
    - Title
    - Content
    - Images
- **Additional Pages**:
  - Overview of user profile.
  - About page.
  - Contact us page.

## Technologies Used

- Python
- Django
- Bootstrap 4
- SQLite
- HTML/CSS

## My Future ideas:-

- don't allow profile image larger than 5mb and make more fields in profile like country
- datepicker
- add search recommendations
- Login Remeber Me
- Videos in the blogs
- Replay on comments

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
2.  Install the required packages:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages: 
    ```bash
    pip install -r requirements.txt
4. Run database migrations:
    ```bash
    python manage.py migrate
5.  Create a superuser:
    ```bash
    python manage.py createsuperuser
6.   Run the development server:
    ```bash
    python manage.py runserver
7.    Access the application in the browser
    http://127.0.0.1:8000/.


### Enable Password Reset via Email

To set up password reset via email, follow these steps:

1. Open `settings.py`.
2. Locate `EMAIL_HOST_USER` and enter your email address.
3. Find `EMAIL_HOST_PASSWORD` and enter your app password. 
   - You can generate this by going to your email settings and searching for "app passwords."
   - enter your email password
   - then you can create your app password.

### NOTE 
- If you find any problems  or bugs, please report them to me. I will do my best to fix them, Thanks. 
- Please tell me your opinion of the website :)
## Contact
- Email: [eld25351@gmail.com]
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/eld-shell/).