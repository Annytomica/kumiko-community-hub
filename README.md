
![header](static/images/kch-brand.png)

# Kumiko Community Hub

KCH is a vibrant community hub for individuals who are passionate about kumiko, providing a welcoming space for people to learn, share, and grow their skills in this intricate art form. Through workshops, tutorials, and collaborative projects, members can deepen their understanding and appreciation of kumiko while connecting with others who share their enthusiasm. Whether you're a beginner eager to explore or an experienced artisan looking to refine your techniques, KCH fosters a nurturing environment where creativity thrives and friendships flourish.

The live website can be accessed [here](https://kumiko-b16d8bc28246.herokuapp.com/) 

![home](static/images/home.png)

# Features

## Existing features
### Abstract template from StyleShout
The site layout is adapted from the free bootstrap template from [StyleShout](https://styleshout.com/abstract-modern-masonry-blog-website-template/) called Abstract. It has a very clean, minimal style and a great gallery display design. It was chosen due to it's stylish implementation of 'masonry' tiling motion of gallery cards.
Custom html and CSS was built on top of this template to suit the project goals.
Usage of this template did not come without issues and in particular Abstract forms classes interfered with django forms and crispy-forms behaviours.

### Hero banner
The hero photography is if Kumiko projects carried out by Anny Devoy, with the photograpgy by Megan Abel. It has a very simple message about the core principles of the community and invites people to join. The hero is a picture element, with differnt images to make efficiently responsive to screen size.
![large hero image](static/images/kch-hero_image-1200px-2.webp)

### Logo
The logo was designed by Megan Abel, a graphic designer and wife of the site owner. The logo reflects the style of kumiko panels while incorporationg the KCH intials of the Kumiko Community Hub.

![logo](static/images/kch-logo.png)

### Article Gallery
The article gallery on the homepage displays cards of individual articles, with card heights varying according to excerpt length. The cards act as links to the full article. 
#### Masonry brick animated cards
The gallery from the Abstract template is based on Masonry which is a JavaScript grid layout library made by [David DeSandro](https://masonry.desandro.com/). It works by placing elements in optimal position based on available vertical space, like a mason fitting stones in a wall. This leads to a adaptive animation of the cards as screen size and card height changes. The card visual styling comes from the Abstract template.

![gallery](static/images/gallery.png)

#### Pagination
Gallery pagination is set to display of a maximum of 8 cards per page, with arrows and page numbers for navagation. The active page number is highlighted visually to assist user navagation.

![pagination](static/images/pagination.png)

### base.html
The base.html contributes all page meta, css and js links plus Navbar, footer and alert messaging areas.
#### Navbar
The Navbar has KCH branding, links to Home, About and Contact on the right, and adaptive links to login/logout/register based on login status as well as a displaying a statement indicating login status. If logged in it contains username as part of 'you are logged in as...' statement.

![navbar_screen](static/images/navbar_screen.png)

The small screen navbar drops down from top, with navagation to left and login/logout status and links to right.

![navbar_tablet](static/images/navbar_tablet.png)

#### Footer
The footer styling comes from Abstract template. It has a short description of KCH, links to pages and external social links, plus an invite to get in contact with a link to the contact form. It also has copyright and required acknowledgement to StyleShout for Abstract template usage.

![footer](static/images/footer.png)

### Single Article
The single articles page displays a single article instance along with likes and comments associated with that article.
#### Display of single article
The page provides a stylised visual presentation of all Article model field entries, except slug, author and status. Author is not displayed as presently only the super-user can submit an article through the admin panel. Cloudinary is used to externally serve the images.

![article](static/images/article.png)

#### Likes and comments counts
Number of likes and approved comments are displayed at top of article, just above the article image.

#### Like button
When logged in the like/unlike toggle button becomes visible. It toggles between outline (user has not liked article) and solid (user likes article). When solid it also add an increment of 1 to the likes counter.

![likes](static/images/likes.png)

#### Next and Previous articles
To improve UX, below the like button is a navigation section that displays links - with article titles - to the next and previous articles and button to return to the homepage with all articles.

#### Approved comments
Approved comments are displayed below the article. If the user is logged in and has a comment awaiting approval this will also appear in comments list. All comments made by the logged in user will also now display edit and delete buttons below to enable full CRUD functionality.

![comments](static/images/comments.png)


#### Comment form
When logged in the comment form is displayed and the user can submit a comment. If the user wants to edit a comment the comment is displayed in the form to change and resubmit.

![comment_form](static/images/comment_form.png)

### About Us
The about us page displays an about instance.
#### Display of about
The page provides a stylised visual presentation of all about model field entries. Cloudinary is used to externally serve the images.

![about](static/images/about.png)

#### Register Banner
The about page has a banner inviting new visitor to join the community and links to the sign-up page.

### Contact
The contact page displays a contact instance.
#### Display of contact
The page provides a stylised visual presentation of all contact model field entries, except updated_on. Cloudinary is used to externally serve the images.

![contact](static/images/contact.png)

#### Contact form
The contact form allows a site visitor to send a message to the site admin. There is no requirement for the user to be logged in for this action.

## Future features
### User submitted projects gallery
A key future development, given kumiko is a very visual craft/artform, it to provide community members an opportunity to share images of thier own projects with a short description. This would allow members to submit an image and short description, which would get displayed in a community gallery after admin approval. The gallery would have smaller cards than article gallery and users cn click on card to open a modal (instagram-style) to read full description and leace commments and likes. The ability to like a project straiht off the card would also be important.

### Homepage that displays selction of articles and user submitted projects
Once community project submissions are enabled the homepage shows a selection of both articles and submitted projects, with new projects and articles gallerys on seperate pages with pagination.

### Conversation Threads
The ability to respond to a comment directly and start a discussion thread from that comment. Presently all comments are independent


# Project Design and Implementation
## Development Process

The project was systematically developed using the following workflow. Principles of **Design Thinking** were implemented to create the project outline, identify the target audience and set clear goals for the project. The project structure and **data models** were then defined, with an ERD generated to show model interactions. **Wireframes** were developed for the project, to define the UI and UX and each page tempaltes structure. **Agile** methods of project management were then implemented, including defining core Epics, user stories, chores and tasks, by taking advantage of **GitHub Agile tools**. Once this was completed the core **technical development** of the Django project was started, systematically building one app at a time until project complete. **Testing** was carried out as new features and app were developed, **automated testing** was carried out for all views and forms at the end of development, followed by a final comprehensive **manual testing** period carried out by multiple testers using a multitude of devices. **Code validations** were then done along with the final update to the **README.md** before submission of the project for external assessment.

## Project Rationale
A full site project outline can be viewed [here](https://docs.google.com/document/d/1W2LfAeY3Gkv_EZSodBBBzSgNinVPhwcOKg3yjh0x3Fs/edit?usp=sharing)

In summary, is a social initiative to support a community space for people interested in the Japanese woodcraft of Kumiko - detailed geometric wood panels for interior decoration applications. It is for those who have a background in woodcraft including Japanese joinery and Kumiko or who want to learn. The site allows users to access and share information about Kumiko and related resources.

## Goal
 A website that:
 - is user friendly and intuitive
 - provides useful information to the community
 - encourages sharing of information through comments and messages to site admin
 - encourages engagement and support through ability to 'like' content
 - Has easy interface for site adim to upload new articles with auto-formatting of content

## Data Models
### Project structure

![structure](static/images/project-structure.png)

### Data models ERD

![erd](static/images/erd.png)

The data models used are summarised as follows:

Article:
- article: 
   - stores all information for presenting a single article
   - Foreign key: User
- article like: 
   - stores like status for single article
   - Foreign keys: User and Article
- article comment:
   - stores comments for single article
   - Foreign keys: User and Article

About:
- about: stores all information for presenting a single about us page. No foreign key.

Contact:
- contact: stores all information for presenting a single contact page. No foreign key. 
- contact form: stores message from user for admin to view. No foreign key.

## Wireframes
Wireframes for the project were developed in Balsamiq. The site consists of four templates - home, single article, about us and contact. The wireframes can be viewed as a pdf [here](static/images/wireframes.pdf)

## Agile project management
The project was managed using GitHub Agile tools - issues, project boards, labels and milestones.
### Issues templates
Custom issues templates were generated for Epics, User Stories, Chores, Tasks and Bugs.
### Labels
Custom labels for tagging issues were generated. They were grouped into two areas - issue type and issue importance.
- Issue type: Epic, User Story, Chore, Task (Bug already exists in github as default)
- Issue importance - Must have, should have, could have and won't have.
### Milestones
Milestones were created for key deadlines (eg. MVP submission deadline) and iterations.
### Github projects
Two projects were set up - KCH Scrum Board and KCH Task Board. 
- **KCH Scrum Board:** This project consists of a Scrum Board and a Roadmap and can be found [here](https://github.com/users/Annytomica/projects/8/views/2). The Scrum board has 6 columns:
   - No status - for epics only as these were not assigned milestones.
   - Backlog: For all user stories, chores and bugs awaiting assigment to an iteration
   - Ready: User stories, chores and bugs assigned to iteration but not yet started.
   - In progress: User stories, chores and bugs actively being worked on.
   - In review: User stories, chores and bugs completed but not yet fully tested for functionality.
   - Done: Epics, User stories, Chores and Bugs that are completed.

   The Roadmap was used to track the issues timelines and completions. It was also used to track workload for an iteration and ensure it was not overly optimistic for number of issues to complete.
- **KCH Task Board:** This project consists of a single task board and can be found [here](https://github.com/users/Annytomica/projects/9/views/1). This board was used to track tasks only, with the tasks assigned to specific user stories or chores. It replicates the column format on the scrum board, except lacks the no status column due to no epics being included on this board.

### Issues
Initial issues to fulfil the basic goals of the project, consisting of Epics, User Stories, Chores and Tasks, were defined before any technical development of the project began. They were outlined in a google sheet that can be found [here](https://docs.google.com/spreadsheets/d/108McokctYqyY1FebOTyf3hxA48sUfmqkOYjqKMCINfU/edit?usp=sharing). Additional issues were added to the sheet as the project progressed. 

Issues were transfered to the relevant project boards as and when required, using the issues templates created at the start of the project. This ensured the backlog columns were not overloaded and issues were easily identified and transfered to ready column when required.

#### Issues Summary:
In total **128** issues were generated for the project, consisting of 9 Epics, 19 User Stories, 38 Chores, 54 Tasks and 8 Bugs.

### Iterations
Iterations, defined using Github milestones, standardly ran with a timebox of 2 days unless a known 'no work' day was within that timeframe. MoSCoW labels were applied to issues as they were assigned to an iteration, with the rule that no more than 60% could be defined as 'must have' per iteration.

## Technical Development
The app development process, for each app included in the project, followed the steps outlined below:
1. create app in kumiko Django project
2. Do minimum wireup of settings.py, views.py and urls.py and creating html template as defined in SI coursework
3. Set up models and link to views and urls
4. test model in admin panel
5. Create appropriate views in views.py to display information stored in database model. One view taken through dev steps 5-9 at one time and then process repeated for next.
6. create appropriate form method in forms.py if required for view
7. add view specific html to template to display the view on the website
8. deploy changes (with collect static) to test views on deployed site
9. Final testing of fully completed app

# Technologies
- Django - all app functions
- Bootstrap
- HTML/CSS/JS
- Cloudinary + dj3-cloudinary-storage - for image storage and management
- Django-crispy-forms - for assistance with form content and processing
- gunicorn - for Heroku deployment of Django project
- Django-allauth - for user validation
- Django-summernote - for auto text area formatting assistance
- WhiteNoise - to assist serving of static files on Heroku
- Figma – flowchart development
- Balsamiq - wireframe generation
- Photoshop - image processing
- ChatGPT - troubleshooting, typo finding and logic problems
- Heroku - app deployment and hosting
- google docs, sheets and slides
- Pixelied.com – conversion of jpeg and png image files to webp for efficient loading
- Favicon.io – generation of favicon from logo design.
- UI.dev – amiresponsive was used to create site mockup images.

# Testing

## General Strategy
Functions were tested as they were developed by running within IDE server (Gitpod). The site was first deployed to Heroku once the project and first app (article) had minimal wireup. Regular deployments, 4-5 times a day were carried out as features were developed. In this way all features were tested during development on the deployed site as well as IDE server to ensure features not impacted by deployment. If changes to any static files were updated or added 'collectstatic' command was used in terminal before testing features. 

All functions, including prescence of any validation messages, were tested after each deployment.

### Automated Testing
Django built-in testing (Unittest) was used to test functionality of forms and views for each app. Where features to be tested were complex the development of tests was carried out with assistance from the CI Blog walkthrough project and ChatGPT. Testing of template useage was taken from a [Medium article by Alice Campkin](https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178)


### Manual Testing
Final testing was carried out on last deployment after all code validations was carried out. It was carried out by multiple individuals on multiple devices (phones and laptops of each tester).

Core assessment criteria for all features were as follows:
- That they work as expected
- That you get a little feedback message at the top of the page if you successfully do something
- That you get a pop-up to confirm action if you are doing something negative like logout or delete a comment.
- That you get the expected visual changes to the site 

The final testing steps were as follows:

Before registering:
1. Check basic page navagation and links for all pages work as expected. To check:
   - Navbar (standard and mobile dropdown menu)
   - Footer
   - sign-up banners (home and about pages) take you to register page
   - sign-in link to sign-up page
   - sign-up link to sign-in page
   - homepage article thumbnail to single article page - does correct article load?
   - homepage pagination - do they work as expected and display correctly
   - single article next and previous articles - do they work as expected and display correctly
   - make general notes on usability and loading/responsivness of each page

Registration and beyond:

2. Account registration
   - register an account - does this work and do you navigate to logged in state on homepage?
   - logout - do you get confirmation request that you want to logout?
   - is logout successful with a small 'you have logged out' message sent
   - login - do you successfully log back in using new user credentials
   - does the navbar update to reflect logged in/logged out status
   - can you see your user-name displayed in navbar if logged in

3. Contact Page contact form
   - while logged out send a message that says 'this is a logged out message' - do you get a confirmation message of it being sent?
   - while logged in send another message that says 'this is a logged in message' - do you get a confirmation message of it being sent?
   - site admin checks and confirms both messages stored and can be marked as read

4. Single article page likes
When logged in:
   - can the like button at bottom of article be seen?
   - can the like button be clicked to register article as liked
      - does the heart go dark to indicate like
      - does the like counter increase by 1 to show registering of like
      - do you get a confirmation of like being recieved?
   - can you unlike a liked article?
      - does the heart go empty to indicate no like
      - does the like counter decrease by 1 to show removal of like
      - do you get a confirmation of like being removed?
When logged out:
   - does the like button disappear?
   - can you still see the same number of registered likes?

5. Single article page comments
When logged in:
   - can the comment form at bottom of article be seen?
   - can a new comment be submitted?
      - does the comment appear in the comments list, marked as awaiting approval?
      - do edit and delete buttons appear below the comment.
      - do you get a confirmation of comment being submitted for approval?
      - does the comment counter stay the same value (should only count approved comments)
      - do comments from other users lack the edit and delete buttons?
      - can you submit multiple comments on same article?
   - can you edit a comment?
      - does clicking on the edit button fill the comment form with the message to be edited?
      - does the submitted edit change the displayed comment?
      - do you get a confirmation of comment being edited?
      - does the comment counter stay the same value (an edit should not count as new comment)
   - can you delete a comment?
      - does clicking on the delete button get a pop-up asking for confirmation of deletion?
      - do you get confirmation of deletion if you delete?
      - do you return to previous state with no changes if you cancel delete?
      - does the deleted comment dissapear from comments thread?
      - does the comment counter stay the same value if deleted comment was not yet approved?
      - does comment counter decrease by 1 if deleted commented had been approved beforehand?
When logged out:
   - does the comment form disappear?
   - do your own unapproved comments disapear (should only see approved comments)
   - do edit and delete buttons disappear?
   - can you still see the same number of comments on counter?
   - on the gyokucho saw review article can you see the comment from kumiko_admin that says 'you should not see this comment as it is not approved'? (you shouldn't)

6. Superuser Admin
   - can you view and approve comments
   - can you view and mark as read messages from contact page from both logged in and logged out users
Articles:
   - can you submit an article
   - is the article immediately added to deployed site and displayed correctly?
   - can you edit an article and do changes display on site after saving
   - can you delete an article and does the article dissapear from site immediately
   - does the default image display if no image file is provided?
About:
   - can you submit content for about us page
   - is the content immediately added to deployed site and displayed correctly?
   - can you edit about content and do changes display on site after saving
   - can you delete about content (leads to empty page with no content on site)
   - does the default image display if no image file is provided?
Comment:
   - can you submit content for contact page
   - is the content immediately added to deployed site and displayed correctly?
   - can you edit contact content and do changes display on site after saving
   - can you delete contact content (leads to empty page with no content on site)
   - does the default image display if no image file is provided?

## Devices and Browsers

### Web browsers
Chrome (primary), Firefox , Edge 

### Devices
- Phones: Pixel4a, iPhoneXR, GalaxyS10
- Laptops: Dell Inspirion 13”, MacBookPro 13”, MacBook Air 13”, MacBook Pro 16" (new model), Microsoft Surface (v.old model)
- Desktop screens: BenQ PD series 27”

## Testing Summary
- During early testing phases, the interaction of classes from the Abstract template caused functional bugs at times and required significant troubleshooting to identify.
- The site worked on all devices and browsers tested, but issues were found on older devices. These issues were: 
   - the like icon does not always update after first like. This appeared to be due to slow submission and page loading being out of sink.
   - Django authorisation forms (register in particlular) which did not always perform as intended and submit details correctly. This issue was present on very old devices only and may have been a soft/hardware compatability issue.
- Recommendations for readability of login/register links in login/register forms was taken into account and changes make to improve.


Testing summarised below - green = behaves as expected, yellow = issue on older devices only, orange = works but behaviour not as expected, red = does not work

![testing-table](static/images/testing-table.png)

### Testing conclusion
This site underperforms on older devices and browsers. The issues are primarily driven by slow loading/submission times and Django third-party packages on these old devices. They were not deemed 'bugs' as all newer devices worked as expected. The masonary bricks are also laggy on old devices and an alternative may work better.

## Final Code Validation
HTML – all pages passed validation with no errors detected using the official [W3C HTML validator](https://validator.w3.org/). The summary of results can be found [here](static/images/html_validatons.pdf). There were multiple warnings about header order usage which were caused by using the Abstract template for styling, as this had predefined header structures.

CSS – the custom style.css file passed validation with no errors detected using the official [W3C CSS validator](https://jigsaw.w3.org/css-validator/). The summary of results can be found [here](static/images/css_validatons.pdf). The abstract.css file from the Abstract template was not tested.

JavaScript - all custom js files (likes.js and comments.js) passed vaildation with no errors detected using [JS Hint](https://jshint.com/). The summary of results can be found [here](static/images/js_validatons.pdf). JS files from the Abstract template were not tested (jquery-3.2.1.min.js, main.js, modernizr.js and plugins.js)

Accessibility – all pages showed high accessibility using Chrome [Lighthouse DevTools](https://developer.chrome.com/docs/lighthouse/). The summary of results can be found [here](static/images/lighthouse.pdf). The delivery of images without defined dimensions by Cloudinary caused some performance issues.

Python - PEP8 validation: all .py files passed validation with no errors reported from [CI pep8 python linter](https://pep8ci.herokuapp.com/). This was carried out on all admin.py, apps.py, forms.py, models.py, test_forms.py, test_views.py, urls.py,views.py and the settings.py file.


# Bugs
## Fixed
- Comment edit submitting new comment not changing old.

**Description:**
The submit process for edit not working and commentForm attribute not being assigned to allow submission of change. Is submitted as a new comment.
**Resolution:**
Found typo in submitButton single_article.html, but major issue was that the Abstract Id of contactForm was conflicting with the commentForm Id that needed to be identified to setAttribute of action="edit_comment" to change button action from submit to edit. The contactForm Id was removed to resolve.

- Nav dropdown menu not working and hiding logo

**Description:**
Conflicting styling causing dropdown menu on small screens to not align properly and hide logo and close button
**Resolution:**
changed logo file to webp and smaller dimensions. Removed abstract classes from nav elements as causing clashing with styling and menu issues. Added custom css to style.css to override how abstract css deals with navbar images (logo).

- Comment submission also submits like

**Description:**
When submitting a new comment the submission also submits a like.
**Resolution:**
Separated POST actions in views.py by ensuring comments actions only occurred when 'body' field included in submit, and like actions only when 'like' included.

- Can see unapproved comments

**Description:**
Can view other users unapproved comments
**Resolution:**
Lacked the conditional classes in comment view area in single_article.html. The conditional statement was added, such that if unapproved and author - message faded, if unapproved and not author - message hidden

- First article like does not register

**Description:**
First like does not register but does give a success message. Second and following attempts work fine.
**Resolution:**
First instance of user_like was not changing default value of False to True. This was resolved in single_article view by adding the statement 'like.like = True'

- Comment does not clear from form after submission

**Description:**
Article comment form does not clear after comment submitted and can be submitted again.
**Resolution:**
This was a bug introduced when fixing the bug associated with a like being submitted when a comment was submitted. It was caused by a change in logic for the view, where an empty form load was accidentally moved to before comment submission instead of after. The logic was reverted back to original order to fix the bug.

- like icon does not update on first like

**Description:**
First like is registered in model correctly but update of icon to solid heart on article page does not occur.
**Resolution:**
After like submitted in views.py added an update to like status, at same point like counts also updated.

- Single article page does not load if not logged in

**Description:**
When try to read single article without being logged in get UnboundLocalError: cannot access local variable 'user_like' where it is not associated with a value.
**Resolution:**
The initial statement 'user_like = None' had been commented out while troubleshooting other likes bugs. Comments removed so statement set default for all views as none.

- Cloudinary serving over HTTP, not HTTPS.

**Description:**  Cloudinary serves over HTTP, not HTTPS, indicating https default is being overridden. This gives a console warning and leads to low lighthouse score for best practises.
**Resolution:** '?secure=true' was appended to end of CLOUDINARY_URL in env.py and Heroku config vars, which ensures all cloudinary urls are https.

#### Neutral resolution
- Registration does not always show success message and reload back to home with logged in status. However, this seemed to be an issue on the oldest devices tested only and therefore marked as compatibility issue not as specific bug on site.


## Unfixed
**All bugs detected have been resolved**

# Deployment
For deployment this project uses Heroku. The app was deployed to Heroku using the process described in the CI Django module coursework. 

In summary:
1. Within the IDE used (Gitpod) a requirements.txt document was populated with the list of dependencies for correct deployment by entering the command 'Pip3 freeze > requirements.txt' into the terminal.
2. All static files were collected using the command 'python3 manage.py collectstatic'
2. Within Heroku the option for setting up a new app was selected and the following Config Vars (key - value) were set (from env.py):
        - CLOUDINARY_URL
        - DATABASE_URL
        - SECRET_KEY

3. The app was then deployed by connecting the corect GitHub repo (kumiko-community-hub) and selecting manual deployment option for the first deployment.
4. The deployment setting was changed to automatic once the majority of functions had been written and tested.

If you wish to develop this app further, feel free. To do this, create a fork of this repository and save it to your own github profile. To do this, use the fork button at the top right of this repository. This brings you to a new window, where you select yourself as the owner and can add extra details to name and description of the repo. You will then, if required, deploy to your own Heroku account using the process described above. You will also need to generate you own env.py and Heroku config var values to ensure all featuires will work. If you chose to do this, please be respectful and credit me as the origin of this project and code.

![GitHub language count](https://img.shields.io/github/languages/count/Annytomica/kumiko-community-hub)
![GitHub top language](https://img.shields.io/github/languages/top/Annytomica/kumiko-community-hub?color=yellow)
![GitHub watchers](https://img.shields.io/github/watchers/Annytomica/kumiko-community-hub)
![GitHub forks](https://img.shields.io/github/forks/Annytomica/kumiko-community-hub?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Annytomica/kumiko-community-hub?style=social)

# Credits
I would like to acknowledge and thank the following people and resources used in the creation of this site.

I would also like to note that this app was developed during a period where I was effectively homeless amd couch surfing with friends and family. I was deprived of reliable internet connections and ideal work spaces for significant periods of time. As such, normal support routes of mentor meetings and tutoring were not always available and ChatGPT was used as a replacement. While no code was directly generated by ChatGPT it does write out corrections for exisiting code, in a way that mentors and tutors do not, and I would like to acknowledge this fact.

## Content
### Large contributions
- [CI Blog walkthrough project](https://github.com/Annytomica/django-blog-walkthrough):
    - Basic code for setting up Django projects and apps
    - all wireups for views, models, urls were adapted from the course code with significant generic code retained
    - deployment to Heroku
    - third-party wireups such as Cloudinary, summernote etc used same versions as used in walkthrough to ensure they connected correctly with Heroku etc.
- The free Abstract boostrap template from [StyleShout](https://styleshout.com/abstract-modern-masonry-blog-website-template/) for providing all styling html, css and js to create a responsive masonary-brick based site. StyleShout is acknowledged in footer as per usage requirement.

- [ChatGPT](https://chatgpt.com):
    - typo identification
    - troubleshooting
    - optimising logic for like functions
    - correcting like/comments view to remove clash of submission (see bug report)
    - displaying article like and comment counts on homepage
    - fixing cloudinary http bug

- [Top Coder](https://www.topcoder.com/thrive/articles/project-management-on-github) for tutorial on how to use GitHub projects for Agile project management

### General contributions
- [Get Bootstrap](https://getbootstrap.com/docs/5.0/components/buttons/) for general bootstrap classes for styling layout and components

- [Compass](https://nimblehq.co/compass/product/backlog-management/user-stories/chores/) for how to use Chores effectively in agile project management

- [Web.dev](https://web.dev/learn/design/picture-element) for usage of picture element to improve performace of hero banner on homepage

- [Chaggy from Stack Overflow](https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms) for comment that introduced using widget to get placeholder text in crispy form input boxes

- [Medium article by Alice Campkin](https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178) for testing template usage in Django testing


## Media
- The photographs were taken by Megan Abel, my wife, who gave permission for thier use.
-	The icons such as like hearts and comment bubble are from [Font Awesome](https://fontawesome.com/)
- The Github summary bar used in README.md is from [shields.io](https://shields.io/badges/)

## Acknowledgements
- My wife, Megan, for help with the wireframe design, product photography, site testing and general emotional support while I was trying to study and code while also moving relentlessly.
- My mum for excellent testing assistance
- My mentor, Oluwafemi Medale , for his invaluable guidance and feedback and intital introduction to the concept of agile chores.
