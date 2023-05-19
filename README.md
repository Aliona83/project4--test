# Table of contents

  * Recipe Book 
  * Project goals
  * UX
     * User stories
     * Agile Methodology
     * The Scope
  *  Features 
      * Navigation
  * Design
     * Colours
     * Typography
     * Media
     * Wireframes


 ## Deployment

Heroku's Hosting Service
1. Log in or create an account at Heroku.
2. On the homepage you select the 'New' button and then select 'Create New App' from the drop-down.
3. Give your app a unique name and choose your relevant region.
4. In the 'Settings' tab of your app select 'Reveal Config Vars'.
5. Add a value for 'SECRET_KEY' connecting to your django environment.
6. Add a value for 'DATABASE_URL' connecting to your postgreSQL database.
7. Add a value for 'ClOUDINARY_URL' connecting to cloudinary's cloud hosting service for media.
8. Proceed down to the 'Buildpack' section and select 'Add buildpack' before choosing Python and 'Save Changes'.
9. Back at the top of the page select the 'Deploy' tab.
10. Select GitHub as preferred deployment method, confirm connecting to Github if not automatic.
11. Connect to your relevant repository on GitHub.
12. You can now select either 'Automatic Deployment' for deployment on every push to GiHub or 'Manual Deployment' for only when you press this button.

Final Deployment
1. Create a runtime.txt python-3.8.13.
2. Ensure a procfile is created with the following web: gunicorn projectnamehere.wsgi.
3. Ensure DEBUG = False in settings.py.

To Clone
You can clone this project by executing the following:
1. Open this project on GitHub here.
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click clipboard in order to copy.
3. Once selected, the forked project will be in your repositories.
4. Open up a new terminal.
5. Adjust the current directory to be the location you wish the cloned directory to be.
6. Type 'git clone' and paste the URL copied above in step 2.
7. Hit 'Enter' and the project will be successfully cloned.

To Fork
1. Open this project on GitHub here.
2. The fork button is found at the top of the page.
3. The forked project will be in your repositories.

## Technologies Used
* Git Used for version control alongside GitHub.
* GitHub Used in conjunction with Gitpod as the code editor, to store the project and utilise git version control.
* Heroku Used to deploy and host the finished product.
* Cloudinary Used as cloud based storage, storing any submitted media in the deployed application.
* ElephantSQL Used to host the PostgreSQL database for the application.
* W3C - HTMLUsed to validate all HTML code.
* W3C - CSS Used to validate all CSS code.
* CI PEP8 Testing Used to validate all Python code.
* Google Fonts Used to provide the fonts used in application styling.
* Bootstrap Used to aid implementation of styling and responsiveness.
* Fontawesome Used to implement effective icons.
* Google Chrome Dev Tools Used during the development to debug and test responsiveness.
* Balsamiq Used to build both the database schema diagram and design wireframes.
     
## Credits    
* Stack Overflow
* bbcgoodfood
* 