# Borderland Buddy 
This is the main site for buying weapons for the multi platform game Borderlands 3. This site is designed to be responsive and accessible on a range of devices, 
making it easy to navigate and buy items. This site is for anyone like myself who simply has no time to play the game for multiple hours per day. By signing up to this site
users will get the chance to experience the game like everyone else who can play for multiple hours. At a small price the users will have the ability to buy weapons to use in game 
instead of spending hours trying to find them. This will help to develop the game further as users wont be getting bored not being able to use the weapons other users have spent 
hours to get increasing the amount of people playing the game. Users who do have time to play the game for hours on end will also beneit from this site. Just because they can play
for hours doesnt guarantee them the weapon they want, so they can also sign up to the site if they ever get sick of farming the weapon they just cant seem to get.

# User Experience (UX)

### User Stories

* First Time Visitor Goals:

    A. As a first time visitor, to Borderland Buddy I want to be able to see the site main purpose and to learn more about what the organisation is trying to achieve.
           
    B. As a first time visitor, I want to be able to easyily navigate around the site and find the content I require both on desktop and mobile. 

    C. As a first time visitor, I want to be able to sign up to the site easily.

    D. As a first time visitor, I want to be able to search for specific weapons by using a search bar so I dont have to search for the weapon manually saving time.

    E. As a first time visitor, Once I have signed up I want to be able to view my profile to edit information about my billing address so I am not having to enter it every time I
        want to buy a weapon.

* Returning Visitor Goals:

    A. As a returning visitor, I want to be able to view my order history incase I forgot to redeem my key I need to input on my console of choice.

    B. As a returning visitor, I want to be able to leave feedback on the site with information like what I like about the site and maybe what I would like to see added to the site.
        
    C. As a returning visitor, I want to be able to leave reviews on weapons that I have bought and used to help other users make that final decision on buying that weapon.

    D. As a returning visitor, I want to be able to purchase weapons of my choice.

*  Frequent User Goals:

    A. As a frequent user, I want to see more new weapons added.
        
    B. As a frequent user, I want to be able to edit and delete the feedback that I have left on the website.
    C. As a frequent user, I want to be able to edit reviews that I have left on weapons.
        

### Design

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

### Wireframes

* Desktop Wireframes - 
* Mobile Wireframes -

# Features

* Borderlands Buddy is responsive on all device sizes
* There are interactive elemenbts within the website
    - Users have the ability to leave feedback on the webpage maybe things they would like to see in the future.
    - Users have the ability to leave reviews on weapons they have used in game so they can advice other users if that weapon is worth buying.
    - Users have the ability to purchase weapons they want to use and redeem them in game.

# Technologies Used 

### Languages Used:

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [SQL](https://en.wikipedia.org/wiki/SQL)

### Frameworks, Libraries & Programs Used:

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

### Testing User Stories from User Experience (UX) Section

* First Time Visitor Goals:

    * As a first time visitor, to Borderland Buddy I want to be able to see the site main purpose and to learn more about what the organisation is trying to achieve.

        A. The user can obtain this information on the websites homepage which clearly states the sites main purpose and what the organisation is wanting to achieve. 
            All the user has to do is simply navigate to the website and the home page with the information will be the first page that loads up.

        B. The user is hit with a bright and colourful home page where the purpose of the site is made immediately with some text right next to the games background image.
            In this short paragrpah the users can learn what the site is trying to achieve.

        C. The user has a few different options at this point they can ether click the shop now button that will take them directly the all weapons page of the site. The user
            can also use the easy and manageable navigation menu to help them find the weapon they require. If the user knows the exact weapon they are looking for then all they
            have to do is use the search bar and this will take them directly to that weapon where they can use some of the other sites features and purcahse the weapon. However this
            is only if the weapon is in the sites database. With Borderlands 3 literally having  a [billion](https://www.google.com/search?q=how+many+weapons+are+in+borderlands+3&rlz=1C1CHBF_en-GBGB926GB926&oq=how+many+weapons+are+in+border&aqs=chrome.0.0i457j69i57j0j0i22i30l6.6923j1j15&sourceid=chrome&ie=UTF-8)
            guns, if you dont believe me follow the link and see for yourself. Guns will be constantly be getting added to the database.
        
    * As a first time visitor, I want to be able to easyily navigate around the site and find the content I require both on desktop and mobile.

        A. The user will find the site very easy to navigate around as the navigation bar is accessible on every page on the website and is very clear to what the user
            will be redirected to when clicking a link.
               
        B. The website's navigation bar is fully responsive so mobile users also have access to every feature on the site.

        C. When a user wants to submit some feedback on the site and they do that by submitting the feedback form they are redirected back to the top of the feedback page
            where they can see what they just submitted and also what other people have submitted to. Notice how they are redirected back to the top of the pay this it to allow
            for easy navigation once again as the nav bar is situated at the top of the page. This applies for any reviews left on a weapons page to. Once the user has submitted
            a review on a weapon they will be redirected back to the top of that weapons page where the nav bar is.
        
    * As a first time visitor, I want to be able to sign up to the site easily.

        A. The user will be able to sign up to the site by navigating to the account section that is clearly labelled on the top nav bar. Once the user clicks this link a dropdown
            menu will appear and they can register from there.

        B. The user will be redirected to a sign up page once they click register which will have a very simple form for them to fill out and they will now be a registered user on 
            submitting the form.
        
    * As a first time visitor, Once I have signed up I want to be able to view my profile to edit information about my billing address so I am not having to enter it every time I
        want to buy a weapon.
        
        A. A user will be able to achieve this by navigating to their profile in the accounts section once they have signed up to the website. On this page the user
            has a simple form to fill out with all the necessary billing information on it.

        B. All the user has to do is fill out the information and click update. Now everytime the user wants to buy a weapon they wont have to fill out all the billing information 
            again it will already be done for them.
    
* Returning Visitor Goals:

    * As a returning visitor, I want to be able to view my order history incase I forgot to redeem the key I needed to input on my console of choice.

        A. The user can easily achieve this by navigating to their profile and on this page they will have all their order history giving them a brief view of the order.

        B. Clicking on a order will redirect them to a page were they can see the full order details.

        C. Also The user will have had a email sent to them when they purcahsed the weapon the user can find all the inforamtion they need on this email if they have saved it.

    * As a returning visitor, I want to be able to leave and read feedback on the site with information like what I like about the site and maybe what I would like to see added to the site.

        A. If the user is wanting to interact with the organisation and leave feedback on the website then all they have to do is use the navigation menu and navigate over to the feedback
            page.

        B. When they click on the feedback button they will be directed to the feedback page where they can see all the other feedback that has been left by other users.

        C. Now if the user wishes they can click the add feedback button where they will be directed again to the add feedback page this is where the user will be requred to fill out a simple
            form and on submitting that form they will be redirected back to the feedback page where they can now see their feedback has been left for the organisation and other users to read.
        
    * As a returning visitor, I want to be able to leave and read reviews on weapons that I have bought and used to help other users make that final decision on buying that weapon.

        A. The user will have to navigate to a weapon of their choice that they wish to purchase. This step has been covered in the first time visitor section.

        B. once a user has navigated to their weapon of choice they will have a few different option on this page. The page contains information about the weapon itself such as its name, 
            manufacture, Type of weapon, Price and a short paragraph about the weapon. At this point the user can ether choose to keep shopping as it is not the weapon they have been looking for
            or they can choose to add it to their bag ready to purchase it.

        C. The other choice the user has is to navigate to the bottom of that weapons page and this is where the reviews are sitatued. The user can read through other peoples reviews and also
            add reviews themselves.

        D. If a user wishes to leave a review about the weapon to help other users they can click the add review button. When they click this button they will be directed to the add review page.
            At this point I would like to mention that if a user does want to leave feedback or a review when using the website they must be signed in this is so the organisation can keep track of people
            leaving reviews and feedback. When the user is on the add review page they will have to fill out a simple form and on submitting this form they will be redirtected back to that weapons page and
            their review will have been added.
        
    * As a returning visitor, I want to be able to purchase weapons of my choice.

        A. Users will be able to purchase a weapon of their choice by navigating to the weapon they wish to purchase and clicking the add to basket button.

        B. When clicking this button they will be hit with a notification with a go to secure checkout button. If the user continues to press this button they
            they will be directed to the shopping bag page.

        C. On this page the user will have a few different choices. If the user decides they dont just want one of that weapon then they can update the quantity on this page with the price also
            being automatically updated for them.

        D. What if the user changes their mind and decides they dont want that weapon at all then also on this page the user has the option to remove that weapon from their basket. On clicking remove
            the basket will be updated.

        E. If the user decides everything is correct with the order and they wish to purchase the order then they can click the secure checkout button. On this page the user will be required to fill out
            a billing details form, this form is simple to fill out and if the user has already filled this form out in their profile the form will be automatically generated for them all they will be required to do
            is fill out the payment details and add their name. Once the user is happy that the form is correct they can click the complete order button which will direct them to a checkout success page
            with all the details that the user requires to redeem their weapon or weapons. Once the order has went through and the user is on this page they can navigate round the website again.
        
* Frequent User Goals:

    * As a frequent user, I want to see more new weapons added.

        A. The site is designed so the super user will be able to add weapons to the database, edit existing weapons and delete weapons people are no longer buying.
            
        B. Also in the feedback section users can communicate to the organisation on which weapons they would like to see added to the site.
        
    * As a frequent user, I want to be able to edit and delete the feedback that I have left on the website.

        A. If a user wants to make changes or even delete the feedback that they have left then they will first have to sign into their account.

        B. Once the user is signed in to their account they will then navigate over to the feedback section. On this page they will be able to see all the feedback they have left
            and other users have left.

        C. The user will notice that only on the feedback that they have left they can edit and delete. They will be unable to edit and delete everyones feedback.

        E. If the user wishes to edit the feedback they have left then they would click the edit button situated at the bottom of the feedback they left. When this button is clicked
            the user will be redirected to a edit feedback page where their old feedback form will be loaded up. At this point the user can edit what they wish and then click submit.
            Once the user has submitted the form they will be redirected back to the feedback page where they can see their edited feedback.
            
        F. If the user decides that they wish to delete the feedback completely then all they have to do is click the delete button and the feedback will be no more.
        
    * As a frequent user, I want to be able to edit reviews that I have left on weapons.

        A. If the user has left a review on a weapon and then later decides that they wish to edit this review then first they must make sure they are signed in on the account that they left the review on.

        B. Once they are happy they are on that accont they will then navigate to the weapon they left the review on and they will notice that only the reviews that they have left have a edit button next to them.
            This is so a user can't just go and edit anyones review.

        C. When the user has found the review they wish to edit they can click the edit button which will direct them to the edit review page. Once on this page the user will see the form that they previously filled out
            with all the previous information in it. They can edit what they need and then submit the form.
            
        D. Once the form is submitted by click the edit review button the user will be redirected back to that weapons page where they will see their edited review.

        E. The user will notice that on this page they dont have the ability to delete their review. Being the developer of this site I believe that every review bad or good should be left on the site as the more information
            other users wishing to purchase the weapon have is better for them when making their decision.


### Further Testing:

* The Website was tested on Google Chrome
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 6/7/8, iPhone X, iPad and iPad Pro
* A large amount of testing was done on each page to make sure that they were all linking correctly.
* Every button on the site was tested to make sure that the user was directed to the correct page when clicking them.
* A large amount of testing went on the payment form to make sure that the form worked correctly so the users can place orders.
* Testing went into the feedback page especially the edit and delete buttons to make sure that only the signed in user could edit and delete their own feedback and not other users.
* The same amount of testing went into the review page to make sure users could only edit their own reviews.
* I had Code Institute tutors sign up to the site and got them to submit a review or feedback or make a purchase to make sure this was all working correctly.
* Friends and family were also asked to sign up to the site to help point out some bugs and any user experience issues.
* I tested the Manage Weapons page ti make sure it was allowing me to add weapons to the site this is only for the superuser.
* Also just for the superuser I tested the edit and delete weapons buttons on the weapons page to make sure I was being firstly directed to the correct form and secondly when the form was submitted the changes were made
  or the weapon was deleted.
* Testing took place on the search bar, searching for specific weapons and making sure only that weapon is brough up. But also searching for manufactures and making sure the correct weapons show.


### Python Testing:

As well as testing Borderlands Buddy as stated above I also used python to test certain files in my project specifically view.py files and form.py files. These tests that I wrote basically test specific parts of 
functions and make sure they are acting as they should be. To test these functions you would enter the following in the console.
* python3 manaage.py test - This will test all the test.py files
* python3 manage.py test checkout.test_forms - This will tests a specific apps test.py file specifically the test_forms.py file, you can change this input depending on the app you are wanting to test and the file you are wanting to
  to test. For example if you wanted to check the feedback apps view file you would input the following in the console python3 manage.py test feedback.test_views.
* If you wanted to test a specific app file and that files specific function you would input the following in the console python3 manage.py test checkout.test_forms.TestOrderForm.test_customer_name_is_required.
  Inputting this in the console will first go to the checkout out apps test_forms.py file find the TestOrderForm class and then find the specific test_customer_name_is_required function and test it.


### Known Bugs:

* On smaller mobile devices the shopping bag on the navigation bar is pushed below the rest of the links.
    - This causes the navigation bar link to look out of place. However this does not show in the developer tool this only shows when you are actually looking on some mobiule devices for example it shows on my iPhone X
      But not on the iPhone X view in developer tools
    - This also causes there to be no margin at the bottom of the homescreen information box. 
    - I have already made these links smaller so that on the larger mobile devices they are on the same line i'm afraid that making them even smaller to suit smaller devices will make the links harder to press and may cause users
      to click other links when trying to press the search bar for example.


# Deployment

### Heroku
The project was deployed to Heroku using the following steps:
1.  First I logged into my Heroku account and clicked "New" then "Create New App" this then directed me to the Create New App page.
2.  From here I can give my app a name and then choose the region that is closest to me, now I am ready to click create app.
3.  I will now be directed to the new apps home page where I have many option to add things like config vars.
4.  Now on this page I will click resources and go to the Add-ons section. in this box I will provision a new postgres database by searching postgres and clicking Heroku Postgres.
    I will make sure that I am using the free version and click provision.
5.  To use postgres I have to navigate back over to my gitpod workspace and install dj_database_url and psycopg2-binary I do this with the following commands in the terminal "pip3 install dj_database_url"
    and "pip3 install psycopg2-binary"
6.  Now these are installed I will freeze the requirements by using the command "pip3 freeze requirements.txt" in the terminal window, this will make sure heroku will download all my apps requirements when I deploy it.
7.  I will get the new database set up by importing dj_database_url in my settings.py file.
8.  Now still in settings.py I will scroll down to the databases setting and comment out the default configuration and replace it with a call to my dj_database_url
9.  Going back to heroku I will navigate over to settings and reveal config vars and copy and paste my DATABASE_URL into my new database I just created in my settings.py file.
10. With this all saved I am ready to connect to my new heroku databse and run migrations. Because I am now connecting to postgres I need to run all these migrations again, I can see this because if I run the showmigrations command
    in the console none of my migrations are marked off. So if I run python3 manage.py migrate it will run all those migrations and get the database all set up.
11. Now I need to import all my weapons data to do this I will use my fixtures. By running the following commands in the terminal it will load all my weapons data back into the database "python3 manage.py loaddata categories" and then
    "python3 manage.py loaddata weapons".
12. Finally I will need to create a super user to log in with to do this I run the command "python3 manage.py createsuperuser" and fill out the fields that it requires.
13. With this finished my heroku app and database are ready to go, however before I commit I am going to remove the heroku database config and uncomment the origional database in my settings.py file. This is so my database url doesnt end
    up in version control.
14. With this done I can now commit and push to github. 
15. Now because I have removed the heroku database I need to write an if statement in my settings.py file so that when the app is running on heroku the database is connecting to postgres, otherwise it will connect to sqlite.
16. Once I am happy with my if statement I need to install gunicorn in the terminal so my app will work on the first try of deploying it. I done this with the following command "pip3 install gunicorn". Now that it is installed 
    I need to freeze it in to my requirements file.
17. I will now create a procfile by right clicking in my Borderlands Buddy workspace and click create file. The file will be named Procfile, in this file I will tell heroku to create a web dyno which will run gunicorn and serve my django app.
18. Now I can log into heroku in the terminal window with the command "heroku login"
19. Once logged in I will need to temporarily disable collect static using the command "heroku config:set DISABLE_COLLECTSTATIC=1 --app borderlands-buddy" so that heroku wont try and collect static files when I deploy.
20. I will also need to add the host name of my heroku app to allowed hosts in settings.py, I will also add local host in there to so that gitpod will still work.
21. With all this saved I will now attempt to deploy my app by adding and committing my changes then push to github. Once it has pushed to github I will need to initialize my heroku git remote with the following command "heroku git:remote -a borderlands-buddy".
    I can now use the command "git push heroku master". If I have done everything right I will now see a link to my heroku app in the console [https://borderlands-buddy.herokuapp.com/]. When I click on the link it will take me to my deployed site,
    however there will be no static or media files being loaded this is where I will use amazon web services to store my static and media file and connect them to my heroku app.
22. I want to set up automatic deploy in my heroku app when I push to github to do this I will go to heroku app page and navigate to the deploy section, on this page I will go to Deployment Method and set it to github and then search for my
    repository and click connect. Once its connected I can enable automatic deploys and now everytime I push to github my code will automatically be deployed to heroku.
23. Before commiting to heroku I am going to update my secret key in my settings.py file. First I am going to search for a django secret key generator and copy a secret key. Going back to my heroku config vars I will paste this secret key
    in a var called "SECRET_KEY". Now I can go back to my gitpod workspace settings.py and replace the SECRET_KEY setting with a call to get it from the environment and use a empty string as a default.
24. Just under this setting I will set DEBUG to be True only if there is a variable called development in the environment, Now I can commit these changes and push them to github. Navigating over to Heroku and activity I can see there is a build
    in progress and my automatic deployments are working.


### AWS S3

This is a cloud based storage service that will give me a small piece of amazon's infostructure that I can use to store my static and media files. To set this up I used the following steps:
1.  To get things started I navigated over to [https://aws.amazon.com/] and signed into my account.
2.  Once I was signed in I will search for s3 and open it to create a new bucket that will be used to store my static and media files. I clicked create bucket and named it to match my heroku app name to keep things simple. I was now asked to select a region
    for this I selected the one that was closest to me. I then unticked block all public access and created the bucket.
3.  I now need to set a few settings on the bucket I just created. First in properties I will turn on Static Website Hosting which will give me a new end point I can use to access it from the internet. For the index and error document I inputted index.html and error.html
    and saved it.
4.  Now navigating to the permissions tab I am going to make two changes. First in the CORS configuration I am going to set up the required access between my heroku app and the s3 bucket. Second in the bucket policy tab I am going to click policy generator
    so I can create a security policy for this bucket. The policy type will be s3 bucket policy, I will allow all principals by inputting * in the field, and the action will be set to get object. Now I will copy the ARN which can be found in the bucket policy tab
    and paste it in the field required back on the policy generator page. Once this is done I will click add statement then generate policy, then copy the policy it just generated into the bucket policy tab back in my bucket. But before I save it I am going to allow
    access to all resourses in this bucket by adding /* at the end of the "Resource" key and now I can save. With all this done my bucket is ready.
5.  With the bucket ready I am going to create a user to access it, to do this I am going to use another service in aws called IAM. The process I am going to use here is to first create a group for a user to live in then create an access policy giving the group
    access to the s3 bucket I created and finally I will assign a user to the group.
6.  First I navigate to Groups and create a new group called "manage-borderlands-buddy", now clicking next step and next step again I can click create group.
7.  Now I can create a policy used to access my bucket by clicking policies and create policy, clicking on the JSON tab I will navigate over to import managed policy which will let me import one that aws has pre-built for full access to s3. I will search for
    s3 and then import AmazonS3FullAccess. Now I dont want to allow access to everything I just want to allow access to my new bucket and everything within it. To do this I will need to copy the buckets arn from the bucket policy page in s3 and paste it
    in the resource key back in IAM. I will paste it twice once without /* on the end of it and one with /* on the end of it. With this done I have all s3 actions allowed both on the bucket itself and on everything in it. Now I can click review policy, I will
    give it a name and a description and click create policy. This will take me back to the policy page where I can see the policy has been created.
8.  I can now attach the policy to the group I created, I will go to groups and click my manage-borderlands-buddy group, click attach policy and search for the policy I just created and select it and click attach policy.
9.  Now I will create a user to put in the group, on the users page I will click add user and add a name of borderlands-buddy-staticfiles-user give them programmatic access and click next. Now I can put the user in the group I created, I will
    select manage-borderlands-buddy and click next till I get to the end and then click create user. Once I have done this I can click download .csv and this will download the users access key and secret access key which I can use to authenticate
    them from my django app.
10. Now its time to connect django to my s3 bucket to do this I will need to navigate back over to gitpod and install two new packages boto3 and django-storages, once they are installed I can freeze them into my requirements.txt so they will be installed 
    on heroku when I deploy. I also need to add storages to my installed apps in my settings.py file.
11. To connect django to s3 I need to add some settings in settings.py to tell django which bucket it should be communicating with.
12. With these settings added I will now navigate over to heroku and add my aws keys to my config variables. These are what I downloaded from the .csv file.
13. Whilst I am in my vars I am going to remove DISABLE_COLLECTSTATIC beacuse now when I deploy to heroku this time django will collect static file and upload them to s3.
14. Back in my settings.py file I will need to tell django where my static files will be coming from in production which will be AWS_S2_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
15. Now I will need to tell django that in production I want to use s3 to store my static files whenever someone runs collect static and I want any uploaded weapon images to go there also. To do this I will create a file called custom_storages.py
    and import settings from django.conf and also import S3Boto3Storage from storages.backends.s3boto3. I will create a custom class called StaticStorage that will inherit the one from django storages giving it all its functionality, in this class
    I will tell it I want to store static files in a location from my setting.py. I will repeat this process but this time the class will be called MediaStorage.
16. Going back to settings.py I will tell it for static file storage I want to use the storage class I just created and that the location it should save static files should be a folder called static I will repeat this process for media files and tell
    it to save files to a folder called media.
17. I also need to overide and set the URL's for static and media files using my custom doamin and the new locations.
18. What will happen now is when my project is deployed to heroku, heroku will run python3 manage.py collectstatic during the build process which will search through all my apps and project folders for static files and it will use the
    AWS_S3_CUSTOM_DOMAIN setting in conjunction with my custom storage classes that tell it the location at that URL where I would like to save things.
19. To make sure this works all I need to do is add all the changes, commit and push to github which will trigger an automatic deployment to heroku. If I navigate over to my s3 bucket I will see a static file in there with all my static files in it.
20. Now I have got all my static files working correctly I am going to get all my media files working.
21. Navigating over to s3 I am going to create a new folder called Media, opening the media folder I will click upload and then add files and simply select all my project images and click open. Now I will click next and then upload this will
    upload all my project images into the new media folder I have just created in s3. Now because I havent yet verified my superuser in the admin I will do so otherwise I wont be able to log into my project.
22. Finally to finish this off I am going to add my stripe key in my heroku config variables. I can find my stripe keys by loggin in to my stripe account at [https://stripe.com/gb] and navigating over to developers and then api keys.
23. Back in stripe I need to setup a new webhook endpoint as the current one is sending webhooks to my gitpod workspace. Once I have done this I will get a webhook signing secret that I can add to my heroku config variables. To test that this is working
    I will send a test webhook from stripe to make sure my listener is working.
24. With all this complete my Borderlands Buddy app is now fully deployed for anyone to see on the internet.
        
