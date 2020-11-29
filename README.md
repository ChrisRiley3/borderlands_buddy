# Borderland Buddy 
This is the main site for buying weapons for the multi platform game Borderlands 3. This site is designed to be responsive and accessible on a range of devices, 
making it easy to navigate and buy items. This site is for anyone like myself who simply has no time to play the game for multiple hours per day. By signing up to this site
users will get the chance to experience the game like everyone else who can play for multiple hours. At a small price the users will have the ability to buy weapons to use in game 
instead of spending hours trying to find them. This will help to develop the game further as users wont be getting bored not being able to use the weapons other users have spent 
hours to get increasing the amount of people playing the game. Users who do have time to play the game for hours on end will also beneit from this site. Just because they can play
for hours doesnt guarantee them the weapon they want, so they can also sign up to the site if they ever get sick of farming the weapon they just cant seem to get.

# User Experience (UX)
* **User Stories**

    * First Time Visitor Goals:

        a. As a first time visitor, to Borderland Buddy I want to be able to see the site main purpose and goals. The user can obtain this information on the websites homepage
           which clearly states the sites main purpose and the goals. All the user has to do is simply navigate to the website and the home page with the information will be the first 
           page that loads up.
           
        b. As a first time visitor, I want to be able to easyily navigate around the site and find the content I require both on desktop and mobile. The user will find the site
           very easy to navigate around as the navigation bar is accessible on every page on the website and is very clear to what the user will be redirected to when clicking a link. 
           Also the website's navigation bar is fully responsive so mobile users can access what they require easily.

        c. As a first time visitor, I want to be able to sign up to the site easily. The user will be able to sign up to the site by navigating to the account section that is clearly
           labelled on the top nav bar. Once the user clicks this link a dropdown menu will appear and they can register from there. The user will be redirected to a sign up page 
           once they click register which will have a very simple form for them to fill out and they will now be a registered user on submitting the form.

        d. As a first time visitor, I want to be able to search for specific weapons by using a search bar so I dont have to search for the weapon manually saving time. The user will 
           have the option to search for any weapon they like as long as it is in the database. The search bar will be at the top on desktop and in the dropdown menu on mobile.

        e. As a first time visitor, Once I have signed up I want to be able to view my profile to edit information about my billing address so I am not having to enter it every time I
           want to buy a weapon. A user will be able to achieve this by navigating to their profile in the accounts section once they have signed up to the website. On this page the user
           has a simple form to fill out with all the necessary billing information on it. All the user has to do is fill out the information and click update. Now everytime the user 
           wants to buy a weapon they wont have to fill out all the billing information again it will already be done for them.

    * Returning Visitor Goals:

        a. As a returning visitor, I want to be able to view my order history incase I forgot to redeem my key I need to input on my console of choice. The user can easily achieve this by
           navigating to their profile and on this page they will have all their order history giving them a brief view of the order. Clicking on a order will redirect them 
           to a page were they can see the full order details.

    *  Frequent User Goals:

        a. As a frequent user, I want to see more new weapons added. The site is designed so the super user will be able to add weapons to the database, edit existing weapons and delete weapons
           people are no longer buying.

* **Design**

    * Colour Scheme: 

        - The game is a very bright game. So I have matched the website to the games background image using bright orange for the navigation bar, some button backgrounds and weapon information
          backgrounds. Black for the text on the website, also blue and red to match buttons up to what they will do. For example removing a item from your basket will be a red and 
          updating will be blue. The reason I chose these colours blue and red is because most site will stick with these colours when doing the same thing so to keep a user from getting confused
          I will keep them the same. 

    * Typography:

        - The main font on the website is Raleway and the backup font is Sans Serif. The reason I chose Raleway as my main font used throughout the full website was because its very clean and 
          easy to read the font is very attractive in a way they it jumps out to the user which makes it appropriate on a site trying to sell itmes.
        
        - The weapon details section is very easy to understand and read. Users will know exactly what they are purchasing and know exactly what the wepon does.

        - The text on the site is also bold so the user wont have trouble reading it. With the background being bright if the text wasnt bold it would be faint and some users may struggle to see
          what they are trying to read.
    
    * Imagery

        - The images used on the site are all saved in the media folder and are visible on the site by using JSON data. these JSON files can be found in weapons/fixtures/weapons.json
          
        - The main background image is designed to be striking and crisp to catch the users eye and make them attracted to the site so they want to browse it.

        - When the users are browsing the site for weapons they will see all the weapons images are formatted the same to make it look professional and yet again to catch the eye of the user.
          The weapons images all have a dark background and the weapons themselves are all bright making them look very sharpe and crisp to the user.

* **Wireframes**

    * Desktop Wireframes - 
    * Mobile Wireframes -

# Features

* Borderlands Buddy is responsive on all device sizes
* There are interactive elemenbts within the website
    - Users have the ability to leave feedback on the webpage maybe things they would like to see in the future.
    - Users have the ability to leave reviews on weapons they have used in game so they can advice other users if that weapon is worth buying.
    - Users have the ability to purchase weapons they want to use and redeem them in game.

# Technologies Used 

* **Languages Used:**

    * [HTML5](https://en.wikipedia.org/wiki/HTML5)
    * [CSS3](https://en.wikipedia.org/wiki/CSS)
    * [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * [SQL](https://en.wikipedia.org/wiki/SQL)

* **Frameworks, Libraries & Programs Used**

    * [Bootstrap 4.4.1](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
        - Bootstrap was useed to assist with the website being responsive and styling of the website
    * [Google Fonts](https://fonts.google.com/)
        - Google fonts was used to import the 'Railway' font into static/css/base.css file which is used on all the pages across the website.
    * [Font Awesome](https://fontawesome.com/)
        - Font awesome was used on the majority of pages throughout the website to add icons to buttons for UX purposes.
    * [jQuery](https://jquery.com/)
        - Jquery comes with Boostrap to help make the navbar responsive.
        - Jquery was used with the update bag and remove from bag buttons so users could easily update their shopping bag and easily remove weapons from their bag.
        - Jquery was used for the country field selector in [profiles](profiles/templates/profiles/profile.html). 
        - Jquery was also used for all the stripe elements this was took from their docs https://stripe.com/docs/payments/accept-a-payment and https://stripe.com/docs/stripe-js. 
        - Jquery was also used in [weapons](weapons/templates/weapons/includes/quantity_input_script.html) to help with users controlling the quanity of the weapon they want to buy.
    * [git](https://git-scm.com/)
        - Git was used for version control in the terminal that gitpod provides so I could could commit to git and then push to gitpod.
    * [Github](https://github.com/)
        - Github was used to store the code from the project after it was pushed from git.
    * [Django](https://www.djangoproject.com/)
        - Django was used for this project to make it easier to build and to help make it quicker.
        - using the terminal window that gitpod provides it makes it easy to download django, start a new project and create new apps within that project in no time at all.
    



    


