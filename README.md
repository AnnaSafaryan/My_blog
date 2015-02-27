Study blog project for school Python/Django elective course
===========================================================

Course was read in [Liceum #40, Nizhniy Novgorod, Russia](http://www.lic40nn.edusite.ru/ "Liceum 40 website")

##A short course program description:
* Intoduction to web techlonogies (HTML, Forms, Styles)
* Django basics (templates, models, views)
* Deploying applications. Deploying to Heroku
* Authorization and security
* Caching


##How to run this blog on local machine?
* Go to repository directory 
* Install dev-dependencies:
    pip install -r requirements-dev.txt
* Run application
    python manage.py runserver --settings=settings.dev
* Blog should be available on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Note that there is default login/password pair "root//123"    