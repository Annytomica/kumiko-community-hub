
![header](static/images/kch-brand.png)

# Kumiko Community Hub

KCH is a vibrant community hub for individuals who are passionate about kumiko, providing a welcoming space for people to learn, share, and grow their skills in this intricate art form. Through workshops, tutorials, and collaborative projects, members can deepen their understanding and appreciation of kumiko while connecting with others who share their enthusiasm. Whether you're a beginner eager to explore or an experienced artisan looking to refine your techniques, KCH fosters a nurturing environment where creativity thrives and friendships flourish.

The live website can be accessed [here](https://kumiko-b16d8bc28246.herokuapp.com/) 


![mock-up](assets/static/mock-up_amiresponsive.png)

# Features

## Existing features
### Hero banner
The hero photography is if Kumiko projects carried out by Anny Devoy, with the photograpgy by Megan Abel. It has a very simple message about the core principles of the community and invites people to join. The hero is a picture element, with differnt images to make efficiently responsive to screen size.
![large hero image](static/images/kch-hero_image-1200px-2.webp)

### Logo

### Article Gallery
#### Masonry brick animated cards
#### Pagination

### base.html
#### Navbar
#### Footer

### Single Article
#### Display of single article
#### Likes
#### Comments

### About Us
#### Display of about
#### Register Banner

### Contact
#### Display of contact
#### Contact form

## Future features
### User submitted projects gallery

### Homepage that displays selction of articles and user submitted projects

### Display of like and comment counts on gallery cards

### Update Django-cloudinary to newer version 
To allow presentation of images via HTTPS, not HTTP. Use of HTTP gives a warning in the console and significantly reduces the Lighthouse score for best practises for all pages displaying a Cloudinary-stored image.

### Increase user navigation ability
Present navigation back and forth on pages is limited. An ability to paginate through articles from the single article page would make a nice improvement to UX.

# App design process

## Rationale
A full site project outline can be viewed [here]()

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
![structure](assets/static/app_flowchart.png)

### Data models ERD
![erd](assets/static/app_flowchart.png)

The data models used are summarised as follows:
Article:
- article: stores all information for presenting a single article
- article like: stores like status for single article 
- article comment: stores comments for single article

About:
- about: stores all information for presenting a single about us page

Contact:
- contact: stores all information for presenting a single contact page
- contact form: stores message from user for admin to view


## Development process
The app development, for each app included in the project, followed the steps outlined below:
1. create app in kumiko Django project
2. Do mminimum wireup of settings.py, views.py and urls.py and creating html template as defined in SI coursework
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
- Cloudinary
- Django-crispy-forms
- gunicorn - for Heroku deployment of Django project
- Django-allauth - for user validation
- Django-summernote - for auto text area formatting assistance
- whitenoise
- Figma – flowchart development
- Photoshop - image processing
- ChatGPT - troubleshooting, typo finding and logic problems
- Heroku - app deployment and hosting
- google docs, sheets and slides
- UI.dev – amiresponsive was used to create site mockup images.

# Testing

## General Strategy
Functions were tested as they were developed by running run.py within IDE terminal (Gitpod). The app was only deployed to Heroku once all gene name search and general functions were developed. The ensembl ID search functions were added after deployment, with initial function testing still carried out in IDE terminal. 

All functions, including validation steps were tested after each deployment. Testing steps were as follows:
1. search selection
    - test if correct gene name and ID selections work
    - test if incorrect input of no input (''), word (mouse), letter (p) and wrong number (5) failed validation and gave correct value error message

2. gene name search
    - test if valid gene name (fus) produced correct gene expression output
    - test if invalid gene (moby) produced the correct 'gene not found' response
    - test if empty field produced correct error message

3. ensembl ID search
    - test if valid ID (ENSMUSG00000032047) produced correct gene expression output
    - test if ID validation worked correctly by identifying:
        - no input ('')
        - not an ID (fus)
        - not 18 characters (ENSMUSG000000320)
        - ENSMUSG start wrong (ENSMUPG00000032047)
        - last 11 characters not numbers (ENSMUSG0000003204m)
        - input begins with empty space before ID ( ENSMUSG00000032047)

4. search again/ exit
    - test if valid input starts search again or produces thank you messsage on exit correctly
    - test if incorrect input of no input (''), word (mouse), letter (p) and wrong number (5) failed validation and gave correct value error message

## Devices and Browsers

### Web browsers
Chrome (primary), Firefox , Edge 

### Devices
- Phones: Pixel4a, iPhoneXR, GalaxyS10
- Laptops: Dell Inspirion 13”, MacBookPro 13”, MacBook Air 13”, MacBook Pro 16" (new model), Microsoft Surface (v.old model)
- Desktop screens: BenQ PD series 27”

## Testing Summary
The site worked on all devices and browsers tested, but issues were found on older devices. 
The biggest issue identified was the Django authorisation forms (register in particlular) which did not always perform as intended and submit details correctly. Secondary, the interaction of classes from the Abstract template did cause fucntinal bugs at times and required significant troubleshooting to identify.

![testing-table](assets/static/testing-table.png)

### Testing conclusion
This site underperforms on older devices and browsers. The issues are primarily driven by Django third-party packages and not general page design. The masonary bricks are also laggy on old devices and an alternative may work better.

## Final Code Validation
HTML – all pages passed validation with no errors detected using the official [W3C HTML validator](https://validator.w3.org/). The summary of results can be found [here](assets/readme/html-validation.png)

CSS – all pages passed validation with no errors detected using the official [W3C CSS validator](https://jigsaw.w3.org/css-validator/). The summary of results can be found [here](assets/readme/css-valdation.png)

JavaScript - the game passed vaildation with no errors detected using [JS Hint](https://jshint.com/). The summary of results can be found [here](assets/readme/jshint_summary.png)

Accessibility – all pages showed high accessibility using Chrome [Lighthouse DevTools](https://developer.chrome.com/docs/lighthouse/). The summary of results can be found [here](assets/readme/Lighthouse-validation.png). It should be noted that there was significant impact on 'best practises' for pages displaying images from older installed version of Cloudinary as it sends immages over HTTP, not HTTPS.

PYTHON - PEP8 validation: all .py files passed validation with no errors reported from [CI pep8 python linter](https://pep8ci.herokuapp.com/). This was carried out on all admin.py, apps.py, forms.py, models.py, tests.py, urls.py,views.py and the settings.py file.


# Bugs
## Fixed


# Neutral resolution
- Registration does not always show success message and reload back to home with logged in status. However, this seemed to be an issue on the oldest devices tested only and therefore marked as compatibility issue not as specific bug on site.
  - Cloudinary serving over HTTP, not HTTPS, which gives a console warning. This requires an upgrade of Cloudinary, specifically changing the couldinary storage plugin. The cloudinary storage used was the one from the CI blog walkthrough, which does not enable HTTPS as default. This was beyond the inital scope of the project and is marked as a future feature.

## Unfixed



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

If you wish to develop this app further, feel free. To do this, create a fork of this repository and save it to your own github profile. To do this, use the fork button at the top right of this repository. This brings you to a new window, where you select yourself as the owner and can add extra details to name and description of the repo. You will then, if required, deploy to your own Heroku account using the process described above. You will also need to generate you own env.py and config var values to ensure all featuires will work. If you chose to do this, please be respectful and credit me as the origin of this project and code.

![GitHub language count](https://img.shields.io/github/languages/count/Annytomica/kumiko-community-hub)
![GitHub top language](https://img.shields.io/github/languages/top/Annytomica/kumiko-community-hub?color=yellow)
![GitHub watchers](https://img.shields.io/github/watchers/Annytomica/kumiko-community-hub)
![GitHub forks](https://img.shields.io/github/forks/Annytomica/kumiko-community-hub?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Annytomica/kumiko-community-hub?style=social)

# Credits
I would like to acknowledge and thank the following people and resources used in the creation of this site.

I would also like to note that this app was developed during a period where I was effectively homeless amd couch surfing with friends and family. I was deprived of reliable internet connections and ideal work spaces for significant periods of time. As such normal support routes of mentor meetings and tutoring, were not always available and ChatGPT was used as a replacement. While no code was directly generated by ChatGPT it does write out corrections for exisiting code, in a way that mentors and tutors do not, and I would like to acknowledge this fact.

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

- [Top Coder](https://www.topcoder.com/thrive/articles/project-management-on-github) for tutorial on how to use GitHub projects for Agile project management

### General contributions
- [Get Bootstrap](https://getbootstrap.com/docs/5.0/components/buttons/) for general bootstrap classes for styling layout and components

- [Compass](https://nimblehq.co/compass/product/backlog-management/user-stories/chores/) for how to use Chores effectively in agile project management

- [Web.dev](https://web.dev/learn/design/picture-element) for usage of picture element to improve performace of hero banner on homepage

- [Chaggy from Stack Overflow](https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms) for comment that introduced using widget to get placeholder text in crispy form input boxes


## Media
-	The icons such as like hearts and comment bubble are from [Font Awesome](https://fontawesome.com/)
- The Github summary bar used in README.md is from [shields.io](https://shields.io/badges/)

## Acknowledgements
- My wife, Megan, for help with the wireframe design, product photography, site testing and general emotional support while I was trying to study and code while also moving relentlessly.
- My mum for excellent testing assistance
- My Mentor My mentor, Oluwafemi Medale , for his invaluable guidance and feedback.
