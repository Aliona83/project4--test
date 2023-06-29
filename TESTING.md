# Table of Contents
 * [Validator Testing](#validator-testing)
   * HTML
   * CSS
   * PYTHON
   * LIGHTHOUSE
   * GTMETRIX 
   * Ax Dev Tools

 * [Device Testing](#)
    * IMac
    * Samsung Galaxy Tablet
    * Iphone 6
    * Iphone 11
    * Chrome
    * Firefox

* [Manual Testing](#manual-testing)
* Bugs

# Validator Testing
<details>
<summary>Click to see more</summary>

  ## HTML Validator

  * Home Page
    ![](./readmeDocumentation/screenshot/homePageValidator.png)
    * Add recipe page
    ![](./readmeDocumentation/screenshot/addRecipeValidator.png)
    * Recipe Library
    ![](./readmeDocumentation/screenshot/allRecipesPageValidator.png)
    * Each Recipe Page
    ![](./readmeDocumentation/screenshot/addRecipeValidator.png)
    * Update Recipe page
    ![](./readmeDocumentation/screenshot/updateRecipeValidator.png)
    * Log In
    ![](./readmeDocumentation/screenshot/logInValidator.png)
    * Log Out
    ![](./readmeDocumentation/screenshot/logOutValidator.png)
    * Register page
    ![](./readmeDocumentation/screenshot/registerValidator.png)

 ## CSS Validator

  * Css 
  ![](./readmeDocumentation/screenshot/cssValidator.png)

  ## Python

 Add_recipe folder 
 All available files have been checked
  * form.py
  ![](./readmeDocumentation/screenshot/formFile.png)
  * model.py
  ![](./readmeDocumentation/screenshot/modelfile.png)
  * url.py
  ![](./readmeDocumentation/screenshot/urlFile.png)

  project4 folder
   * url.py
   ![](./readmeDocumentation/screenshot/projectUrl.png)
  
  recipe folder
    * url.py
    ![](./readmeDocumentation/screenshot/recipeUrl.png)
    * view.py
    ![](./readmeDocumentation/screenshot/recipeView.png)
</details>

## Lighthouse

<details>
<summary>Click to see more</summary>

 * Home Page
     * Desktop
  ![Desktop](./readmeDocumentation/screenshot/homePageDesktop.png)
     * Mobile
  ![Mobile](./readmeDocumentation/screenshot/homePageMobile.png)
 
 * Add Recipe page
     * Desktop
   ![](./readmeDocumentation/screenshot/addRecipePageDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/addRecipePageMobile.png)

  * Recipe Library
     * Desktop 
   ![](./readmeDocumentation/screenshot/recipeLibraryDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/recipeLibraryPageMobile.png)

  * Register Page 
     * Desktop 
   ![](./readmeDocumentation/screenshot/registerPageDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/registerPageMobile.png)
  
  * Each Recipe Page
     * Desktop 
   ![](./readmeDocumentation/screenshot/eachRecipePageDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/eachRecipePageMobile.png)
  
  * Update Recipe Page
     * Desktop 
   ![](./readmeDocumentation/screenshot/updatePageDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/updatePageMobile.png)

   * Log In
     * Desktop 
   ![](./readmeDocumentation/screenshot/logInPageDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/logInPageMobile.png)

   * Log Out
     * Desktop 
   ![](./readmeDocumentation/screenshot/logOutDesktop.png)
     * Mobile 
   ![](./readmeDocumentation/screenshot/logOutMobile.png)

  </details>

   ## GTMETRIX 
   ![](./readmeDocumentation/screenshot/gtMetrixTest.png)

   ## Ax Dev Tools

   * All pages had been checked with AX Dev Tools

   ![](./readmeDocumentation/screenshot/axDevTool.png)
   # Manual Testing

<details>
<summary>Click to see more</summary>


| Feature       |           Test Performed    |             Result           |        
|:--------------|:--------------------------- |:---------------------------  |
|                        Navigation                                        |
| Logo          | Clicked on Logo to check or redirect to the home page| Pass |
| Home button   | Clicked on the Home button from different pages to check or redirect to the home page| Pass  | 
| Add recipe    | Clicked on Add recipe link brings the User to the  Add recipe page | Pass |
| Register      | When clicking on the register link, brings the User to the registration page | Pass |
| Small screens |  Checked that on smaller devices changes to the burger menu | Pass |
| Recipe Library| Clicked recipe library link to check or will open a page with all recipes | Pass | 
| Log In        | Clicked on the log-in link that will bring the User to the login page  | Pass |
| Log Out       | Clicked on the log-out link that will bring the User to log out page | Pass |
|                                                         Footer                      |
| Small screens |       Checked that all media links are visible on small devices | Pass |                                |
| Media  Links  | Clicked on each media link opens a new page   | Pass |
| Footer is on all pages      | Check all pages how the footer looks   | Pass |
|                     Add Recipe Page                     |
| Try to create a new recipe with blank fields | For this test, I want to make sure that empty fields won't let to save the recipe and return the user to empty fields.|Pass |
| View form on different sizes of devices | Check how will look add recipe form on tablets and phones, make sure all form fields are easy to see and use| Pass. |
| Save new recipe | Recipe was successfully saved with the image. and I filled out all the fields| Pass|
|                          Recipe library                                                |
| Search bar functionality | Enter different ingredients and meal types, all recipes were found from the recipe library that was searched in the search bar| Pass |
| Pagination | Test all the links should be functional by clicking on the numbers, next and previous buttons | Pass |
| View each recipe | By clicking on a recipe title link should open the recipe with full instructions and ingredients.| Pass |
| Delete recipe| By clicking on the delete button the User should be able to delete the recipe from the recipe library | Pass |
| Update recipe | By clicking on the button update recipe user will be able to make changes to the recipe and successfully save it| Pass|
| Like button | By clicking on the like button(heart) user will be able to like the recipe which he likes, heart has to be red if a user liked the recipe| Pass|
| Unlike button | Click on the heart button to unlike the recipe, and the button turns to unlike | Pass|
| Check how the page works on small devices | Check that page looks good and is able to use on tablets and phones| Pass |
| Success messages |After deleting, update and adding recipe User gets messages/feedback| Pass |
|Check authentication | User able to Sign Up, log in and log out | Pass |
| Security App | Without login, I wanted to go to the add recipe page, but I was redirected to the login page| Pass |

</details>

# Bugs 
***


| Bug      |       What  Issue   |       How   Issue     Fixed      |        
|:--------------|:--------------------------- |:---------------------------  |
| Wrong Url path| When I click create recipe was redirecting to add recipe page | Issue fixed by changing right URL path |
| couldn't see any add recipes in all_recipe page | Page was empty whit out any recipes | Issue was wrong spell object variable this had issue by iterate through the list of objects| 
| Page not found (404)
No recipes match the given query| When I want to like recipe get error no recipes match query | Fixed issue by check the query parameters|
| DisallowedHost at /add _recipe| During the work on the project changed frequently HTTP_HOST header | Was adding the right HTTP_HOST header to ALLOWED_HOSTS|
| Success message | After the user log in or log out success massage appeared on page all_recipes | Move to display messages tag from all_recipes to base.html file|
| Like button | Issue was that when I like one recipe I liked all recipes what was on that page | Made decision to move the like button from all_recipes to each recipe and like each recipe separately|

