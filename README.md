## About
TalentEd is a platform for freelancers to share their talents and get hired. The purpose of this platform is to help talented people to share their experiences. Everyone that is registered can comment, like and share their talents with the world. 

![Home Page](/instructions/hemmmm.png) 


The Live Site can be found [here](https://talent-ed.herokuapp.com/).

## Table of Contents
* [User Experience](#user-experience)
    * [Admin](#admin)
    * [Member User](#member-user)
    * [General User](#general-user)
* [Features](#features)
    * [Existing Features](#existing-features)
* [Future Features](#future-features)
* [Wireframes](#wireframes)
* [Structure](#structure)
* [Databases](#databases)
    * [Post Model](#post-model)
    * [Comment Model](#comment-model)
* [Technologies Used](#technologies-used)
* [Frameworks, Libraries & Tools Used](#frameworks-libraries--tools-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## User Experience
I have designed this platform with an aproach of design thinking. The basic and necessaryinformation. The user are able to go through the site with ease and get the information they are looking for.
My user stories can be checked [here](https://github.com/Onursoyar/TalentEd/issues)
## Admin
* As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
* As a Site Admin I can create, read, update and delete posts so that I can manage the content.
* As a Site Admin I can aproove Posts before it is published so that the site content will be consistent.

## Member User
* As a Member User I can register an account so that I can manage my posts, comment and like.
* As a Member User I can post/add/edit/delete poems so that I can share and manage my poems.
* As a Member User I can like or unlike a post so that I can interact with the content.
* As a Member User I can leave comments on a post so that get in touch with other talents.

## General User
* As a Site User I can view a list of posts so that I can select one to read.
* As a Site User I can click on a post so that I can read the full text.
* As a Site User / Admin user I can view comments on an individual post so that I can read the conversation.
* As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.


## Features
### Existing Features
* **Home Page**
    * The home page is built with minimal content to keep it clean. The page has a Navigation bar, information scroll down buttons and a button to directly go to the posted talents page. In the navbar a use can easily login or signup. Once the user is signed in, the user can add, edit or delete a post through the navbar.
        
        ![Home Page](/instructions/homepage.png)

    * Once the user is logged in member, the navigation bar will change. The use will be able to add, delete or update posted. The look of the navbar is going to change.
        
        ![Home Page](/instructions/navbar.png)
    
    * The talents button takes the user to the list of page where the talents are posted.

* **Talents Page**
    * Talents page is the page to see list of all the posted talents. 
    * The title, name of author, date of publication and number of likes isvisible for each post. 

        ![Poems Page](/instructions/talents.png)

    * This feature helps users to choose which talent they want to go through.
    
* **Sign Up**
    * Users can register and create their an account. 
    * The sign-up form checks if the username is used by someone else, alerts the user if any information is incorrect, such as passwords not matching or empty required fields.
    * Creating account enables access to more features. 
    * Registered members can publish and manage their talents (edit/delete).
    * These users can also like and comment on others posts.
        
        ![Sign Up](/instructions/signup.png)
    
* **Sign In**
    * Users can access their account via sign-in/login feature.
    * By singning in, the users can publish and manage their posts (edit/delete). They can also like and comment on other posts.
    * Users can find login option from the navbar menu.
    * If the user does not have a registered account, they can click 'sign up' on the menu and create an account.
        
        ![Sign-in](/instructions/login.png)

* **Logout**
    * The user can logout from Menu and from their accounts page.
    * When the user wants to logout a pop-up modal is triggered for confirmation. 
    * The logout modal asks the user if they confirm to logout.

        ![Logout](/instructions/logout.png)
    
* **User Account**
    * Once the user is registered or logged in, they have a user profile page. 
    * In this page users can publish or manage their posts. 

        ![User Account](/instructions/profile.png)
    
* **Publish a post**
    * Creating and adding a post is only possible for a registered user. 
    * The user can publish their talents after signing in and from their profile page.
    * The user must enter a title, content and image.

        ![Publish/Add poem](/instructions/publish.png)

    * The submitted post can be viewed/edited/deleted by the user from 'My posts' page.

* **Manage my posts Page**
    * User has the control to their published posts.

        ![Manage My Poems](/instructions/manage.png)

* **Edit a post**
    * Only the registered use of that specific post can edit the post.

         ![Edit a poem](/instructions/edit.png)

* **Delete a post**
    * The owner of the post can only delete it.
    * The posts that are chosen to be deleted asks the user for confirmation by pop-up alert on the window.

        ![Delete a poem](/instructions/delete.png)

* **Like and Comment on a post**
    * All the site visitors can view the comments and the number of likes.
    * The unregistered site visitors cannot view the comment box to write a comment. Once registered, only then is it visible for them and they can post a comment.

        ![View likes and comments](/instructions/comments.png)

    * The registered  members can like and comment on a post.


# Future Features
* Connect with Google translate API, so users can submit posts from different languages.
* Add more functions, such as to edit or delete a comment driectly while commenting.
* Add a chat function, so that the members can privately chat with eachother.


# Structure
The structure plan for TalentEd is to keep it simple and clean. The simplicity helps user to easily access and navigate within the website. 

Throughout the project development, GitHub projects is used. Click [here](https://github.com/Onursoyar/TalentEd) to view the process.


## Post Model:
Post model handles talent post details: the title, content, approval status, date created/updated, featured image and likes. This post model handles the base for confirming user/author authentication to manage their own posts.
    
## Comment Model:
Comment model handles the content of the comment, the username of the person commenting, date/time of commenting.

# Technologies Used:
* HTML
* CSS
* JavaScript
* Python

# Frameworks, Libraries & Tools Used
* Bootstrap - grid, layout, columns, cards and forms structure.
* Django - django frameworks to manage apps.
* GitHub - to store the overall project repository.
* GitPod - used as workspace to do the coding.
* Balsamiq Wireframes - To design the wireframe of the complete project.
* Google Fonts - to brandize 'Harmonic Poems' with google fonts. Used for logo and all the written content.
* Fontawesome - fontawesome icons for social media links and as additional design.
* Heroku - for the [deployement](#deployment) of the project.
* Coolors - to choose the color palette and color shades.
* PostgreSQL - database storage of the models.
* Cloudinary - image and static files storage.


# Deployment:
This project was deployed to Heroku. "Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps."- [Heroku.](https://www.heroku.com/)

<details>
<summary>Steps to open account in Heroku:</summary>
<br>
<ul>
    <li>
        <a href="https://signup.heroku.com/">Signup here </a>if you do not have an account already.
        <img src="instructions/heroku.png">
    </li>
    <li>
        After you fill in all the information for account and sign in, you will be on <a href="https://dashboard.heroku.com/apps">Dashbord.</a> Here it is where you will create an application.
    </li>
    <li>
        <p>Click on New => Create new app.</p>
    </li>
    <li>Choose a name to your application and select location that you are based.</li>
</ul>
</details>

<br>

The initial deployment was immediately after cretaing all the file directories within the repository. This is to ensure and overcome any deployment error before hand and resolve the issue before it gets more complicated.

<br>

<details>
<summary>Steps to Deployment</summary>    
I have followed Code Institute's <a href="https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf" target="_blank">Django Blog Cheat Sheet</a> steps to follow, create and deploy the project on Herokuapps.

<br>

<h2>Step 1: Installing Django and supporting libraries</h2>

<br>

<h3>In the terminal</h3>
<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Install Django and gunicorn:</td>
        <td>pip3 install django gunicorn</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Install supporting libraries: </td>
        <td>pip3 install dj_database_url psycopg2</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Install Cloudinary Libraries</td>
        <td>pip3 install dj3-cloudinary-storage</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Create requirements file</td>
        <td>pip3 freeze --local > requirements.txt</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Create Project</td>
        <td>django-admin startproject PROJ_NAME . (Don’t forget the . )</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Create App</td>
        <td>python3 manage.py startapp APP_NAME</td>
    </tr>
</table>

<br>

<h3>In the setting.py</h3>
<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>7</td>
        <td>Add to installed apps</td>
        <td>‘APP_NAME’,</td>
    </tr>
</table>

<br>

<h3>In the terminal</h3>
<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>8</td>
        <td>Migrate Changes</td>
        <td>python3 manage.py migrate</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Run Server to Test</td>
        <td>python3 manage.py runserver</td>
    </tr>
</table>

<br>

<h2>Step 2: Deploying an app to Heroku</h2>

<br>
<ul> 4 stages:
    <li> Create the Heroku app</li>

    <li>Prepare our environment and settings.py file</li>
    <li>Get our static and media files stored on Cloudinary</li>
</ul>

<br>

<h3>2.1 Create the Heroku app</h3>

<p>1. Create new Heroku App</p>

<p>2. Add Database to App Resources - Located in the Resources Tab, Add-ons, search andadd e.g. ‘Heroku Postgres’</p>


<p>3. Copy DATABASE_URL - Located in the Settings Tab, in Config Vars, Copy Text</p>

<br>



<br>

<h3>In Heroku.com</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>8</td>
        <td>Add Secret Key to Config Vars</td>
        <td>SECRET_KEY, “randomSecretKey”</td>
    </tr>
</table>


<br>

<h3>2.3 Prepare the environment and settings.py file:</h3>
<h3>In settings.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>9</td>
        <td>Reference env.py </td>       
    </tr>
    <tr>
        <td>10</td>
        <td>Remove the insecure secret key and replace - links to the secret key variable on Heroku</td>
        <td>SECRET_KEY = os.environ.get('SECRET_KEY')</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Replace DATABASES Section (Comment out the old DataBases Section) - links to the DATATBASE_URL variable on Heroku</td>
    </tr>
</table>

<br>

<h3>In the terminal</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>12</td>
        <td>Make Migrations</td>
        <td>python3 manage.py migrate</td>
    </tr>
</table>

<br>

<h3>2.4 Get our static and media files stored on Cloudinary:</h3>
<h3>In Cloudinary</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Copy your CLOUDINARY_URL e.g. API Environment Variable.</td>
        <td>From Cloudinary Dashboard</td>
    </tr>
</table>

<br>

<h3>In env.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>2</td>
        <td>Add Cloudinary URL to env.py - be sure to paste in the correct section of the link</td>
        <td>os.environ["CLOUDINARY_URL"] = "cloudinary://9444:ExampleCloudinaryi@dbhyuj5mc"</td>
    </tr>
</table>

<br>

<h3>In Heroku</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>3</td>
        <td>Add Cloudinary URL to Heroku Config Vars - be sure to paste in the correct section of the link</td>
        <td>Add to Settings tab in Config Vars e.g. COUDINARY_URL, cloudinary://9444:ExampleCloudinaryi@dbhyuj5mc</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, must be removed before deployment)</td>
    </tr>
</table>


<br>

<h3>In settings.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>5</td>
        <td>Add Cloudinary Libraries to installed apps (note: order is important)</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Tell Django to use Cloudinary to store media and static files. Place under the Static files Note</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Link file to the templates directory in Heroku. Place under the BASE_DIR line</td>
        <td>TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array</td>
        <td>'DIRS': [TEMPLATES_DIR]</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Add Heroku Hostname to ALLOWED_HOSTS</td>
        <td>ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]</td>
    </tr>
</table>

<br>

<h3>In Gitpod</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>10</td>
        <td>Create 3 new folders on top level directory</td>
        <td>media, static, templates</td>
    </tr>
     <tr>
        <td>11</td>
        <td>Create procfile on the top level directory</td>
        <td>Procfile</td>
    </tr>
</table>

<br>

<h3>In Procfile</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>12</td>
        <td>Add code</td>
        <td>web: gunicorn PROJ_NAME.wsgi</td>
    </tr>
</table>

<br>

<h3>In Terminal</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>13</td>
        <td>Add, Commit and Push </td>
        <td>
            <p>git add . </p>
            <p>git commit -m “Deployment Commit”</p>
            <p>git push</p>
        </td>
    </tr>
</table>

<br>

<h3>In Heroku</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>14</td>
        <td>Deploy Content manually through heroku/</td>
        <td>E.g Github as deployment method, on main branch</td>
    </tr>
</table>

<br>

<p>Before the final Deployement: Remove the "DISABLE_COLLECTSTATIC" from Heroku Config vars, and Change Debug to "False" in settings.py</p>

</details>

<br>


If using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MerveKucukzoroglu/reading-tracker)


# Credits
During the process of project development, there have been various sources that gave me idea how to do a particular feature or fix a bug. The following are the sources that I got knowledge from:
* [Stack Overflow](https://stackoverflow.com/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/#)
* [Django Project Documentation](https://www.djangoproject.com/)
* [Code Instiute](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=581817633089&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjw0PWRBhDKARIsAPKHFGgmnuTJCpzeJBqKg9fy2p-7NlU8NY95XaXmoPzBpuDdIekQWqUKxocaAso5EALw_wcB) course materials and Django Blog Walkthrough Project.
* [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
* [Bootstrap Modal](https://getbootstrap.com/docs/5.1/components/modal/#tooltips-and-popovers)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [User registration email form and views by Corey Schafer](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6) for future email verification purposes.
    * forms.py 
        ```python
        class UserRegisterForm(UserCreationForm):
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
        ```
    * Views.py
        ```python
            def register(request):
                if request.method == 'POST':
                    form = UserRegisterForm(request.POST)
                    if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        messages.success(request, f'Account created for {username}!')
                        return redirect('profile')
                    else:
                        form = UserRegisterForm()
                return render(request, 'account/signup.html', {'form': form})

        ```
* I have taken my inspiration for the project from the blog applications that we have done with the code institute. On top of that I have taken logic, some code and general information and structure from this profile and project [Click here](https://github.com/MerveKucukzoroglu/harmonic-poems).


# Acknowledgements
I would like to acknowledge and present my thanks to my mentor at Code Insitute for his guidance and constant support. It wouldn't have been possible without the amazing community in Slack, Tutors of Code insitute Tutor supports, and my friends who constantly motivated and supported me.