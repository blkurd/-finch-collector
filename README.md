# -finch-collector

fun lil django app all about finches


## User Stories
- As a User, when I click the View All My Finches link, I want to see a page listing all of my finches.
- AAU, when I click on a finch in the finch list, I want to see a page that displays all the details for that finch.

## ERD

![erd](https://i.imgur.com/37yYc42.png)

## Routes

route controller action 
/finches  finches index view all finches
/finches/:id show finches view one finch


### Development Steps

    1. Start by adding the url, to our urls
    2. create the view function associated with that url
    3. make the html template for that view
    4. add some functionality(UI) to quickly get to that template
