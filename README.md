# Safety Forms
A one-stop location for safety awareness in Physical Safety, Mental Health, and Diversity. Submit feedback forms regarding safety concerns! Also see community resources page!

#
Hugely based on the concepts taught by Miguel Grinberg's Flask Mega-Tutorial! https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# Usage note

Way to add resources to Resources page not currently implemented through interface. Can manually fill out and run in flask shell:
`x = Resources(url='', desc='')`

`db.session.add(x)`

`db.session.commit()`

If you remove app.db and want to start fresh:

`flask db init`

`flask db migrate`

`flask db upgrade`

## Inspiration

* We were inspired by a single word: continuous. Demonstrated through ConocoPhillips’ SPIRIT values, we wanted to create a product that, also, consistently and continually maintained safety standards.
* We believe that building community and a sense of trust is a key aspect of creating continuity. Thus, we created our web app, with direct communication between staff and supervisors and a community resources page, to create everlasting bonds and connection.

## What it does
* Our web app hosts two main capabilities..
* First, it has a Feedback Area, where Staff Members can submit requests and concerns – namely, Physical Concerns, Mental Concerns, Hazard Report, Diversity Suggestion, Resource Submission, and Miscellaneous Concerns – directly to Administrators.
* Administrators can see these submissions directly within our app.
* The second capability our app has is a Community Resources Page. It allows for easy access to important safety content, and staff and administrators can easily add resources to this page.


## How we built it
* <b>Flask</b> for web framework. We like that it's very flexible in leaving implementation details to the developer. We're also big fans of its ecosystem of extensions.
* <b>HTML</b>, <b>CSS</b>, and <b>Flask-Bootstrap</b> for the frontend.
* <b>Flask-WTF</b>, a Flask wrapper for <b>WTForms</b>, for forms and submissions.
* <b>Flask-SQLAlchemy</b>, a Flask wrapper for <b>SQLAlchemy</b>, for the SQLite database.
* <b>Flask-Migrate</b>, a Flask wrapper for <b>Alembic</b>, a database migration framework.
* <b>Flask-Login</b>, a Flask wrapper for handling login sessions.
* <b>GitHub</b> repository to encourage community contribution towards the community-driven app!

## Challenges we ran into

* Coming from no web development experience, first up was deciding what web framework to use. Python was the only language any of us really knows. Between popular frameworks Flask and Django, we chose Flask because its flexibility and lighter weight allowed us to learn it much faster, as well as allow us to put our app together with less overhead.
* We spent a great deal of time trying to get our app running on Google Cloud Run / Firebase, but were unable to make significant progress. We decided to invest more time in ideas and planning future upgrade paths, and then making a barebones demo, to be realistic about what we could accomplish with the given time & our current levels of knowledge.
* Front-end. We struggled a lot with learning both the backend and frontend at the same time. We fortunately eventually came across Bootstrapping, a way to utilize css templates with great ease!
* Back-end. Fortunately, we came across SQLAlchemy, an Object-Relational Mapping, which allowed us to manage the database using high-level entities such as classes, objects, and methods.
* Curveballs! One of our planned members was unable to attend due to the international students rule. Another one of our members got Covid-19. Another member ended up having plans all weekend, and not being present! Fortunately, we were able to utilize online tutorials, extensive communication, planning, and work delegation to create our envisioned product (and an all-nighter).

## Accomplishments that we're proud of/what we learned

* Able to accomplish implementing a backbone for our product/website
* Successfully contributed as a team
* Building an actual, real-world product
* Following the time limit and doing a good amount of what we wanted to do
* Making the Web App Easy To Use
* Were able to get a more polished frontend than the bare basic HTML code we had for the majority of development.
* Successfully utilizing an online git repository.
* Successfully linking the frontend and backend, at a barebones level.
* Learned a lot about web development, and difficulties that can arise in working with a team (and how to deal with that)!


## What's next for Safety Forms

* Increase accessibility, extensibility, and general features
* Integrate our app to Google Cloud to support its extensibility and allow more people to take advantage of what our app features. 
* Create specific location-based subpages, so that a region office in one area doesn’t have to use the same pages as an office somewhere else. Since ConocoPhillips is an international company, we knew that this would be important. 
* Build a ticket system, so that administrators can respond to feedback forms within the app. 
* Use Google maps to create an incident map, providing an easy way for safety to be maintained.
* Create data visualization tools. These will allow for seamless, quick, and easy regulation of safety measures and protocol. Being able to see trends in the data is extremely useful for acknowledging and addressing concerns.
* Provide email notifications to administrators through our app, so administrators are notified when a request is submitted. This will decrease response times, and it will allow for responses to come to individual staff members quicker. 
* Work on the frontend development and user interface of our web app to be more appealing and dynamic.

# Flask license
BSD 3-Clause License https://github.com/pallets/flask/blob/main/LICENSE.rst
