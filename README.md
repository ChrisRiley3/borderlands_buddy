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

        a. As a first time visitor, to Borderland Buddy I want to be able to see the site main purpose and to learn more about what the organisation is trying to achieve.
           
        b. As a first time visitor, I want to be able to easyily navigate around the site and find the content I require both on desktop and mobile. 

        c. As a first time visitor, I want to be able to sign up to the site easily.

        d. As a first time visitor, I want to be able to search for specific weapons by using a search bar so I dont have to search for the weapon manually saving time.

        e. As a first time visitor, Once I have signed up I want to be able to view my profile to edit information about my billing address so I am not having to enter it every time I
           want to buy a weapon.

    * Returning Visitor Goals:

        a. As a returning visitor, I want to be able to view my order history incase I forgot to redeem my key I need to input on my console of choice.

        b. As a returning visitor, I want to be able to leave feedback on the site with information like what I like about the site and maybe what I would like to see added to the site.
        
        c. As a returning visitor, I want to be able to leave reviews on weapons that I have bought and used to help other users make that final decision on buying that weapon.

        d. As a returning visitor, I want to be able to purchase weapons of my choice.

    *  Frequent User Goals:

        a. As a frequent user, I want to see more new weapons added.
        
        b. As a frequent user, I want to be able to edit and delete the feedback that I have left on the website.

        c. As a frequent user, I want to be able to edit reviews that I have left on weapons.
        

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
        - Jquery was used for the country field selector in [profiles](profiles/static/profiles/js/countryfield.js). 
        - Jquery was also used for all the stripe elements this was took from their docs https://stripe.com/docs/payments/accept-a-payment and https://stripe.com/docs/stripe-js. 
        - Jquery was also used in [weapons](weapons/templates/weapons/includes/quantity_input_script.html) to help with users controlling the quanity of the weapon they want to buy.
    * [git](https://git-scm.com/)
        - Git was used for version control in the terminal that gitpod provides so I could could commit to git and then push to gitpod.
    * [Github](https://github.com/)
        - Github was used to store the code from the project after it was pushed from git.
    * [Django](https://www.djangoproject.com/)
        - Django was used for this project to make it easier to build and to help make it quicker.
        - using the terminal window that gitpod provides it makes it easy to download django, start a new project and create new apps within that project in no time at all.

# Testing
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and [W3C Markup Validator](https://validator.w3.org/#validate_by_input) service, pep8 checker that comes with gitpod
and also just to make sure I used a [pep8 online checker](http://pep8online.com/) to validate every page on this project to make sure that there
were no syntax errors.

* **Testing User Stories from User Experience (UX) Section**

    * First Time Visitor Goals:

        * As a first time visitor, to Borderland Buddy I want to be able to see the site main purpose and to learn more about what the organisation is trying to achieve.

            a. The user can obtain this information on the websites homepage which clearly states the sites main purpose and what the organisation is wanting to achieve. 
               All the user has to do is simply navigate to the website and the home page with the information will be the first page that loads up.

            b. The user is hit with a bright and colourful home page where the purpose of the site is made immediately with some text right next to the games background image.
               In this short paragrpah the users can learn what the site is trying to achieve.

            c. The user has a few different options at this point they can ether click the shop now button that will take them directly the all weapons page of the site. The user
               can also use the easy and manageable navigation menu to help them find the weapon they require. If the user knows the exact weapon they are looking for then all they
               have to do is use the search bar and this will take them directly to that weapon where they can use some of the other sites features and purcahse the weapon. However this
               is only if the weapon is in the sites database. With Borderlands 3 literally having  a [billion](https://www.google.com/search?q=how+many+weapons+are+in+borderlands+3&rlz=1C1CHBF_en-GBGB926GB926&oq=how+many+weapons+are+in+border&aqs=chrome.0.0i457j69i57j0j0i22i30l6.6923j1j15&sourceid=chrome&ie=UTF-8)
               guns, if you dont believe me follow the link and see for yourself. Guns will be constantly be getting added to the database.
        
        * As a first time visitor, I want to be able to easyily navigate around the site and find the content I require both on desktop and mobile.

            a. The user will find the site very easy to navigate around as the navigation bar is accessible on every page on the website and is very clear to what the user
               will be redirected to when clicking a link.
               
            b. The website's navigation bar is fully responsive so mobile users also have access to every feature on the site.

            c. When a user wants to submit some feedback on the site and they do that by submitting the feedback form they are redirected back to the top of the feedback page
               where they can see what they just submitted and also what other people have submitted to. Notice how they are redirected back to the top of the pay this it to allow
               for easy navigation once again as the nav bar is situated at the top of the page. This applies for any reviews left on a weapons page to. Once the user has submitted
               a review on a weapon they will be redirected back to the top of that weapons page where the nav bar is.
        
        * As a first time visitor, I want to be able to sign up to the site easily.

            a. The user will be able to sign up to the site by navigating to the account section that is clearly labelled on the top nav bar. Once the user clicks this link a dropdown
               menu will appear and they can register from there.

            b. The user will be redirected to a sign up page once they click register which will have a very simple form for them to fill out and they will now be a registered user on 
               submitting the form.
        
        * As a first time visitor, Once I have signed up I want to be able to view my profile to edit information about my billing address so I am not having to enter it every time I
          want to buy a weapon.
        
            a. A user will be able to achieve this by navigating to their profile in the accounts section once they have signed up to the website. On this page the user
               has a simple form to fill out with all the necessary billing information on it.

            b. All the user has to do is fill out the information and click update. Now everytime the user wants to buy a weapon they wont have to fill out all the billing information 
               again it will already be done for them.
    
    * Returning Visitor Goals:

        * As a returning visitor, I want to be able to view my order history incase I forgot to redeem the key I needed to input on my console of choice.

            a. The user can easily achieve this by navigating to their profile and on this page they will have all their order history giving them a brief view of the order.

            b. Clicking on a order will redirect them to a page were they can see the full order details.

            c. Also The user will have had a email sent to them when they purcahsed the weapon the user can find all the inforamtion they need on this email if they have saved it.

        * As a returning visitor, I want to be able to leave and read feedback on the site with information like what I like about the site and maybe what I would like to see added to the site.

            a. If the user is wanting to interact with the organisation and leave feedback on the website then all they have to do is use the navigation menu and navigate over to the feedback
               page.

            b. When they click on the feedback button they will be directed to the feedback page where they can see all the other feedback that has been left by other users.

            c. Now if the user wishes they can click the add feedback button where they will be directed again to the add feedback page this is where the user will be requred to fill out a simple
               form and on submitting that form they will be redirected back to the feedback page where they can now see their feedback has been left for the organisation and other users to read.
        
        * As a returning visitor, I want to be able to leave and read reviews on weapons that I have bought and used to help other users make that final decision on buying that weapon.

            a. The user will have to navigate to a weapon of their choice that they wish to purchase. This step has been covered in the first time visitor section.

            b. once a user has navigated to their weapon of choice they will have a few different option on this page. The page contains information about the weapon itself such as its name, 
               manufacture, Type of weapon, Price and a short paragraph about the weapon. At this point the user can ether choose to keep shopping as it is not the weapon they have been looking for
               or they can choose to add it to their bag ready to purchase it.

            c. The other choice the user has is to navigate to the bottom of that weapons page and this is where the reviews are sitatued. The user can read through other peoples reviews and also
               add reviews themselves.

            d. If a user wishes to leave a review about the weapon to help other users they can click the add review button. When they click this button they will be directed to the add review page.
               At this point I would like to mention that if a user does want to leave feedback or a review when using the website they must be signed in this is so the organisation can keep track of people
               leaving reviews and feedback. When the user is on the add review page they will have to fill out a simple form and on submitting this form they will be redirtected back to that weapons page and
               their review will have been added.
        
        * As a returning visitor, I want to be able to purchase weapons of my choice.

            a. Users will be able to purchase a weapon of their choice by navigating to the weapon they wish to purchase and clicking the add to basket button.

            b. When clicking this button they will be hit with a notification with a go to secure checkout button. If the user continues to press this button they
               they will be directed to the shopping bag page.

            c. On this page the user will have a few different choices. If the user decides they dont just want one of that weapon then they can update the quantity on this page with the price also
               being automatically updated for them.

            d. What if the user changes their mind and decides they dont want that weapon at all then also on this page the user has the option to remove that weapon from their basket. On clicking remove
               the basket will be updated.

            e. If the user decides everything is correct with the order and they wish to purchase the order then they can click the secure checkout button. On this page the user will be required to fill out
               a billing details form, this form is simple to fill out and if the user has already filled this form out in their profile the form will be automatically generated for them all they will be required to do
               is fill out the payment details and add their name. Once the user is happy that the form is correct they can click the complete order button which will direct them to a checkout success page
               with all the details that the user requires to redeem their weapon or weapons. Once the order has went through and the user is on this page they can navigate round the website again.
        
    * Frequent User Goals:

        * As a frequent user, I want to see more new weapons added.

            a. The site is designed so the super user will be able to add weapons to the database, edit existing weapons and delete weapons people are no longer buying.
            
            b. Also in the feedback section users can communicate to the organisation on which weapons they would like to see added to the site.
        
        * As a frequent user, I want to be able to edit and delete the feedback that I have left on the website.

            a. If a user wants to make changes or even delete the feedback that they have left then they will first have to sign into their account.

            b. Once the user is signed in to their account they will then navigate over to the feedback section. On this page they will be able to see all the feedback they have left
               and other users have left.

            c. The user will notice that only on the feedback that they have left they can edit and delete. They will be unable to edit and delete everyones feedback.

            e. If the user wishes to edit the feedback they have left then they would click the edit button situated at the bottom of the feedback they left. When this button is clicked
               the user will be redirected to a edit feedback page where their old feedback form will be loaded up. At this point the user can edit what they wish and then click submit.
               Once the user has submitted the form they will be redirected back to the feedback page where they can see their edited feedback.
            
            f. If the user decides that they wish to delete the feedback completely then all they have to do is click the delete button and the feedback will be no more.
        
        * As a frequent user, I want to be able to edit reviews that I have left on weapons.

            a. If the user has left a review on a weapon and then later decides that they wish to edit this review then first they must make sure they are signed in on the account that they left the review on.

            b. Once they are happy they are on that accont they will then navigate to the weapon they left the review on and they will notice that only the reviews that they have left have a edit button next to them.
               This is so a user can't just go and edit anyones review.

            c. When the user has found the review they wish to edit they can click the edit button which will direct them to the edit review page. Once on this page the user will see the form that they previously filled out
               with all the previous information in it. They can edit what they need and then submit the form.
            
            d. Once the form is submitted by click the edit review button the user will be redirected back to that weapons page where they will see their edited review.

            e. The user will notice that on this page they dont have the ability to delete their review. Being the developer of this site I believe that every review bad or good should be left on the site as the more information
               other users wishing to purchase the weapon have is better for them when making their decision.