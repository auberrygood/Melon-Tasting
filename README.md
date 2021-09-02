Melon Tasting WebApp

Service Summary:
- Melon Tasting is a service that allows users to make reservations to go to a fancy melon tasting! 
- Melon Tasting offers coverage 24/7/365 (including weekends and holidays!), but due to COVID regulations and required social distancing, only one user per reservation time is allowed.

Features:
- Users can create an account with email, username, and password.
- When logged in, users can pick a date they would like to have their reservation booked
- App will display all available appointent times for the date user selected
- Users can select preferred appointment time and book (anytimes)
- Users can view all booked reservations by that user

Behind the Scenes -- Creating Melon Tasting:
- This app had a time-limit of 6 hours to be completed. 
- I spent about 90 minutes building my database, seed file, server route skeleton, and all desired landing pages with a basic design in place (Bootstrap/CSS).
- Because this build was timed, I opted to utilize the same tech I recently used in my previous webapp since it was still fresh in my head, and I had the ability to re-use some blocks of code to save time.
- I mistakenly did not realize that a built-in date input-type existed for HTML forms, and I proceeded to spend 4 hours designing my own responsive calendar from scratch. I had a hard time getting my event hadlers to work, and while researchign solutions I discovered that HTML forms have a built-in date input-type -_- . It took me less than 2 minutes to implement the form, and have a working date-picker with accompanying responsive calendar. At this point my 6 hours was up, and I did not have enough time to handle any data passed between front-end and back-end with exception to the login feature.
- After consulting with my advisor, I deducted the time spent on the custom calendar, and gave myself 4 hours to complete rest of webapp. In exactly 6 hours I was able to complete all features mentioned above, but was unable to complete the optional time range feature, this README file, nor deploy within the allotted time frame.
- I did decide to leave the custom calendar I built within the app for display purposes (I didn't want all that work to be a complete waste), and in the future I would to make the custom calendar functional over the built-in date form.

Challenges/Unfixed Bugs:
- I had some challenges with my environment right out the gate and had issues installing psycopg2 and psycopg2-binary. I could not do this in virtualenv (error) or locally (permissions denied). I opted to build on hackbright's docker container, and had no issues, but would rather not have to do this.
- When running seed file, program is suppose to drop the melontasting database then re-create. My app would refuse to drop, causing my tables to increase with user data (I used Faker to seed users in db) with each running of the seed file. I ultimately manually dropped the tables in terinal (psql) each time I wanted to reset.
- When a user books a midnight reservation for a single date, no users are able to book a midnight reservation for any day (the blocking of the midnight availability incorrectly persists across all dates). This is not the case for any other reservation time.

Project Tech Stack:
 - Python, Javascript, HTML, Jinja, Flask, Flask_Login, PostGreSQL, SqlAlchemy, Requests, Werkzeug.Security, CSS, Bootstrap