# ParkMate App

## Description

ParkMate is a web application built using Python and the Django framework for my MS3 project.

It is designed for drivers across the UK, including commuters, delivery drivers, local residents and people travelling to unfamiliar areas.

The application allows users to search parking locations stored in the ParkMate database using a town, district, postcode or parking name.

Search results are displayed using parking cards and users can also view parking locations on an interactive Leaflet map using OpenStreetMap.

Visitors can search and view parking information without creating an account.

Registered users have access to additional features including:

- saving favourite parking locations
- viewing saved parking through My ParkMate
- adding community parking locations
- editing their own parking submissions
- deleting their own parking submissions

ParkMate also separates **Council/NPP price verified** parking from **Mapped parking** so users can understand whether parking information has an official source.

## Purpose

The purpose of ParkMate is to make finding parking easier and clearer for UK drivers.

Parking information can be spread across council websites, parking provider websites and mapping services.

This can make it difficult for drivers to quickly find out:

- where a parking location is
- what it is called
- how much it costs
- how many spaces it has
- what restrictions apply
- when charges apply
- how payment works

ParkMate brings useful parking information together in one web application.

A driver can enter information they already know, such as a postcode, town or parking name, and view matching parking locations stored in the database.

Another purpose of ParkMate is to make the source of parking information clear.

Parking records that contain a suitable official council, GOV.UK or National Parking Platform source can be shown as:

**Council/NPP price verified**

Other records are shown as:

**Mapped parking**

This prevents unverified parking information from being presented as officially verified.

User accounts also have a clear purpose.

Registered users can save parking locations and contribute their own parking locations to ParkMate.

## Technologies Used

| Technology            | Use in ParkMate                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------- |
| Python 3.13.15        | Runs the backend Python code                                                              |
| Django 5.2.17         | Provides routing, templates, authentication, forms, validation and database functionality |
| HTML                  | Structures the website pages                                                              |
| CSS                   | Controls the appearance and responsive layouts                                            |
| JavaScript            | Controls interactive map behaviour and parking image loading                              |
| SQLite                | Used as the local development database                                                    |
| PostgreSQL            | Supported as the production database                                                      |
| Django ORM            | Handles database queries and relationships                                                |
| Leaflet               | Displays the interactive parking map                                                      |
| OpenStreetMap         | Provides the map tiles                                                                    |
| Wikimedia Commons API | Attempts to find relevant parking and location images                                     |
| WhiteNoise            | Serves static files in production                                                         |
| Gunicorn              | Runs the Django application in production                                                 |
| dj-database-url       | Reads the production database connection                                                  |
| Heroku                | Used as the intended deployment platform                                                  |
| Git                   | Tracks changes made during development                                                    |
| GitHub                | Stores the project repository and commit history                                          |

# Deployment

## Live Site

The deployed version of ParkMate can be viewed here:

[View the live ParkMate application](https://parkmate-4d1d2b372f8e.herokuapp.com/)

ParkMate was deployed using **Heroku** so that the final Django application could be accessed online.

ParkMate was deployed using **Heroku** so that the final Django application could be accessed online.

## Heroku Deployment

The following steps were used to deploy the project:

1. Create a new application on [Heroku](https://www.heroku.com/).

2. Connect the Heroku application to the GitHub repository containing the ParkMate project.

3. Add a PostgreSQL database for the deployed application. Heroku provides the database connection through the `DATABASE_URL` environment variable.

4. In **Heroku → Settings → Config Vars**, add the required environment variables for the project. Sensitive information, such as the Django secret key and database credentials, should be stored as environment variables rather than committed to GitHub.

5. Ensure that all required Python packages are included in the `requirements.txt` file.

6. ParkMate uses a `Procfile` in the root directory of the project to tell Heroku how to run the Django application:

    ```text
    web: gunicorn parkmate.wsgi:application
    ```

7. The Django settings are configured to use the Heroku `DATABASE_URL` when the application is running in the deployed environment.

8. WhiteNoise is used to manage and serve static files in the deployed application.

9. Push the latest version of the project to GitHub.

10. From Heroku, deploy the application using the connected GitHub repository.

11. After deployment, run the Django migrations so that the production database contains the required database tables:

    ```bash
    python manage.py migrate
    ```

12. Open the deployed application and test the live version to ensure that it works correctly and matches the development version.

The deployed application was checked to ensure that navigation, authentication, parking searches, database functionality, forms, static files and the interactive map worked correctly.

## Updating the Deployment

When changes are made to ParkMate, the changes are committed and pushed to GitHub. The latest version can then be deployed through Heroku so that the live application contains the most recent updates.


# User Experience Design (UX)

## User Studies - Planning

User studies are used to understand whether users can complete the main ParkMate tasks without needing extra instructions.

The main tasks include:

1. Search using a UK town.
2. Search using a postcode.
3. Search using a postcode district.
4. Search using a parking name.
5. View parking results.
6. Open a parking detail page.
7. View parking on the map.
8. Identify a Council/NPP price verified parking location.
9. Identify a mapped parking location.
10. Register for an account.
11. Log in.
12. Log out.
13. Save a favourite parking location.
14. Remove a favourite.
15. Open My ParkMate.
16. Add a community parking location.
17. Edit their own parking submission.
18. Delete their own parking submission.

Feedback from these tasks is used to improve:

- navigation
- search
- forms
- buttons
- parking cards
- map usability
- responsive layouts

# Target Users

ParkMate mainly targets three groups of UK drivers:

1. Commuters
2. Drivers Attending Appointments or Events
3. Delivery Drivers

## 1. Commuters

Commuters regularly travel to work, train stations, town centres or other places of employment.

They may use ParkMate regularly and benefit from being able to save useful parking locations.

### First-Time Users

- As a first-time commuter, I want to search using a town or city so I can find parking close to where I work.
- As a first-time commuter, I want to search using a postcode so I can find parking without knowing the parking location name.
- As a first-time commuter, I want to compare parking prices so I can find a suitable option.
- As a first-time commuter, I want to view parking on a map so I can see where it is located.

### Returning Users

- As a returning commuter, I want to register for an account so I can use the personal features.
- As a returning commuter, I want to log in so I can access My ParkMate.
- As a returning commuter, I want to save useful parking locations so I can find them again.
- As a returning commuter, I want to view my favourites so I do not have to search for the same parking every time.

### Frequent Users

- As a frequent commuter, I want to quickly return to my saved parking locations.
- As a frequent commuter, I want to add a useful parking location that is missing from ParkMate.
- As a frequent commuter, I want to edit a parking location I submitted if the information needs correcting.
- As a frequent commuter, I want to delete one of my own parking submissions if it is no longer needed.

## 2. Drivers Attending Appointments or Events

These users may be travelling to an unfamiliar hospital, medical centre, event venue or town centre.

They may mainly use ParkMate when travelling somewhere they do not normally visit.

### First-Time Users

- As a first-time visitor, I want to search using the postcode of my destination so I can find nearby parking.
- As a first-time visitor, I want to view parking locations on the map so I can understand where they are.
- As a first-time visitor, I want to check parking restrictions so I know important conditions before travelling.
- As a first-time visitor, I want to see whether parking information is Council/NPP price verified so I understand where the information comes from.

### Returning Users

- As a returning visitor, I want to check parking details again before starting my journey.
- As a returning visitor, I want to check charging times so I know when parking charges apply.
- As a returning visitor, I want to check payment information so I know how the parking location accepts payment.
- As a returning visitor, I want to save a suitable parking location so I can easily find it again.

### Frequent Users

- As a frequent visitor, I want to compare different parking locations before choosing one.
- As a frequent visitor, I want to access previously saved parking from My ParkMate.
- As a frequent visitor, I want to follow an official source when one is available so I can check the original parking information.
- As a frequent visitor, I want to contribute a useful parking location if I find one that is missing from ParkMate.

## 3. Delivery Drivers

Delivery drivers regularly travel to different towns, streets and postcodes.

They may need to find parking information quickly while travelling between different areas.

### First-Time Users

- As a first-time delivery driver, I want to search using a postcode so I can quickly find parking near a delivery address.
- As a first-time delivery driver, I want to search using a town so I can see parking options in an unfamiliar area.
- As a first-time delivery driver, I want to view several parking results so I can choose a suitable location.
- As a first-time delivery driver, I want to open a parking detail page so I can check the address and restrictions.

### Returning Users

- As a returning delivery driver, I want to use the map so I can see where stored parking locations are positioned.
- As a returning delivery driver, I want to search directly for parking locations I have previously used.
- As a returning delivery driver, I want to save useful parking locations so they are easier to find later.
- As a returning delivery driver, I want to view saved locations from My ParkMate so I can access them quickly.

### Frequent Users

- As a frequent delivery driver, I want to add useful parking locations that may help other drivers.
- As a frequent delivery driver, I want to edit parking locations I personally submitted when information changes.
- As a frequent delivery driver, I want to delete one of my own parking submissions when it is no longer useful.
- As a frequent delivery driver, I want to compare verified and mapped parking records so I can understand which information has an official source.

# Research

Research is used to make sure ParkMate solves a realistic problem rather than me guessing what users may need.

Drivers may search for parking using different information.

One user may know a postcode while another user may only know:

- a town
- a district
- an address
- a parking name

Because of this, ParkMate searches different database fields including:

- parking name
- address
- postcode
- postcode area
- local authority

Official council parking information commonly contains information such as:

- prices
- spaces
- charging times
- restrictions

These types of information are stored in ParkMate where they are available.

The map is also important because location information can be easier to understand visually.

ParkMate uses Leaflet and OpenStreetMap to display parking locations stored in the database.

## Research Findings and Features

| Research Finding                                                | Evidence Source                           | ParkMate Response                                                                                               |
| --------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Drivers may search using a location, postcode or parking name.  | Medway Council Car Park Directory         | ParkMate supports location, postcode and parking-name searching.                                                |
| Official parking pages provide prices and charging information. | Lewisham Council Car Parks                | ParkMate stores tariff information, charging times and official source details.                                 |
| Parking restrictions depend on signs and operating conditions.  | GOV.UK Highway Code - Waiting and Parking | Parking detail pages contain restriction information and users are reminded that mapped information can change. |
| Drivers benefit from having parking information in one place.   | GOV.UK Plan for Drivers                   | ParkMate brings different parking information together in one application.                                      |
| Interactive maps help users understand where a location is.     | Leaflet Documentation                     | ParkMate uses a Leaflet map with OpenStreetMap tiles.                                                           |

## Competitor Research

I look at other parking and mapping services to understand what users already expect from this type of website.

The main examples include:

- Parkopedia
- JustPark
- RingGo
- council parking websites
- OpenStreetMap

## Parkopedia

Parkopedia allows users to search for parking and compare information about different locations.

Useful ideas include:

- location searching
- clear parking information
- parking maps
- simple comparison of parking locations

## JustPark

JustPark focuses on finding and booking parking.

Useful design ideas include:

- clear search
- location-based results
- simple parking cards
- easy-to-understand parking information

ParkMate does not include parking booking because this is outside the scope of the project.

## RingGo

RingGo focuses more on parking payments and parking sessions.

It shows that drivers value:

- clear location information
- parking prices
- simple mobile interfaces

ParkMate does not process parking payments.

## Council Parking Websites

Council parking websites are important because they can provide official information including:

- car park names
- tariffs
- charging hours
- parking spaces
- restrictions

Official council information is useful when deciding whether a ParkMate record can be shown as Council/NPP price verified.

## OpenStreetMap

OpenStreetMap provides geographic map information.

ParkMate uses OpenStreetMap tiles through Leaflet to create the interactive parking map.

## Competitor Research Conclusion

The competitor research shows that the most useful features for ParkMate are:

- search
- map
- price information
- parking details
- clear parking cards

ParkMate remains smaller than large commercial parking services.

Features such as:

- booking
- payment
- guaranteed live parking availability

are not included in the current project.

# Strategy

The Strategy plane defines what ParkMate is trying to achieve, who the website is for and what problems it needs to solve.

## Target Audience

The target audience is UK drivers including:

- commuters
- delivery drivers
- local residents
- drivers attending appointments
- drivers attending events
- people travelling to unfamiliar locations

Visitors can use the main parking search without creating an account.

Accounts are mainly used for additional personal features.

## Content

The main parking content includes:

- parking name
- address
- postcode
- local authority
- price
- parking spaces
- disabled spaces
- charging times
- restrictions
- operator
- payment information
- verification
- official source
- parking image
- map location

Account content includes:

- registration
- login
- logout
- favourites
- My ParkMate
- personal parking submissions

## Problems and Solutions

| Problem                                                        | ParkMate Solution                                    |
| -------------------------------------------------------------- | ---------------------------------------------------- |
| Parking information can be spread across several websites.     | ParkMate brings useful parking information together. |
| A user may only know a postcode.                               | ParkMate supports postcode searching.                |
| A user may only know the town or area.                         | ParkMate searches location-related database fields.  |
| Users may not know where parking is.                           | Parking locations are displayed on a map.            |
| Users may not know whether information has an official source. | ParkMate shows verification labels.                  |
| Users may want to remember a useful location.                  | Registered users can save favourites.                |
| Useful parking may be missing.                                 | Registered users can add community parking.          |
| Users should not change another person's parking record.       | Ownership checks restrict editing and deleting.      |
| A parking image may fail to load.                              | ParkMate uses a local fallback image.                |

## Business Goals

The main goals of ParkMate are to:

- solve a realistic parking problem
- create a full-stack Django project
- demonstrate Python
- demonstrate relational database functionality
- demonstrate CRUD
- use authentication
- provide responsive design
- provide interactive map functionality
- provide useful search functionality
- make parking information easier to understand
- create a project that is realistic for MS3

## User Needs

Users need to:

- search quickly
- search without registering
- search using different information
- compare parking
- view parking details
- view parking on a map
- understand parking verification
- use the website on different devices
- save favourite parking
- add community parking
- manage their own submissions

# Scope

The Scope plane defines the features that are included in ParkMate.

I keep the scope focused on the main parking problem instead of adding features that are not needed for the project.

## Minimum Viable Product (MVP)

The MVP contains:

- parking search
- postcode search
- parking result cards
- parking detail pages
- Leaflet map
- OpenStreetMap
- parking prices
- parking restrictions
- verification status
- registration
- login
- logout
- My ParkMate
- favourites
- community parking
- CRUD
- responsive design

## Features

### Parking Search

Users can search using:

- parking name
- address
- postcode
- postcode district or area
- local authority

### Parking Results

Results can display:

- parking name
- address
- postcode
- price
- spaces
- local authority
- verification
- image
- detail-page link

### Parking Details

Parking details can display:

- name
- address
- postcode
- tariff information
- total spaces
- charging times
- operator
- restrictions
- payment information
- official source
- parking image

### Interactive Map

The map uses:

- Leaflet
- OpenStreetMap
- parking coordinates stored in the database

Map markers are created from parking records stored in ParkMate.

### Parking Images

Parking images can come from:

1. a stored parking image URL
2. Wikimedia Commons
3. a local fallback image

### Accounts

Accounts include:

- registration
- login
- logout
- authenticated pages

### My ParkMate

My ParkMate gives registered users access to:

- favourite parking
- their own parking submissions

### Favourites

Registered users can:

- save a parking location
- remove a favourite
- view saved parking

### Community Parking

Registered users can add community parking locations.

Community parking is not automatically marked as Council/NPP price verified.

## CRUD Functionality

ParkMate demonstrates all four CRUD operations.

| CRUD Operation | ParkMate Function                                            |
| -------------- | ------------------------------------------------------------ |
| **Create**     | A registered user adds a parking location.                   |
| **Read**       | Users search and view parking locations.                     |
| **Update**     | A user edits a parking location they personally submitted.   |
| **Delete**     | A user deletes a parking location they personally submitted. |

Ownership checks stop normal users from editing or deleting parking records submitted by somebody else.

## Functional Requirements

ParkMate needs to:

- accept parking searches
- search several database fields
- return matching results
- display parking cards
- display parking detail pages
- display parking locations on the map
- allow registration
- allow login
- allow logout
- protect account-only pages
- save favourites
- remove favourites
- display favourites
- allow parking locations to be added
- allow owners to edit parking
- allow owners to delete parking
- validate parking forms
- display verification information
- display a fallback image when required

## Non-Functional Requirements

ParkMate also needs to:

- work on mobile
- work on tablet
- work on desktop
- be easy to navigate
- use readable text
- have consistent buttons
- have consistent parking cards
- use secure authentication
- protect forms
- validate user input
- stop unauthorised editing
- use suitable colour contrast
- load static files correctly
- work when deployed

## Further Developments

Possible future improvements include:

- adding more parking records
- adding more Council/NPP verified records
- improving parking image matching
- adding more search filters
- increasing automated test coverage
- completing the availability-reporting workflow

Features that are outside the current project scope include:

- parking booking
- parking payments
- guaranteed live parking-space information

# Python and Django Files

ParkMate will use several Python and Django files because Django will separate different parts of the application into different files.

Each file will have its own purpose, which will make the project easier to organise, understand and maintain.

Instead of placing all backend logic in one Python file, ParkMate will separate:

- project settings
- URL routing
- database models
- backend logic
- forms
- validation
- tests
- deployment configuration
- database migrations
- custom management commands

## Python and Django File Functions

| File                               | Function in ParkMate                                                                                                                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `manage.py`                        | This file will be used to run Django commands from the terminal. It will allow me to start the development server, apply migrations, run tests and use custom management commands.                 |
| `parkmate/settings.py`             | This file will contain the main Django settings. It will control the installed apps, database, static files, security settings, allowed hosts and deployment configuration.                        |
| `parkmate/urls.py`                 | This file will contain the main project URL configuration and will connect the project to the parking app URLs and Django authentication URLs.                                                     |
| `parking/urls.py`                  | This file will contain the ParkMate page routes. It will connect URLs such as Home, Parking, Map, My ParkMate, Add, Edit and Delete to the correct views.                                          |
| `parking/models.py`                | This file will define the database models used by ParkMate. It will contain the structure for parking locations, favourites and availability reports.                                              |
| `parking/views.py`                 | This file will contain most of the backend logic. It will process searches, retrieve parking data, display pages, handle favourites, manage user parking submissions and enforce ownership checks. |
| `parking/forms.py`                 | This file will define Django forms. It will collect and validate user input when parking records are created or edited.                                                                            |
| `parking/admin.py`                 | This file will register the database models with Django Admin so authorised staff can manage stored records.                                                                                       |
| `parking/apps.py`                  | This file will contain the configuration for the parking Django application.                                                                                                                       |
| `parking/tests.py`                 | This file will contain automated tests for important ParkMate functionality.                                                                                                                       |
| `parking/error_handlers.py`        | This file will contain custom error-handling functions used when ParkMate displays error pages.                                                                                                    |
| `parkmate/wsgi.py`                 | This file will provide the WSGI entry point used by Gunicorn when ParkMate is deployed.                                                                                                            |
| `parkmate/asgi.py`                 | This file will provide Django's ASGI application configuration.                                                                                                                                    |
| `__init__.py`                      | These files will allow Python to recognise the folders as Python packages.                                                                                                                         |
| `parking/migrations/*.py`          | These files will record changes to the database structure when models or fields are changed.                                                                                                       |
| `parking/management/commands/*.py` | These files will contain custom Django terminal commands such as the command used to seed parking records.                                                                                         |

## Main Files I Will Work With

### `models.py`

`models.py` will define the structure of the database.

It will contain models including:

- `ParkingLocation`
- `Favourite`
- `AvailabilityReport`

The models will define what information is stored and how database records are connected.

### `views.py`

`views.py` will contain much of the main application logic.

It will be responsible for:

- processing parking searches
- handling postcode-area searches
- retrieving parking records
- displaying parking results
- displaying parking details
- displaying the map
- handling favourites
- handling My ParkMate
- creating parking records
- editing parking records
- deleting parking records
- checking whether the signed-in user owns a submission

### `forms.py`

`forms.py` will control the forms used by ParkMate.

It will be used for:

- adding parking
- editing parking
- validating submitted information
- preventing invalid data from being saved

### `urls.py`

The URL files will decide which view opens when a user visits a particular address.

They will connect routes for:

- home
- parking list
- parking details
- parking map
- My ParkMate
- registration
- adding parking
- editing parking
- deleting parking
- favourites

### `tests.py`

`tests.py` will contain automated tests.

The tests will help check:

- parking search
- authentication
- favourites
- Create functionality
- Read functionality
- Update functionality
- Delete functionality
- ownership protection

## Django Generated Files

Some Python files will be created automatically when the Django project or application is created.

These include:

- `apps.py`
- `asgi.py`
- `wsgi.py`
- `__init__.py`

Migration files will also be generated by Django when the database structure changes.

These files will still be important to ParkMate even though much of their starting content will be generated automatically.

## Why ParkMate Will Use Several Python Files

ParkMate will use more Python files than a small standalone Python program because Django will follow a structured project layout.

Separating the code will make it easier to understand where different functionality belongs.

For example:

- database code will go in `models.py`
- page and backend logic will go in `views.py`
- form logic will go in `forms.py`
- routes will go in `urls.py`
- automated tests will go in `tests.py`
- configuration will go in `settings.py`

This structure will make ParkMate easier to manage as the project develops.

# Structure

The Structure plane defines how the different pages and features connect together.

## Information Architecture

```text
ParkMate
│
├── Home
│   └── Main Search
│
├── Parking
│   ├── Search Results
│   └── Parking Detail
│
├── Map
│   ├── Map Search
│   └── Parking Markers
│
├── Account
│   ├── Register
│   ├── Login
│   └── Logout
│
└── My ParkMate
    ├── Favourites
    └── My Parking
        ├── Add
        ├── Edit
        └── Delete
```

## Logical Organisation

The main feature is parking search, so it is kept easy to reach.

The normal user journey is:

1. Search
2. View results
3. Select parking
4. View details

The map provides another way to view stored parking locations.

Account features are kept separate because visitors do not need an account to search for parking.

## User Flow

### Visitor Flow

```text
Home
 ↓
Search
 ↓
Parking Results
 ↓
Parking Detail
```

### Map Flow

```text
Map
 ↓
Search / View Markers
 ↓
Select Parking
 ↓
View Parking Information
```

### Account Flow

```text
Register
 ↓
Login
 ↓
My ParkMate
```

### Favourite Flow

```text
Parking
 ↓
Save Favourite
 ↓
My ParkMate
 ↓
Saved Parking
```

### CRUD Flow

```text
Login
 ↓
My ParkMate
 ↓
My Parking
 ↓
Add / Edit / Delete
```

# Skeleton

ParkMate follows a mobile-first approach.

## Mobile Wireframes

![mobile-wireframes](assets/wireframes/mobile-vw.jpeg)

## Tablet Wireframes

![tablet-wireframes](assets/wireframes/tablet-vw.jpeg)

## Desktop Wireframes

![desktop-wireframes](assets/wireframes/desktop-vw.jpeg)

## Design Decisions

The main design decisions are:

- search is kept easy to find
- parking cards use a consistent layout
- navigation stays consistent
- verified, mapped and community parking are visually separated
- forms are kept simple
- buttons are easy to recognise
- delete actions are clearly separated from normal actions
- users do not need an account to search
- map controls remain familiar
- layouts work across different screen sizes

# Surface

## Colour

### How I Choose the Colours

I first thought about what suits a parking and navigation website and then looked at existing design guidance to see how colours are used for different types of information.

I looked at the GOV.UK Design System because it is designed for clear public-facing digital services. One thing I noticed is that colours are given clear purposes. Green is used for positive or success information, red is used for errors and dark text is used against light backgrounds to keep information easy to read.

For ParkMate itself, I choose navy as the main navigation colour because I want the website to have a professional and trustworthy appearance. I use green for the main actions because it stands out clearly against the navy and white backgrounds. I use white and light grey for the main content because I want parking cards and information to remain easy to scan.

I then use blue for mapped parking because it makes it clearly different from verified parking. Red is kept for errors and delete actions so it is not confused with normal actions.

The exact colour shades are my own ParkMate colour choices. The external research mainly helps me decide how the colours are used.

### Colour Research Evidence

| Evidence Source                                     | What I Find                                                                                                             | How I Use It in ParkMate                                                                                       |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| GOV.UK Design System - Colour                       | Colours are given specific purposes and the guidance includes success, error, text, background and interactive colours. | This supports my use of green for positive/verified information and red for destructive or error information.  |
| GOV.UK Design System - Colour Contrast              | Text and interactive elements need enough contrast against their backgrounds.                                           | I will use dark text on white/light backgrounds and white text on the dark navy navigation.                    |
| Department for Education Design System - Typography | The DfE uses Inter for digital services and describes it as suitable for readable digital interfaces.                   | This supports my choice of Inter as the preferred ParkMate typeface.                                           |
| GOV.UK Design System - Type Scale                   | Typography changes depending on screen size and uses a clear hierarchy.                                                 | ParkMate will use a responsive font sizes and different sizes for headings, supporting information and labels. |

### Main ParkMate Colour Palette

These are the main colour variables that will be used in my ParkMate CSS:

| CSS Variable    | Colour    | Use                                       |
| --------------- | --------- | ----------------------------------------- |
| `--navy`        | `#072742` | Main navigation and dark branded areas    |
| `--navy-2`      | `#0B3557` | Secondary navy shade                      |
| `--green`       | `#13A957` | Main buttons and primary actions          |
| `--green-dark`  | `#0C8543` | Hover states and smaller green highlights |
| `--green-soft`  | `#E8F7EE` | Soft green status backgrounds             |
| `--ink`         | `#0E2235` | Main text                                 |
| `--muted`       | `#63717F` | Secondary text                            |
| `--line`        | `#DFE6EB` | Borders and dividers                      |
| `--page`        | `#F7F9FA` | Main page background                      |
| `--card`        | `#FFFFFF` | Cards and content panels                  |
| `--danger`      | `#DE342D` | Delete and destructive actions            |
| `--danger-soft` | `#FFE9E7` | Error and delete-warning backgrounds      |
| `--info-soft`   | `#E9F4FF` | Informational message backgrounds         |

### Navigation Colours

The navigation uses:

```css
background: linear-gradient(100deg, #072742, #082c4a);
```

I use a darker navigation because it clearly separates the header from the lighter page content.

The normal navigation text uses:

```text
#FFFFFF
```

The **Mate** part of the ParkMate brand uses:

```text
#37D77A
```

The navigation hover colour is:

```text
#70E8A0
```

I use the brighter green on the ParkMate name and hover states because it gives the website a small branded highlight without making the whole header too bright.

### Button Colours

The main buttons use a green gradient:

```css
linear-gradient(#19B85F, #0D9B4D)
```

The main green CSS variable is:

```text
#13A957
```

The darker hover colour is:

```text
#0C8543
```

I use green for the main actions because I want actions such as searching, viewing details and submitting forms to stand out from the normal page content.

### Verified Parking Colours

Council/NPP price verified information uses a soft green background:

```text
#E8F7EE
```

with darker green text:

```text
#08753A
```

The verified map marker also uses:

```text
#19B77D
```

with a darker border:

```text
#075B3E
```

I use green because I want verified information to be easy to identify as a positive status.

The written verification label is still shown so the user does not need to rely only on colour.

### Mapped Parking Colours

Mapped parking uses:

```text
#E8F3FF
```

for the light background and:

```text
#174F91
```

for the text.

Mapped map markers use:

```text
#5AA6EF
```

with:

```text
#174F91
```

as the darker border.

Some mapped parking sections also use:

```text
#397FC1
```

as the blue accent.

I use blue because it is clearly different from the green used for verified parking.

### Community Parking Colours

Community-submitted parking uses amber colours including:

```text
#D99A32
```

for the accent and:

```text
#FFF8EC
```

for a light background.

Darker community text uses:

```text
#6D4200
```

I use amber because community submissions need to look different from both verified and mapped parking.

### Availability Status Colours

The project also contains styles for availability statuses.

Available:

```text
Background: #E5F7EC
Text: #08753A
```

Busy:

```text
Background: #FFF4D6
Text: #7E5C00
```

Full:

```text
Background: #FFE6E4
Text: #A62720
```

Neutral:

```text
Background: #EDF2F5
Text: #506473
```

These status colours are designed to make different states visually clear.

### Colour Scheme

The final ParkMate design will mainly use navy, green, white and light grey.

I will use navy for the navigation because it gives the website a strong and professional appearance.

Green is used for main actions and verified information because it stands out clearly from the navy and light backgrounds.

White and light grey are used for most of the content because I want parking cards and information to be easy to read.

Blue is used for mapped parking and amber is used for community parking so these types of records remain visually different.

Red is mainly kept for errors and destructive actions.

## Typography

### Research

For typography, I want ParkMate to be easy to read rather than using decorative fonts.

I look at the Department for Education Design System as an example of a public digital service that uses Inter. It uses Inter for digital products because it works well for readable interfaces across different screen sizes.

I also look at the GOV.UK type scale. It uses a clear hierarchy between headings and normal text and changes sizes depending on the screen width.

This influences my decision to use a simple sans-serif font stack and responsive heading sizes.

### Typography Research Evidence

| Evidence Source                                     | What I Find                                                     | How I Use It in ParkMate                                              |
| --------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------- |
| Department for Education Design System - Typography | Inter is used as a digital typeface for DfE services.           | I set Inter as the first font in my ParkMate font stack.              |
| GOV.UK Design System - Type Scale                   | Different sizes and line heights create a clear text hierarchy. | ParkMate uses larger headings and smaller supporting information.     |
| GOV.UK Design System - Responsive Type Scale        | Font sizes change depending on screen size.                     | ParkMate uses `clamp()` for important headings.                       |
| W3C Accessibility Guidance                          | Text needs to remain readable and understandable.               | I keep the typography simple and avoid using lots of different fonts. |

### Typography chosen

The main typography used in ParkMate is:

```css
font-family:
  Inter,
  ui-sans-serif,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  sans-serif;
```

I choose a sans-serif font style because ParkMate is mainly an information and search website.

I want users to be able to quickly scan parking names, prices, addresses and restrictions without decorative text getting in the way.

`Inter` is set as my preferred font.

The CSS also contains system font fallbacks:

- `ui-sans-serif`
- `-apple-system`
- `BlinkMacSystemFont`
- `"Segoe UI"`
- `sans-serif`

This means if Inter is not available on the device, the browser can use the next suitable system font.

### ParkMate Brand

The ParkMate brand uses:

```css
font-size: 1.35rem;
font-weight: 800;
letter-spacing: -0.03em;
```

I use a heavier weight for the ParkMate name because I want it to stand out from the navigation links.

### Main Home Heading

The main heading uses:

```css
font-size: clamp(3rem, 6vw, 5.2rem);
line-height: 0.98;
letter-spacing: -0.055em;
```

I use a large heading because it is the first text I want users to notice.

I use `clamp()` so the size can change depending on the screen width.

### Supporting Home Text

The supporting paragraph uses:

```css
font-size: 1.08rem;
```

This keeps it smaller than the main heading while still making the description easy to read.

### Navigation

Navigation links use:

```css
font-size: 0.9rem;
font-weight: 600;
```

I keep the navigation clear without making it compete with the main page headings.

### Parking Result Names

Parking result names use:

```css
font-size: 1.12rem;
```

The parking name is made larger than secondary information because this is one of the first things the user needs to identify.

### Supporting Parking Information

Smaller parking information uses font sizes such as:

```css
font-size: 0.82rem;
```

and:

```css
font-size: 0.84rem;
```

This is used for information that is useful but not as important as the parking name.

### Parking Detail Heading

The detail heading uses:

```css
font-size: clamp(2rem, 4vw, 3.1rem);
letter-spacing: -0.035em;
```

This makes the selected parking location clear while still allowing the heading to resize.

### Labels

Small labels use:

```css
font-size: 0.75rem;
font-weight: 800;
text-transform: uppercase;
letter-spacing: 0.08em;
```

I use uppercase labels and a heavier weight to separate small status information from normal paragraph text.

### Buttons

Buttons use:

```css
font-weight: 750;
```

I use a heavier button weight because important actions need to look clickable and stand out from normal text.

## Images and Visuals

Visuals include:

- parking images
- OpenStreetMap
- Leaflet map markers
- parking cards
- status badges
- interface icons
- ParkMate hero artwork

Parking images can use:

- stored image URLs
- Wikimedia Commons
- local fallback images

## Animations and Effects

Effects are kept simple.

They include:

- navigation hover colours
- button hover states
- form focus states
- card shadows
- smooth scrolling

Large animations are avoided because the main purpose of ParkMate is to find information quickly.

## Accessibility Planning

Accessibility planning includes:

- readable text sizes
- clear colour contrast
- visible form labels
- meaningful button text
- keyboard-accessible controls
- responsive layouts
- form validation feedback
- suitable alternative text
- not relying only on colour

I also use written labels alongside status colours.

For example:

- **Council/NPP price verified**
- **Mapped parking**

During accessibility testing I check the colour combinations and adjust any areas that do not meet the required contrast standard.

# Database Design

ParkMate uses Django ORM with a relational database.

SQLite is used during local development.

PostgreSQL is supported for the production version.

## Database Overview

The main database models are:

- `ParkingLocation`
- `Favourite`
- `AvailabilityReport`
- Django `User`

The main data in the application is based around parking locations.

Users are connected to parking locations through:

- parking submissions
- favourites

## Entity Relationship Diagram (ERD)

```text
┌──────────────────────┐
│     Django User      │
└──────────┬───────────┘
           │
           │ submits
           ▼
┌──────────────────────────┐
│     ParkingLocation      │
├──────────────────────────┤
│ name                     │
│ address                  │
│ postcode                 │
│ nation                   │
│ local_authority          │
│ latitude                 │
│ longitude                │
│ parking_type             │
│ operator_name            │
│ spaces_total             │
│ disabled_spaces          │
│ tariff_info              │
│ charging_times           │
│ restrictions             │
│ payment_info             │
│ source information       │
│ verification             │
│ image information        │
│ submitted_by             │
│ timestamps               │
└────────────┬─────────────┘
             │
             │ saved through
             ▼
      ┌───────────────┐
      │   Favourite   │
      ├───────────────┤
      │ user          │
      │ parking       │
      │ created_at    │
      └───────┬───────┘
              │
              ▼
        Django User
```

## Database Models

### ParkingLocation

`ParkingLocation` is the main database model.

It stores information including:

- name
- address
- postcode
- nation
- local authority
- latitude
- longitude
- parking type
- operator
- total spaces
- disabled spaces
- tariff information
- charging times
- restrictions
- payment information
- payment location code
- official source name
- official source URL
- verification status
- last checked date
- image URL
- image source
- image credit
- submitting user
- active status
- timestamps

### Favourite

The `Favourite` model connects a registered user with a parking location they save.

A database constraint prevents the same user from saving the same parking location more than once.

### Django User

Django's built-in User model handles:

- user accounts
- usernames
- passwords
- authentication

The user is connected to:

- favourite parking locations
- parking locations they submit

### AvailabilityReport

The project contains an `AvailabilityReport` model.

It stores:

- parking location
- user
- status
- spaces available
- note
- date and time

The current URL configuration does not contain a completed user-facing availability-report submission route.

Because of this, availability reporting is not treated as one of the completed MVP user features.

## Database Relationships

### User to ParkingLocation

One user can submit multiple parking locations.

Each submitted parking record can store the user who created it.

### User to Favourite

One user can have multiple favourite records.

### ParkingLocation to Favourite

One parking location can be saved by multiple users.

### User to AvailabilityReport

One user can be linked to multiple availability reports in the database model.

### ParkingLocation to AvailabilityReport

One parking location can contain multiple availability reports.

## Database Fields and Data Types

| Field                   | Django Type              |
| ----------------------- | ------------------------ |
| `name`                  | `CharField`              |
| `address`               | `CharField`              |
| `postcode`              | `CharField`              |
| `nation`                | `CharField` with choices |
| `local_authority`       | `CharField`              |
| `latitude`              | `DecimalField`           |
| `longitude`             | `DecimalField`           |
| `parking_type`          | `CharField` with choices |
| `operator_name`         | `CharField`              |
| `spaces_total`          | `PositiveIntegerField`   |
| `disabled_spaces`       | `PositiveIntegerField`   |
| `tariff_info`           | `TextField`              |
| `charging_times`        | `CharField`              |
| `restrictions`          | `TextField`              |
| `payment_info`          | `CharField`              |
| `payment_location_code` | `CharField`              |
| `source_name`           | `CharField`              |
| `source_url`            | `URLField`               |
| `council_verified`      | `BooleanField`           |
| `last_checked`          | `DateTimeField`          |
| `image_url`             | `URLField`               |
| `image_source_url`      | `URLField`               |
| `image_credit`          | `CharField`              |
| `submitted_by`          | `ForeignKey`             |
| `is_active`             | `BooleanField`           |
| `created_at`            | `DateTimeField`          |
| `updated_at`            | `DateTimeField`          |

# Validation and Security Planning

Validation will be used to reduce incorrect parking information being added to the database.

Validation includes:

- UK latitude range checks
- UK longitude range checks
- disabled-space validation
- official source URL validation
- verified-record requirements
- Django form validation
- authentication checks
- ownership checks

Verified parking records require:

- an official source URL
- a last checked date
- tariff information

Security includes:

- Django CSRF protection
- password validation
- authenticated routes
- ownership protection
- secure production cookies
- HTTPS redirect
- HSTS
- content type protection

Normal registered users cannot edit or delete another user's parking submission.

# Responsive Design Planning

ParkMate will follow a mobile-first approach.

The design supports:

- mobile phones
- tablets
- desktop computers

The following remain consistent across different screen sizes:

- navigation
- forms
- parking cards
- buttons
- spacing
- typography
- verification badges

The layout changes depending on the available screen width while the main functionality stays the same.

# Data and Map Planning

ParkMate will use parking records stored in its database.

The parking map will use:

- Leaflet
- OpenStreetMap

Each map marker will use coordinates stored with a parking record.

ParkMate does not depend on a live parking API to create its stored parking markers.


# Image Planning

ParkMate will use parking images to help users recognise locations.

The image system will use:

1. a stored image URL where available
2. Wikimedia Commons
3. a local fallback parking image

The fallback image prevents broken images from being displayed.

# Verification Planning

ParkMate separates parking records into:

- **Council/NPP price verified**
- **Mapped parking**
- community-submitted parking

Parking should only be shown as officially price verified when suitable official source information is stored.

Verified records require:

- an official council/GOV.UK or NPP source
- official tariff information
- a last checked date

Community parking is not automatically marked as verified.

This makes the source of the parking information clearer to the user.

# Authentication and Authorisation Planning

Authentication controls whether a user is signed into ParkMate.

Authorisation controls what the signed-in user is allowed to do.


## Visitors

Visitors can:

- search parking
- view parking results
- view parking details
- view the map


## Registered Users

Registered users can also:

- save favourites
- remove favourites
- view My ParkMate
- add parking
- edit their own parking
- delete their own parking


# Testing Planning

Testing covers the backend functionality and the visible website.


## Automated Testing

Django tests are stored in:

```text
parking/tests.py
```

The test suite is run using:

```bash
python3 manage.py test
```

Django system checks are run using:

```bash
python3 manage.py check
```


## Manual Testing

Manual testing covers:

- registration
- login
- logout
- parking search
- postcode search
- postcode-area search
- parking results
- parking detail pages
- map display
- favourites
- Create
- Read
- Update
- Delete
- form validation
- mobile layout
- tablet layout
- desktop layout
- browser compatibility


## Validation Testing

The final website is also checked using:

- HTML validation
- CSS validation
- Lighthouse


# Success Criteria

ParkMate is successful when a user can:

- search using a town or city
- search using a postcode
- search using a postcode area
- search using a parking name
- view matching parking results
- open parking details
- view parking on a map
- identify Council/NPP price verified parking
- identify mapped parking
- register
- log in
- log out
- save favourites
- remove favourites
- view My ParkMate
- add parking
- edit their own parking
- delete their own parking
- use the website on mobile
- use the website on tablet
- use the website on desktop

The technical success criteria include demonstrating:

- Python
- Django
- relational database functionality
- Django ORM
- authentication
- CRUD
- forms
- validation
- security
- responsive design
- interactive maps
- testing
- deployment

# Changes During Development

During the development of ParkMate, some parts of the original plan changed as the application was built and tested. These changes were made as new requirements became clearer, features were developed and the structure of the Django application evolved.

Documenting these changes shows how the project developed from the original planning stage into the final application.

| Original Plan | Change During Development | Reason for the Change |
| --- | --- | --- |
| ParkMate would use the main Django files such as `models.py`, `views.py`, `forms.py`, `urls.py` and `tests.py`. | Additional project files and functionality were introduced, including custom error handlers, Django Admin configuration, custom management commands and deployment configuration. | As the project became more complex, additional files were needed to separate responsibilities and keep the application organised. |
| Parking data would mainly be added and managed through the application. | A custom Django management command was created to import official parking data from CSV files. A separate command was also used to seed parking data during development. | Importing structured parking data through management commands was more efficient and reliable than manually creating every record. |
| Users would be able to create and manage parking information. | Community parking submissions were separated from trusted/official parking information. Community submissions cannot automatically mark themselves as Council/NPP verified. | This prevents normal users from falsely marking submitted parking information as officially verified. |
| Basic Django authentication would be used for user accounts. | A custom registration form was added using Django's `UserCreationForm`, including email validation and checks for duplicate email addresses. | This provided additional validation and improved the account registration process. |
| Users would be able to manage their own parking submissions. | Ownership checks were added so that users can only edit or delete parking records that they submitted, while authorised staff can also manage records. | This improved security and prevented users from changing another user's parking information. |
| Parking search would allow users to locate parking records. | Search functionality was expanded to work with parking names, addresses, postcodes, postcode areas, local authorities and nations. | Testing showed that users may search for parking using different types of location information, so broader search functionality improved usability. |
| Parking locations would be displayed to users. | An interactive Leaflet map was developed so that database parking locations could also be viewed geographically. | A map provides a more intuitive way for users to understand where parking locations are positioned. |
| Users would be able to save parking locations. | A `Favourite` model and favourite toggle functionality were implemented and connected to the My ParkMate dashboard. | This allowed logged-in users to save useful parking locations and access them again easily. |
| Availability reporting was planned as part of the parking system. | The `AvailabilityReport` model and `AvailabilityReportForm` were created, including validation, but the complete user-facing availability-reporting workflow was not implemented in the final version. | Development time was prioritised towards completing and testing the core parking search, map, favourites and CRUD functionality. Completing availability reporting has therefore been included as a future development. |
| Standard Django error behaviour would initially be used. | Custom error handlers were added for HTTP 400, 403, 404 and 500 errors. | Custom error pages provide clearer feedback and maintain a consistent ParkMate user experience when an error occurs. |
| The application would contain the main user-facing routes. | An application health-check route was also added. | This provides a simple way to confirm that the deployed application is running successfully. |
| The project would use Django's standard database structure. | The database developed into three connected ParkMate models: `ParkingLocation`, `Favourite` and `AvailabilityReport`, alongside Django's built-in `User` model. | The additional models were required to support saved parking locations, user submissions and the planned availability-reporting functionality. |
| The application would eventually be deployed online. | ParkMate was configured for production deployment using Heroku, Gunicorn, WhiteNoise, environment variables and a production database configuration. | These changes were required to run the Django application securely on a cloud-hosting platform rather than only in the local development environment. |

## Features Not Fully Implemented

One planned feature was not completed as a full user-facing feature during the development period.

### Availability Reporting

The database model and Django form for availability reporting were implemented. The form also contains validation to prevent the number of reported available spaces from exceeding the stored capacity of a parking location.

However, the final version does not currently contain a complete user-facing URL, view and template workflow for submitting availability reports.

Rather than presenting this as a completed feature, it has been retained as part of the project's future development plans.

This allowed development and testing to focus on the core functionality of ParkMate, including:

- parking search and filtering
- interactive map functionality
- user authentication
- parking details
- favourites
- My ParkMate
- creating parking records
- editing parking records
- deleting parking records
- ownership and permission checks

The availability-reporting workflow could be completed in a future version by connecting the existing model and form to dedicated views, URLs and user-interface controls.

# Manual Functional Testing

Manual functional testing was used to check that the main ParkMate features work as expected from a user's point of view. Testing covered navigation, parking search, parking information, the interactive map, user authentication, favourites, the My ParkMate dashboard, CRUD functionality, form validation and authorisation.

The tests below were carried out using the deployed version of ParkMate.

| Feature | Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- |
| Home page | Open the ParkMate home page | The home page loads successfully with the main navigation, search area and account options visible | Home page loaded correctly | Pass |
| Navigation | Use the Home, Parking and Map navigation links | Each navigation link opens the correct page | All navigation links opened the expected pages | Pass |
| Parking list | Open the Parking page without entering a search | Active parking locations are displayed as parking cards | Parking locations displayed correctly | Pass |
| Town/city search | Search using a supported town or city, such as Birmingham | Parking locations matching the town or city are displayed | Matching parking locations were returned | Pass |
| Postcode search | Search using a postcode, such as `ME1` | Parking locations matching the postcode are displayed | Relevant postcode results were returned | Pass |
| Postcode-area search | Search using a supported postcode area | ParkMate identifies the associated area and returns relevant parking locations | Relevant parking locations were displayed | Pass |
| Parking name search | Search using the name or part of the name of a parking location | Matching parking locations are displayed | Matching parking locations were returned | Pass |
| Case-insensitive search | Enter a search using different upper/lower-case characters | Search continues to return matching parking locations | Search worked regardless of letter case | Pass |
| No search results | Enter a search term that does not match any parking location | A clear message is displayed explaining that no parking was found | No-results message displayed correctly | Pass |
| Nation filter | Select a nation from the available parking filters | Only parking locations belonging to the selected nation are displayed | Parking results were filtered correctly | Pass |
| Parking details | Select a parking location from the parking results | The parking detail page opens and displays information about the selected location | Correct parking details were displayed | Pass |
| Verification status | View official and community/mapped parking records | Officially verified parking is clearly distinguished from other parking records | Verification information displayed correctly | Pass |
| Map page | Open the Map page | The interactive Leaflet map loads and displays stored parking locations | Map and parking locations loaded correctly | Pass |
| Map search | Search for a location using the map search | The map data is filtered to parking locations matching the search | Matching parking locations were shown | Pass |
| Map marker information | Select a parking marker on the map | Information for the selected parking location is displayed | Correct parking information was displayed | Pass |
| Registration | Register using a new username, valid email address and valid matching passwords | A new account is created, the user is logged in and redirected to My ParkMate | Account was successfully created and user was redirected | Pass |
| Duplicate email | Attempt to register using an email address already associated with another account | Registration is rejected and an error explains that the email address is already in use | Duplicate email was rejected correctly | Pass |
| Password validation | Attempt to register using passwords that do not meet Django's password requirements | Registration is rejected and validation feedback is displayed | Invalid password was rejected | Pass |
| Password confirmation | Enter two different passwords during registration | Registration is rejected and the user is informed that the passwords do not match | Password mismatch was detected correctly | Pass |
| Login | Log in using a valid username and password | User is successfully authenticated and account-only functionality becomes available | Login worked correctly | Pass |
| Invalid login | Attempt to log in using incorrect credentials | Login is rejected and the user remains unauthenticated | Invalid credentials were rejected | Pass |
| Logout | Select the logout option while signed in | The user is logged out and account-only functionality is no longer available | Logout worked correctly | Pass |
| Protected dashboard | Attempt to access My ParkMate while logged out | The user is redirected to the login page | Unauthenticated access was prevented | Pass |
| Save favourite | Log in and save a parking location | The parking location is added to the user's saved parking | Parking location was successfully saved | Pass |
| Favourite button | Save a parking location | The favourite control changes from `Save` to `Saved` | Favourite state updated correctly | Pass |
| My ParkMate favourites | Open My ParkMate after saving a parking location | The saved parking location appears in the user's favourites | Saved parking was displayed correctly | Pass |
| Remove favourite | Select a previously saved parking location again to remove it | The location is removed from the user's saved parking | Favourite was successfully removed | Pass |
| Add parking access | Attempt to open the Add Parking page while logged out | The user is required to log in before adding parking | Unauthenticated user was prevented from adding parking | Pass |
| Add parking | Log in and submit the Add Parking form using valid information | A new parking record is created and the user is redirected to its detail page | Parking location was successfully created | Pass |
| Community verification | Add a parking location as a normal registered user | The new record is stored as community-submitted parking and is not marked Council/NPP verified | Community parking remained unverified | Pass |
| Required fields | Attempt to submit the parking form without completing required fields | The form is not submitted and validation messages identify the missing information | Required-field validation worked correctly | Pass |
| UK latitude validation | Enter a latitude outside the permitted UK range | The parking location is not saved and a validation error is displayed | Invalid latitude was rejected | Pass |
| UK longitude validation | Enter a longitude outside the permitted UK range | The parking location is not saved and a validation error is displayed | Invalid longitude was rejected | Pass |
| Disabled spaces validation | Enter a disabled-space value greater than the total number of spaces | The parking location is not saved and a validation error is displayed | Invalid space values were rejected | Pass |
| Postcode formatting | Enter a postcode using lowercase characters when adding parking | The postcode is stored using uppercase formatting | Postcode was formatted correctly | Pass |
| Edit own parking | Edit a parking location created by the logged-in user | The changes are saved and displayed on the parking detail page | Parking location updated successfully | Pass |
| Edit authorisation | Attempt to edit a parking location submitted by another normal user | The change is prevented and the user is informed that they can only edit their own parking locations | Unauthorised editing was prevented | Pass |
| Delete page | Select Delete for a parking location owned by the logged-in user | A confirmation page is displayed before deletion | Delete confirmation page displayed correctly | Pass |
| Delete own parking | Confirm deletion of a parking location owned by the logged-in user | The parking record is deleted and the user is redirected to My ParkMate | Parking location was successfully deleted | Pass |
| Delete authorisation | Attempt to delete a parking location submitted by another normal user | Deletion is prevented and the original parking record remains unchanged | Unauthorised deletion was prevented | Pass |
| My Parking | Add a parking location and open My ParkMate | The user's own parking submissions are displayed separately from saved favourites | User submissions displayed correctly | Pass |
| Authentication state | Compare navigation while logged in and logged out | Account-related navigation changes appropriately depending on authentication state | Correct navigation options were displayed | Pass |
| Form data retention | Submit a form containing invalid information | Validation messages are displayed without unnecessarily clearing the other entered information | Form remained usable after validation failure | Pass |
| Invalid parking URL | Attempt to open a parking record that does not exist | ParkMate returns the custom 404 error page instead of exposing a server error | Invalid record handled correctly | Pass |
| CRUD workflow | Create, view, edit and finally delete a parking location | The complete Create, Read, Update and Delete workflow works for the logged-in owner | Full CRUD workflow completed successfully | Pass |

### Manual Functional Testing Result

The manual functional testing confirmed that ParkMate's main user-facing functionality operates as intended. Users can search and view parking without an account, while registered users can save favourites and manage their own community parking submissions.

Authentication and authorisation checks also prevent unauthenticated users from accessing protected functionality and prevent normal users from editing or deleting parking records belonging to another user.

Form validation prevents invalid parking data from being stored, including coordinates outside the supported UK range and disabled-space values greater than the total number of spaces. Community-created parking records also remain separate from Council/NPP verified parking so that normal users cannot incorrectly mark their own submissions as officially verified.

All core manual functional tests passed.


## Registration Testing

Registration testing was carried out to ensure that users can create a ParkMate account successfully and that invalid registration details are handled correctly.

The registration form was tested with valid and invalid inputs to confirm that Django's authentication and validation rules work as expected.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Register with valid details | A new account should be created successfully and the user should be logged in | Account was created successfully and the user was logged in | Pass |
| Enter a unique username | The username should be accepted when it is not already registered | Unique username was accepted | Pass |
| Enter a username that already exists | Registration should be prevented and an error message should be displayed | Duplicate username was rejected and validation feedback was displayed | Pass |
| Enter a valid email address | The email address should be accepted | Valid email address was accepted | Pass |
| Enter an email address already registered | Registration should be prevented and the user should be informed that the email address is already in use | Duplicate email address was rejected | Pass |
| Leave the username field empty | Registration should not continue and a required-field message should be displayed | Required-field validation was displayed | Pass |
| Leave the email field empty | Registration should not continue and a required-field message should be displayed | Required-field validation was displayed | Pass |
| Leave the password field empty | Registration should not continue and a required-field message should be displayed | Required-field validation was displayed | Pass |
| Leave the password confirmation field empty | Registration should not continue and a required-field message should be displayed | Required-field validation was displayed | Pass |
| Enter two matching valid passwords | The passwords should be accepted and registration should continue | Matching passwords were accepted | Pass |
| Enter two different passwords | Registration should be prevented and the user should be informed that the passwords do not match | Password mismatch validation was displayed | Pass |
| Enter a password that is too short | Registration should be prevented according to Django's password validation requirements | Short password was rejected | Pass |
| Enter a commonly used password | Registration should be prevented according to Django's password validation requirements | Common password was rejected | Pass |
| Enter an entirely numeric password | Registration should be prevented according to Django's password validation requirements | Numeric-only password was rejected | Pass |
| Enter a password too similar to the user's personal information | Registration should be prevented according to Django's password validation requirements | Similar password was rejected | Pass |
| Submit invalid registration details | The form should remain on the registration page and display validation messages | Validation messages were displayed and the account was not created | Pass |
| Correct invalid details and resubmit | Registration should succeed once all details meet the validation requirements | Account was successfully created after correcting the details | Pass |
| Successful registration redirect | After successful registration, the user should be authenticated and redirected to My ParkMate | User was logged in and redirected to My ParkMate | Pass |
| Registration authentication state | After registration, account-only navigation and features should become available | Logged-in navigation and account features were displayed correctly | Pass |
| Registered user login | Log out and sign back in using the newly created account | The user should be able to log in using the registered credentials | New account successfully logged in | Pass |

### Registration Testing Result

Registration testing confirmed that new users can successfully create a ParkMate account when valid information is provided.

The registration form correctly prevents duplicate usernames and email addresses and applies Django's built-in password validation requirements. Required fields and password confirmation are also validated before an account can be created.

When registration is successful, the new user is authenticated and redirected to My ParkMate, where registered-user functionality becomes available.

All registration tests passed.


## Login and Logout Testing

Login and logout testing was carried out to ensure that registered users can securely access and leave their ParkMate accounts.

Testing included valid and invalid login attempts, protected pages, authentication state changes and successful logout behaviour.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Log in with valid username and password | The user should be authenticated successfully | User was successfully logged in | Pass |
| Log in with an incorrect username | Login should be rejected and the user should remain unauthenticated | Login was rejected and the user remained logged out | Pass |
| Log in with an incorrect password | Login should be rejected and the user should remain unauthenticated | Incorrect password was rejected | Pass |
| Log in with both username and password incorrect | Login should be rejected and authentication should not take place | Invalid credentials were rejected | Pass |
| Leave the username field empty | Login should not continue and required-field validation should be displayed | Required-field validation was displayed | Pass |
| Leave the password field empty | Login should not continue and required-field validation should be displayed | Required-field validation was displayed | Pass |
| Leave both login fields empty | Login should not continue and validation feedback should be displayed | Login was prevented and validation feedback was displayed | Pass |
| Submit invalid login credentials | The user should remain on the login page and receive appropriate feedback | User remained unauthenticated and login feedback was displayed | Pass |
| Correct invalid login details and resubmit | Login should succeed once the correct credentials are entered | User successfully logged in after correcting the credentials | Pass |
| Successful login redirect | After successful login, the user should be redirected to the appropriate ParkMate page | User was successfully redirected after login | Pass |
| Logged-in navigation | Account-related navigation options should become available after login | Logged-in navigation options were displayed correctly | Pass |
| Access My ParkMate while logged in | The user should be able to access their My ParkMate dashboard | My ParkMate loaded successfully | Pass |
| Access Add Parking while logged in | The logged-in user should be able to access the Add Parking page | Add Parking page was accessible | Pass |
| Access My ParkMate while logged out | The user should be redirected to the login page | Unauthenticated user was redirected to login | Pass |
| Access Add Parking while logged out | The user should be required to log in before accessing the page | Unauthenticated user was redirected to login | Pass |
| Access protected edit functionality while logged out | The user should be required to log in before editing parking | Protected edit functionality was inaccessible while logged out | Pass |
| Access protected delete functionality while logged out | The user should be required to log in before deleting parking | Protected delete functionality was inaccessible while logged out | Pass |
| Log out while authenticated | The user should be logged out successfully | User was successfully logged out | Pass |
| Navigation after logout | Logged-in account options should no longer be displayed | Navigation changed correctly after logout | Pass |
| Access My ParkMate after logout | The user should no longer be able to access the protected dashboard without logging in again | User was redirected to the login page | Pass |
| Access protected functionality after logout | Protected features should no longer be available until the user logs in again | Protected functionality was no longer accessible | Pass |
| Log back in after logout | The user should be able to authenticate again using valid credentials | User successfully logged back in | Pass |
| Session authentication | The user's authenticated state should remain active while navigating between ParkMate pages until logout | Authentication remained active while navigating the site | Pass |
| Logout authentication state | After logout, the user's authenticated session should end | User session ended successfully | Pass |

### Login and Logout Testing Result

Login and logout testing confirmed that registered users can successfully authenticate using valid credentials and that invalid login attempts are rejected.

Protected ParkMate functionality, including My ParkMate and parking management features, is only available to authenticated users. Users who attempt to access protected pages while logged out are redirected to the login page.

Logging out successfully ends the authenticated session and removes access to account-only functionality until the user logs in again.

All login and logout tests passed.


## Parking Search Testing

Parking search testing was carried out to ensure that users can search for parking locations using different types of search terms and receive relevant results.

Testing included searching by town or city, postcode, parking name and local authority, as well as checking how ParkMate handles case differences and searches with no matching results.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Open the Parking page without entering a search | All active parking locations should be displayed | Parking locations were displayed correctly | Pass |
| Search using a valid town or city | Parking locations matching the entered town or city should be displayed | Relevant parking locations were returned | Pass |
| Search for Birmingham | Parking locations associated with Birmingham should be displayed | Birmingham parking locations were displayed correctly | Pass |
| Search using a valid postcode | Parking locations matching the entered postcode should be displayed | Relevant postcode results were returned | Pass |
| Search using a postcode area such as `ME1` | ParkMate should return parking locations associated with the postcode area | Relevant parking locations were displayed | Pass |
| Search using a parking location name | Parking locations matching the entered name should be displayed | Matching parking locations were returned | Pass |
| Search using part of a parking location name | ParkMate should return locations containing the entered search text | Partial-name search returned relevant results | Pass |
| Search using a local authority name | Parking locations associated with the local authority should be displayed | Relevant local authority parking was returned | Pass |
| Search using lowercase text | Search should work regardless of letter case | Lowercase search returned the correct results | Pass |
| Search using uppercase text | Search should work regardless of letter case | Uppercase search returned the correct results | Pass |
| Search using mixed uppercase and lowercase text | Search should continue to return matching parking locations | Mixed-case search worked correctly | Pass |
| Search using a term with leading or trailing spaces | Search should still process the useful search text correctly | Relevant results were returned | Pass |
| Search for a location with several matching parking records | All relevant matching parking locations should be displayed | Multiple matching parking locations were displayed | Pass |
| Search for an exact parking location | The matching parking location should appear in the results | Exact parking location was displayed | Pass |
| Search for a term that does not exist | No parking locations should be returned and a clear no-results message should be displayed | No-results message was displayed correctly | Pass |
| Submit an empty search | The Parking page should continue to display the available parking locations | Available parking locations remained visible | Pass |
| Change the search term after a previous search | Results should update to match the new search term | Search results updated correctly | Pass |
| Clear the search term | The full parking list should become available again | Parking list returned correctly | Pass |
| Select a parking result | The user should be taken to the correct parking detail page | Correct parking detail page opened | Pass |
| Search while logged out | Parking search should remain available to guest users | Search worked correctly without authentication | Pass |
| Search while logged in | Parking search should continue to work for authenticated users | Search worked correctly while logged in | Pass |
| Search and then save a parking location while logged in | The matching location should be available to save to favourites | Parking location was successfully available for saving | Pass |
| Search after adding a community parking location | The newly added parking record should appear when searched using matching details | Community parking location appeared in search results | Pass |
| Search results display parking information | Each result should display enough information for the user to identify the parking location | Parking information was displayed correctly | Pass |
| Search results link to the correct record | Selecting a search result should not open a different parking location | Correct parking record was opened | Pass |

### Parking Search Testing Result

Parking search testing confirmed that ParkMate can successfully return relevant parking locations using different search terms, including town or city names, postcodes, parking names and local authority information.

The search functionality works regardless of uppercase or lowercase input and supports partial search terms where appropriate. Searches with no matching parking locations are handled by displaying clear feedback instead of an empty or broken page.

Parking search is available to both guest and registered users, allowing visitors to find and view parking without needing to create an account.

All parking search tests passed.


## Favourites Testing

Favourites testing was carried out to ensure that registered users can save parking locations, view their saved parking and remove locations from their favourites.

Testing also confirmed that favourite functionality is only available to authenticated users and that saved parking is correctly linked to the individual user account.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| View parking while logged out | Parking locations should be viewable without needing an account | Parking locations were displayed correctly | Pass |
| Attempt to save a favourite while logged out | The user should be required to log in before saving a parking location | Unauthenticated user was redirected to login | Pass |
| Log in and open a parking location | Favourite functionality should become available to the authenticated user | Favourite option was displayed correctly | Pass |
| Save a parking location | The selected parking location should be added to the user's favourites | Parking location was successfully saved | Pass |
| Favourite button after saving | The favourite control should update to show that the parking location is saved | Favourite button changed to `Saved` | Pass |
| Open My ParkMate after saving a favourite | The saved parking location should appear in the user's favourites section | Saved parking location appeared correctly | Pass |
| Save multiple parking locations | All selected parking locations should appear in the user's favourites | Multiple favourites were saved successfully | Pass |
| Save different parking locations | Each selected parking location should be stored separately | Different parking locations were saved correctly | Pass |
| Attempt to save the same parking location again | The existing favourite should not be duplicated | Duplicate favourite was not created | Pass |
| View a saved favourite from My ParkMate | Selecting the favourite should open the correct parking detail page | Correct parking detail page opened | Pass |
| Remove a saved favourite | The parking location should be removed from the user's favourites | Favourite was successfully removed | Pass |
| Favourite button after removal | The favourite control should return to its unsaved state | Favourite button updated correctly | Pass |
| Open My ParkMate after removing a favourite | The removed parking location should no longer appear in the favourites section | Removed favourite was no longer displayed | Pass |
| Remove one favourite when several are saved | Only the selected favourite should be removed | Selected favourite was removed while other favourites remained | Pass |
| Save a favourite, log out and log back in | The saved favourite should remain associated with the user's account | Favourite remained saved after logging back in | Pass |
| Refresh the page after saving a favourite | The saved state should remain correctly displayed | Favourite remained marked as saved | Pass |
| Navigate away and return to a saved parking location | The favourite state should still show that the parking location is saved | Saved state remained correct | Pass |
| Favourite while using parking search | A parking location found through search should still be available to save | Search result was successfully saved as a favourite | Pass |
| Favourite a community parking location | The parking location should be saved in the same way as other available parking records | Community parking location was successfully saved | Pass |
| Favourite an official parking location | The parking location should be added to the user's saved parking | Official parking location was successfully saved | Pass |
| User account separation | A favourite saved by one user should not automatically appear in another user's favourites | Favourites remained associated with the correct user | Pass |
| Log out after saving favourites | Account-specific favourite information should no longer be accessible through My ParkMate | Protected favourites were inaccessible while logged out | Pass |
| Log back into the same account | Previously saved favourites should be available again | Saved favourites were displayed correctly | Pass |
| Remove all saved favourites | The favourites section should show no saved parking once all favourites are removed | All favourites were removed successfully | Pass |
| Save a favourite again after removing it | The parking location should be added back to the user's favourites | Parking location was successfully saved again | Pass |

### Favourites Testing Result

Favourites testing confirmed that authenticated ParkMate users can successfully save and remove parking locations from their favourites.

Saved parking locations are displayed within My ParkMate and remain associated with the correct user account between sessions. Duplicate favourites are prevented and removing one saved location does not affect other favourites.

Favourite functionality is protected so that guest users cannot save parking locations until they have logged in.

All favourites tests passed.


## CRUD Testing

CRUD testing was carried out to ensure that authenticated users can create, read, update and delete their own parking submissions correctly.

Testing also confirmed that users cannot edit or delete parking records created by other users and that the correct validation and permissions are applied throughout the CRUD process.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Open Add Parking while logged out | The user should be redirected to the login page | Unauthenticated user was redirected to login | Pass |
| Open Add Parking while logged in | The Add Parking form should be displayed | Add Parking form loaded correctly | Pass |
| Create a parking location with valid details | A new parking record should be created successfully | Parking location was created successfully | Pass |
| Submit Add Parking with required fields missing | The form should not submit and validation messages should be displayed | Required-field validation was displayed | Pass |
| Enter a valid parking name | The parking name should be accepted | Parking name was accepted correctly | Pass |
| Enter a valid address | The address should be accepted | Address was accepted correctly | Pass |
| Enter a valid postcode | The postcode should be accepted and stored correctly | Postcode was accepted successfully | Pass |
| Enter a lowercase postcode | The postcode should be normalised to uppercase | Postcode was stored using uppercase formatting | Pass |
| Enter valid UK latitude and longitude values | The coordinates should be accepted | Valid UK coordinates were accepted | Pass |
| Enter a latitude outside the supported UK range | The form should reject the invalid coordinate | Invalid latitude was rejected | Pass |
| Enter a longitude outside the supported UK range | The form should reject the invalid coordinate | Invalid longitude was rejected | Pass |
| Enter a disabled-space value greater than total spaces | The form should reject the invalid values | Invalid disabled-space value was rejected | Pass |
| Create a community parking location | The parking record should be created as a community submission | Community parking location was created correctly | Pass |
| Create parking as a normal user | The user should not be able to mark the parking as Council/NPP verified | Community submission remained unverified | Pass |
| Successful Create redirect | After creating parking, the user should be redirected to the parking detail page | User was redirected correctly | Pass |
| View newly created parking | The new parking record should display the submitted information | Created parking details were displayed correctly | Pass |
| View parking from the Parking page | The created parking should appear in the available parking records where appropriate | Created parking record was visible | Pass |
| View parking from My ParkMate | The user's own parking submission should appear in My ParkMate | Parking submission appeared correctly | Pass |
| View a parking record owned by another user | The record should remain viewable where public viewing is allowed | Parking details displayed correctly | Pass |
| Open Edit for own parking | The edit form should load with the existing parking information | Edit form loaded with existing values | Pass |
| Update the parking name | The new parking name should be saved | Parking name was updated successfully | Pass |
| Update parking details | The changed details should be stored and displayed | Parking information was updated correctly | Pass |
| Submit invalid information while editing | The update should be prevented and validation messages should be displayed | Invalid update was rejected | Pass |
| Correct an invalid edit and resubmit | The updated details should be saved successfully | Corrected information was saved | Pass |
| Successful Update redirect | After editing, the user should be redirected to the updated parking detail page | User was redirected correctly | Pass |
| Attempt to edit another user's parking | The update should be prevented | Unauthorised editing was prevented | Pass |
| Directly access another user's edit URL | The user should not be allowed to modify the record | Access to unauthorised editing was blocked | Pass |
| Open Delete for own parking | A confirmation page should be displayed before deletion | Delete confirmation page displayed correctly | Pass |
| Cancel deletion | The parking record should remain unchanged | Parking record remained available | Pass |
| Confirm deletion | The parking record should be permanently removed | Parking location was deleted successfully | Pass |
| Successful Delete redirect | After deletion, the user should be redirected away from the removed record | User was redirected correctly | Pass |
| Check My ParkMate after deletion | The deleted parking record should no longer appear | Deleted parking was removed from My ParkMate | Pass |
| Check Parking page after deletion | The deleted parking record should no longer appear in available records | Deleted parking was no longer displayed | Pass |
| Attempt to delete another user's parking | Deletion should be prevented | Unauthorised deletion was prevented | Pass |
| Directly access another user's delete URL | The parking record should remain protected from unauthorised deletion | Delete access was blocked | Pass |
| Refresh after creating parking | The created parking record should still exist | Parking record remained stored correctly | Pass |
| Log out after creating parking | The parking record should remain stored in the database | Parking record remained available | Pass |
| Log back into the same account | The user's parking submission should still appear in My ParkMate | Parking submission remained linked to the account | Pass |
| Complete CRUD workflow | The user should be able to create, view, edit and delete their own parking record successfully | Full CRUD workflow completed correctly | Pass |

### CRUD Testing Result

CRUD testing confirmed that ParkMate allows authenticated users to successfully create, read, update and delete their own parking submissions.

Form validation prevents invalid parking information from being stored, including invalid UK coordinates and disabled-space values that exceed the total number of spaces.

Ownership checks also protect user-created parking records by preventing normal users from editing or deleting submissions that belong to another account.

Community parking submissions remain separate from officially verified Council/NPP parking, ensuring that normal users cannot incorrectly mark their own records as verified.

All CRUD tests passed.

## Authentication and Authorisation Testing

Authentication and authorisation testing was carried out to ensure that ParkMate correctly controls access to protected features and prevents users from modifying data that does not belong to them.

Testing covered logged-in and logged-out behaviour, protected pages, ownership checks and user-specific functionality.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Access the home page while logged out | The home page should remain publicly accessible | Home page loaded correctly | Pass |
| Access the Parking page while logged out | Parking search and viewing should remain publicly accessible | Parking page loaded correctly | Pass |
| Access the Map page while logged out | The map should remain publicly accessible | Map page loaded correctly | Pass |
| Access a parking detail page while logged out | Public parking information should remain viewable | Parking detail page loaded correctly | Pass |
| Access My ParkMate while logged out | The user should be redirected to the login page | Unauthenticated user was redirected to login | Pass |
| Access Add Parking while logged out | The user should be required to log in | Unauthenticated user was redirected to login | Pass |
| Attempt to save a favourite while logged out | The user should be required to authenticate before saving parking | Unauthenticated user was redirected to login | Pass |
| Attempt to access Edit Parking while logged out | The user should be required to log in before editing parking | Unauthenticated edit access was prevented | Pass |
| Attempt to access Delete Parking while logged out | The user should be required to log in before deleting parking | Unauthenticated delete access was prevented | Pass |
| Log in with a valid account | The user should become authenticated | User was successfully authenticated | Pass |
| Access My ParkMate after login | The dashboard should become available | My ParkMate loaded correctly | Pass |
| Access Add Parking after login | The Add Parking form should become available | Add Parking page loaded correctly | Pass |
| Save a favourite after login | The selected parking location should be stored for the authenticated user | Favourite was saved successfully | Pass |
| Create parking after login | The authenticated user should be able to create a parking submission | Parking record was created successfully | Pass |
| View own parking submission | The user should be able to view their created parking record | Own parking record displayed correctly | Pass |
| Edit own parking submission | The user should be allowed to modify their own parking record | Own parking record was updated successfully | Pass |
| Delete own parking submission | The user should be allowed to delete their own parking record | Own parking record was deleted successfully | Pass |
| Attempt to edit another user's parking | The user should not be allowed to modify a parking record owned by another user | Unauthorised edit was prevented | Pass |
| Attempt to delete another user's parking | The user should not be allowed to delete a parking record owned by another user | Unauthorised deletion was prevented | Pass |
| Directly enter another user's edit URL | Ownership checks should prevent modification even when the URL is entered manually | Direct edit access was blocked | Pass |
| Directly enter another user's delete URL | Ownership checks should prevent deletion even when the URL is entered manually | Direct delete access was blocked | Pass |
| View another user's parking record | Public parking information should remain viewable even when the record belongs to another user | Parking information remained viewable | Pass |
| User account separation | Data belonging to one user should not automatically appear in another user's account area | User-specific data remained separated | Pass |
| Favourite account separation | Favourites saved by one user should not appear in another user's favourites | Favourites remained linked to the correct user | Pass |
| Parking ownership association | A community parking submission should remain linked to the account that created it | Parking ownership was stored correctly | Pass |
| My ParkMate account data | The dashboard should only display data relevant to the authenticated user | Correct user-specific information was displayed | Pass |
| Log out of the account | The authenticated session should end | User was successfully logged out | Pass |
| Access My ParkMate immediately after logout | Protected access should no longer be available | User was redirected to login | Pass |
| Access Add Parking immediately after logout | Protected creation functionality should no longer be available | User was redirected to login | Pass |
| Attempt to edit parking after logout | Edit functionality should no longer be available until the user logs in again | Edit access was prevented | Pass |
| Attempt to delete parking after logout | Delete functionality should no longer be available until the user logs in again | Delete access was prevented | Pass |
| Attempt to save a favourite after logout | Favourite functionality should require authentication again | Favourite access was prevented | Pass |
| Log back into the same account | Previously associated account data should become available again | User-specific data was displayed correctly after login | Pass |
| Log into a different account | The second user should only see their own account-specific data | Separate account data was displayed correctly | Pass |
| Normal user verification permissions | A standard registered user should not be able to mark their own parking submission as Council/NPP verified | Community parking remained unverified | Pass |
| Unauthorised modification protection | Changing URLs or navigating directly should not bypass ownership checks | Protected records remained secure | Pass |

### Authentication and Authorisation Testing Result

Authentication and authorisation testing confirmed that ParkMate correctly separates public and protected functionality.

Guest users can search for and view parking information, while account-specific features such as My ParkMate, favourites and parking management require authentication.

Authorisation checks prevent users from editing or deleting parking submissions that belong to another account, including attempts to access protected URLs directly.

User-specific data, including favourites and community parking submissions, remains associated with the correct account. Logging out removes access to protected functionality until the user successfully authenticates again.

All authentication and authorisation tests passed.


## Error Handling Testing

Error handling testing was carried out to ensure that ParkMate responds clearly and safely when users enter invalid data, request pages that do not exist or attempt actions they are not authorised to perform.

Testing covered form validation, invalid URLs, permission errors and custom error pages.

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Open a URL that does not exist | ParkMate should display a custom 404 page instead of a default server error | Custom 404 page displayed correctly | Pass |
| Open a parking record that does not exist | The missing record should be handled safely and a 404 response should be returned | Missing parking record was handled correctly | Pass |
| Submit the registration form with missing required fields | The form should not submit and validation messages should be displayed | Required-field errors were displayed | Pass |
| Submit the login form with missing required fields | Login should not continue and validation feedback should be displayed | Required-field validation was displayed | Pass |
| Enter incorrect login credentials | The user should remain unauthenticated and receive clear feedback | Invalid login attempt was handled correctly | Pass |
| Submit mismatching registration passwords | Registration should be prevented and a password mismatch message should be displayed | Password mismatch error was displayed | Pass |
| Submit a password that does not meet Django requirements | Registration should be prevented and the relevant validation message should be shown | Password validation worked correctly | Pass |
| Register using a duplicate username | Account creation should be prevented | Duplicate username was rejected | Pass |
| Register using a duplicate email address | Account creation should be prevented and clear feedback should be displayed | Duplicate email was rejected | Pass |
| Submit Add Parking with required fields missing | The parking record should not be created and form errors should be displayed | Required-field errors were displayed | Pass |
| Enter an invalid latitude | The form should reject the value and explain that the coordinate is outside the supported range | Invalid latitude was rejected | Pass |
| Enter an invalid longitude | The form should reject the value and explain that the coordinate is outside the supported range | Invalid longitude was rejected | Pass |
| Enter disabled spaces greater than total spaces | The form should reject the invalid values | Validation prevented the invalid parking record | Pass |
| Submit invalid data while editing parking | Changes should not be saved and validation messages should be displayed | Invalid update was rejected | Pass |
| Correct invalid form data and resubmit | The form should submit successfully once the errors are corrected | Corrected data was accepted | Pass |
| Search for a parking location that does not exist | A clear no-results message should be shown instead of a broken page | No-results message displayed correctly | Pass |
| Submit an empty parking search | The page should remain usable and display the available parking data | Parking page continued to work correctly | Pass |
| Access My ParkMate while logged out | The user should be redirected to login instead of seeing a permission-related server error | User was redirected correctly | Pass |
| Access Add Parking while logged out | The user should be redirected to login | Unauthenticated access was handled correctly | Pass |
| Attempt to edit another user's parking | The action should be blocked and handled safely | Unauthorised edit was prevented | Pass |
| Attempt to delete another user's parking | The action should be blocked and the record should remain unchanged | Unauthorised deletion was prevented | Pass |
| Enter another user's edit URL directly | Permission checks should prevent unauthorised modification | Direct unauthorised access was blocked | Pass |
| Enter another user's delete URL directly | Permission checks should prevent unauthorised deletion | Direct unauthorised delete access was blocked | Pass |
| Submit malformed or invalid parking data | Invalid data should not be stored in the database | Invalid parking data was rejected | Pass |
| Refresh a page after a validation error | The application should remain stable and usable | Page remained functional | Pass |
| Return to the form after a validation error | The user should be able to correct the submitted information | Form remained available for correction | Pass |
| Trigger a bad request scenario | ParkMate should return the custom 400 error page where applicable | Custom 400 error handling worked correctly | Pass |
| Trigger a permission-denied scenario | ParkMate should return the custom 403 error page where applicable | Custom 403 error handling worked correctly | Pass |
| Trigger an unexpected server error | ParkMate should use the custom 500 error page instead of exposing technical details | Custom 500 error handling was configured correctly | Pass |
| Error page navigation | Custom error pages should provide a clear way for the user to return to ParkMate | Error page navigation worked correctly | Pass |

### Error Handling Testing Result

Error handling testing confirmed that ParkMate handles invalid user input, missing resources and unauthorised actions without exposing unnecessary technical information or breaking the user experience.

Form validation prevents incorrect information from being submitted and gives users clear feedback so that errors can be corrected.

Missing pages and records are handled through the custom 404 page, while additional custom 400, 403 and 500 error handling provides a consistent ParkMate experience when other errors occur.

Authentication and ownership checks also prevent unauthorised actions from resulting in unsafe changes to user data.

All core error handling tests passed.

## External API Failure Testing

ParkMate uses the Wikimedia Commons API to attempt to retrieve relevant images for parking locations.

The parking image system is designed so that the external API is not required for ParkMate's main functionality. If Wikimedia Commons cannot provide an image or the external request fails, ParkMate can continue displaying the parking information and use its local fallback image where required.

External API failure testing was carried out to confirm that ParkMate remains usable if the Wikimedia Commons API becomes temporarily unavailable or a request cannot be completed.

### How I Tested an External API Failure

I simulated a failed Wikimedia Commons API request using Chrome DevTools.

This allowed me to test the failure handling without changing the ParkMate source code or deliberately breaking the deployed application.

I used the following steps:

1. Opened the ParkMate Parking page in Google Chrome.
2. Pressed `F12` to open Chrome DevTools.
3. Selected the **Network** tab.
4. Reloaded the Parking page so that the network requests appeared.
5. Located the Wikimedia Commons API request.
6. Right-clicked the Wikimedia API request.
7. Selected **Block request URL**.
8. Reloaded the page again while DevTools remained open.
9. Checked whether the fallback image appeared.
10. Checked that the Parking page remained usable.
11. Checked that parking information could still be viewed.
12. Checked that parking search and navigation continued to work.
13. Disabled request blocking after completing the test.
14. Reloaded the page and confirmed that Wikimedia image requests worked normally again.

This simulated a realistic situation where ParkMate could not communicate with the external Wikimedia Commons API.

### Wikimedia API Working Normally

Before blocking the request, I loaded the Parking page normally and confirmed that Wikimedia Commons could be contacted when ParkMate attempted to retrieve an external parking image.

The screenshot below shows the application before the Wikimedia API request was blocked.

![Wikimedia Commons API working normally](static/images/testing/api-test/wikimedia-api-working.png)

### Simulated Wikimedia API Failure

I then used Chrome DevTools to block the Wikimedia Commons API request.

To do this, I opened the **Network** tab, located the Wikimedia request, right-clicked it and selected **Block request URL**.

I then reloaded the Parking page while DevTools remained open.


### Fallback Behaviour During API Failure

After blocking the Wikimedia Commons request, I checked how ParkMate behaved when the external image service could no longer be reached.

The Parking page continued to load and the local ParkMate fallback image was displayed where an external image could not be retrieved.

The screenshot below shows the fallback behaviour while the Wikimedia Commons request was blocked.

![ParkMate fallback image during Wikimedia API failure](static/images/testing/api-test/wikimedia-api-fallback.png)

### Application Functionality During the Failure

While the Wikimedia Commons API request was blocked, I also tested the rest of the Parking page to make sure the API failure did not affect the main functionality of ParkMate.

I confirmed that the following continued to work:

- parking names were still displayed;
- parking addresses were still displayed;
- parking prices remained available;
- verification information remained visible;
- parking search continued to work;
- parking detail pages could still be opened;
- navigation remained usable; and
- the Parking page did not crash or display a server error.

After completing the test, I disabled request blocking in Chrome DevTools and reloaded the page.

The Wikimedia Commons requests were then able to operate normally again.

### External API Failure Test Results

| Test | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Load Parking page before blocking Wikimedia | Wikimedia image requests should operate normally | Wikimedia request operated normally | Pass |
| Open Chrome DevTools Network tab | Network requests should be visible | Network requests were displayed correctly | Pass |
| Locate the Wikimedia Commons API request | The external Wikimedia request should appear in the Network panel | Wikimedia request was identified | Pass |
| Block the Wikimedia request URL | Chrome should prevent the request from reaching Wikimedia | Wikimedia request was successfully blocked | Pass |
| Reload the page with the request blocked | The external image request should fail | Wikimedia request failed as expected | Pass |
| Load Parking page while Wikimedia is blocked | The page should continue loading instead of crashing | Parking page remained fully usable | Pass |
| External image request fails | ParkMate should handle the failed request without breaking the page | Failed request was handled correctly | Pass |
| Check fallback image | A local fallback image should be available when an external image cannot be retrieved | Local fallback image was displayed | Pass |
| Check for broken image | The user should not be left with an unusable broken image | Broken external image was avoided | Pass |
| Check parking names | Parking names should remain visible | Parking names displayed correctly | Pass |
| Check parking addresses | Parking addresses should remain visible | Parking addresses displayed correctly | Pass |
| Check parking prices | Parking price information should remain visible | Parking prices displayed correctly | Pass |
| Check verification information | Verification information should remain visible | Verification information displayed correctly | Pass |
| Search for parking while Wikimedia is blocked | Parking search should continue working because it does not depend on Wikimedia | Parking search continued to work | Pass |
| Open parking detail page while Wikimedia is blocked | Parking information should still be accessible | Parking detail page loaded correctly | Pass |
| Use navigation while Wikimedia is blocked | Site navigation should continue working | Navigation remained functional | Pass |
| Check for application error | The API failure should not cause a Django or JavaScript page failure | Application remained stable | Pass |
| Disable request blocking | Wikimedia requests should be allowed again | Request blocking was successfully disabled | Pass |
| Reload after disabling request blocking | Wikimedia functionality should return to normal | Wikimedia requests operated normally again | Pass |

### External API Failure Testing Result

External API failure testing confirmed that ParkMate remains usable when the Wikimedia Commons API cannot be reached.

The failure was simulated using Chrome DevTools by blocking the Wikimedia Commons request URL and then reloading the Parking page.

When the external request was blocked, ParkMate continued displaying its main parking information and the page remained functional. The failed Wikimedia request did not prevent users from searching for parking, viewing parking details or navigating around the application.

The local fallback image also remained available when an external image could not be retrieved, preventing the external API failure from significantly affecting the user experience.

This test demonstrates that Wikimedia Commons is an enhancement to ParkMate rather than a dependency for the application's core functionality.

After the test was completed, request blocking was disabled and the page was reloaded. Wikimedia Commons image requests then returned to normal.

All external API failure tests passed.




# HTML Validation

The HTML was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check for structural and HTML errors.

## HOME Validation

### Initial Validation

During the first validation of `home.html`, the validator reported a warning because the `home-features` area used a `<section>` element without an identifying heading for the overall section.

![Initial HTML validation](static/images/testing/validation/home.html-validation-before.png)

The original code used:

```html
<section class="home-features" id="about">
```

Although the individual feature cards contained their own `<h2>` headings, the main `<section>` itself did not have a heading describing the whole section.

### Fix Applied

To resolve the validation warning, I changed the `home-features` container in `home.html` from a `<section>` element to a `<div>`:

```html
<div class="home-features" id="about">
```

The matching closing tag was also changed from:

```html
</section>
```

to:

```html
</div>
```

A `<div>` was more appropriate because this element is mainly used as a container to group the Search, Map and Save feature cards rather than representing a separate semantic section of the page.

I also cleaned up the formatting of `home.html`, including indentation and spacing, to make the HTML easier to read and maintain.

### Trailing Slash Validation Messages

The W3C validator also displayed informational messages about trailing slashes on void HTML elements, for example:

```html
<meta charset="utf-8" />
<link rel="stylesheet" href="..." />
```

These trailing slashes are commonly seen in XHTML-style formatting. In HTML5, void elements such as `<meta>`, `<link>`, `<img>` and `<input>` do not need a closing slash, but using one does not stop the browser from interpreting the HTML correctly.

I filtered these messages because they were informational notices rather than structural errors affecting the page. The formatting was also used consistently throughout the project, so I chose not to make unnecessary changes just to remove these notices.

The main validation issue was the missing heading warning on the `home-features` `<section>`, which was fixed by changing the container to a `<div>`.

### Final Validation

After making the structural change, `home.html` was tested again using the W3C Markup Validation Service.

![Final HTML validation](static/images/testing/validation/home.html-validation-after.png)

The previous section-heading warning was resolved. The remaining trailing-slash messages were filtered because they were informational notices rather than errors affecting the structure or functionality of the website.

## Parking Page Validation

The rendered Parking page was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check the final HTML output produced by Django.

The Parking page is generated using `templates/base.html` and `templates/parking/list.html`, with `list.html` extending the main `base.html` template. I opened the Parking page in the browser, used **View Page Source**, and validated the final combined HTML that was sent to the browser.

The page passed validation with no HTML errors, so no changes were required.

![Parking page validation](static/images/testing/validation/parking-page-validation.png)


## Map Page Validation

The rendered Map page was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check the final HTML output produced by Django.

The Map page is generated using `templates/base.html` and `templates/parking/map.html`, with `map.html` extending the main `base.html` template. I opened the Map page in the browser, used **View Page Source**, and validated the final combined HTML that was sent to the browser.

The page passed validation with no HTML errors, so no changes were required.

![Map page validation](static/images/testing/validation/map-page-validation.png)

## Login Page Validation

The rendered Login page was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check the final HTML output produced by Django.

The Login page is generated using `templates/base.html` and `templates/registration/login.html`, with `login.html` extending the main `base.html` template. I opened the Login page in the browser, used **View Page Source**, and validated the final combined HTML that was sent to the browser.

The page passed validation with no HTML errors, so no changes were required.

![Login page validation](static/images/testing/validation/login-page-validation.png)



## Registration Page Validation

The Registration page was tested using the [W3C Markup Validation Service](https://validator.w3.org/).

The page uses `base.html` for the main site layout and `registration/register.html` for the registration form.

### Before Validation

The first validation test identified two HTML errors.

The first error was caused by an `aria-label` being used directly on the account benefits `<div>`. The `<div>` did not have a suitable ARIA role, so the `aria-label` was removed.

The second error was caused by Django's automatically generated password help text. Django outputs the password requirements as a `<ul>` list, but the help text was being wrapped inside a `<small>` element. As a `<ul>` cannot be placed inside a `<small>` element, this caused an HTML validation error.

![Registration page validation before fixes](static/images/testing/validation/registration-page-validation-before.png)

### Changes Made

The account benefits section was changed from:

```html
<div class="auth-benefits" aria-label="Account benefits">
```

to:

```html
<div class="auth-benefits">
```

The Django form help text was also changed from:

```html
{% if field.help_text %}
  <small>{{ field.help_text|safe }}</small>
{% endif %}
```

to:

```html
{% if field.help_text %}
  <div class="field-help">
    {{ field.help_text|safe }}
  </div>
{% endif %}
```

This allows Django's generated `<ul>` password requirements to be displayed inside a valid HTML container.

### After Validation

After making these changes, the Registration page was tested again using the W3C Markup Validation Service.

The previous validation errors were resolved and the page successfully passed HTML validation.

![Registration page validation after fixes](static/images/testing/validation/registration-page-validation-after.png)

## Dashboard Page Validation

The rendered Dashboard page was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check the final HTML output produced by Django.

The Dashboard page is generated using `templates/base.html` and `templates/parking/dashboard.html`, with `dashboard.html` extending the main `base.html` template. I opened the Dashboard page in the browser, used **View Page Source**, and validated the final combined HTML that was sent to the browser.

The page passed validation with no HTML errors, so no changes were required.

![Dashboard page validation](static/images/testing/validation/dashboard-page-validation.png)

## Add Parking Page Validation

The rendered Add Parking page was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check the final HTML output produced by Django.

The Add Parking page is generated using `templates/base.html` and `templates/parking/form.html`, with `form.html` extending the main `base.html` template. I opened the Add Parking page in the browser, used **View Page Source**, and validated the final combined HTML that was sent to the browser.

The page passed validation with no HTML errors, so no changes were required.

![Add Parking page validation](static/images/testing/validation/add-parking-page-validation.png)


## Delete Page Validation

The rendered Delete page was tested using the [W3C Markup Validation Service](https://validator.w3.org/) to check the final HTML output produced by Django.

The Delete page is generated using `templates/base.html` and `templates/parking/delete.html`, with `delete.html` extending the main `base.html` template. I opened the Delete page in the browser, used **View Page Source**, and validated the final combined HTML that was sent to the browser.

The page passed validation with no HTML errors, so no changes were required.

![Delete page validation](static/images/testing/validation/delete-page-validation.png)


# CSS Validation

The ParkMate stylesheet was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check for CSS errors and ensure that the styling followed valid CSS standards.

The stylesheet passed validation with no CSS errors found, so no changes were required.

![CSS validation](static/images/testing/validation/css-validation.png)

# JavaScript JSLint Validation

The JavaScript file responsible for loading parking images from Wikimedia Commons was tested using JSLint. The initial validation returned 22 warnings relating to browser globals, arrow functions, object property order, trailing commas, `continue` statements, unused variables, and strict indentation and line formatting.

## Before corrections

The original JavaScript returned 22 JSLint warnings.

![JSLint validation before corrections](static/images/testing/validation/js-lint-before.png)

The main warnings included:

- `document`, `URLSearchParams`, and `fetch` being reported as undeclared browser globals.
- Complex arrow functions being flagged by JSLint.
- Properties inside `URLSearchParams` objects not being ordered according to JSLint requirements.
- Trailing commas being reported as unexpected.
- `continue` statements being flagged.
- The `error` variable inside `catch (error)` being declared but never used.
- Multi-line assignments and expressions not matching JSLint's strict indentation rules.
- Multi-line function arguments being flagged because of their column alignment.

## Corrections made

The following changes were made to resolve the JSLint warnings while keeping the existing Wikimedia Commons image functionality unchanged.

### Browser environment

The following JSLint browser directive was added to the top of the JavaScript file:

```javascript
/*jslint browser*/
```

This informs JSLint that the JavaScript is intended to run inside a web browser and allows browser-provided globals such as `document`, `fetch`, and `URLSearchParams`.

### Complex arrow functions

The main `DOMContentLoaded` arrow function:

```javascript
document.addEventListener("DOMContentLoaded", () => {
```

was changed to:

```javascript
document.addEventListener("DOMContentLoaded", function () {
```

The `forEach` arrow function:

```javascript
images.forEach((image) => {
    loadImage(image);
});
```

was also changed to:

```javascript
images.forEach(function (image) {
    loadImage(image);
});
```

This resolved JSLint warnings relating to complex arrow functions.

### Multi-line assignments

Several assignments were originally split across multiple lines.

For example:

```javascript
const fallback =
    document.body.dataset.parkingFallback || "";
```

was changed to:

```javascript
const fallback = document.body.dataset.parkingFallback || "";
```

The Wikimedia Commons API endpoint:

```javascript
const commonsEndpoint =
    "https://commons.wikimedia.org/w/api.php";
```

was changed to:

```javascript
const commonsEndpoint = "https://commons.wikimedia.org/w/api.php";
```

Similar changes were made to other assignments throughout the file to follow JSLint's indentation requirements.

### Wikimedia search parameters

The properties inside the Wikimedia Commons `URLSearchParams` object were reordered to meet JSLint's expected property ordering.

The corrected text search parameters are:

```javascript
const params = new URLSearchParams({
    action: "query",
    format: "json",
    generator: "search",
    gsrlimit: "10",
    gsrnamespace: "6",
    gsrsearch: searchText,
    iiprop: "url",
    iiurlwidth: "900",
    origin: "*",
    prop: "imageinfo"
});
```

The trailing comma after the final object property was also removed.

### Nearby image search parameters

The properties used for the Wikimedia Commons geographic search were also reordered.

The corrected parameters are:

```javascript
const params = new URLSearchParams({
    action: "query",
    format: "json",
    generator: "geosearch",
    ggscoord: `${latitude}|${longitude}`,
    ggslimit: "10",
    ggsnamespace: "6",
    ggsprimary: "all",
    ggsradius: "1000",
    iiprop: "url",
    iiurlwidth: "900",
    origin: "*",
    prop: "imageinfo"
});
```

This resolved the property-order and trailing-comma warnings reported by JSLint.

### Fetch requests

Multi-line `fetch()` requests were simplified.

The original:

```javascript
const response = await fetch(
    `${commonsEndpoint}?${params}`
);
```

was changed to:

```javascript
const response = await fetch(`${commonsEndpoint}?${params}`);
```

This change was applied to both Wikimedia Commons requests.

### Object values

The original multi-line `Object.values()` statement:

```javascript
const pages = Object.values(
    data.query.pages
);
```

was changed to:

```javascript
const pages = Object.values(data.query.pages);
```

This correction was applied to both Wikimedia search functions.

### Continue statements

JSLint reported warnings for the use of `continue`.

The original code:

```javascript
for (const page of pages) {
    const info =
        page.imageinfo &&
        page.imageinfo[0];

    if (!info) {
        continue;
    }

    const imageUrl =
        info.thumburl ||
        info.url;

    if (imageUrl) {
        return imageUrl;
    }
}
```

was changed to:

```javascript
for (const page of pages) {
    const info = page.imageinfo && page.imageinfo[0];

    if (info) {
        const imageUrl = info.thumburl || info.url;

        if (imageUrl) {
            return imageUrl;
        }
    }
}
```

This keeps the same behaviour while avoiding the use of `continue`.

The correction was applied to both the standard Wikimedia search and nearby geographic search.

### Unused error variables

The original `catch` blocks contained an `error` variable that was not used:

```javascript
} catch (error) {
    return null;
}
```

These were changed to:

```javascript
} catch {
    return null;
}
```

This resolved the unused variable warnings.

### Search function formatting

The nearby search function was originally written across multiple lines:

```javascript
async function searchNearby(
    latitude,
    longitude
) {
```

It was changed to:

```javascript
async function searchNearby(latitude, longitude) {
```

This follows JSLint's expected formatting.

### Parking image dataset values

The original parking image values were split across multiple lines:

```javascript
const fullSearch =
    image.dataset.parkingImage || "";

const latitude =
    image.dataset.latitude || "";

const longitude =
    image.dataset.longitude || "";
```

They were changed to:

```javascript
const fullSearch = image.dataset.parkingImage || "";
const latitude = image.dataset.latitude || "";
const longitude = image.dataset.longitude || "";
```

This resolved the related indentation warnings.

## Wikimedia search assignments

The original search assignment:

```javascript
commonsImage =
    await searchCommons(fullSearch);
```

was changed to:

```javascript
commonsImage = await searchCommons(fullSearch);
```

The shortened location-name search was changed in the same way.

The original:

```javascript
const locationName =
    fullSearch.split(",")[0];

commonsImage =
    await searchCommons(locationName);
```

was changed to:

```javascript
const locationName = fullSearch.split(",")[0];
commonsImage = await searchCommons(locationName);
```

#### Nearby search assignment

The original nearby image search:

```javascript
commonsImage =
    await searchNearby(
        latitude,
        longitude
    );
```

was changed to:

```javascript
commonsImage = await searchNearby(latitude, longitude);
```

This resolved the remaining JSLint indentation and column-position warnings.

## After corrections

After all corrections were made, the JavaScript was tested again using JSLint.

![JSLint validation after corrections](static/images/testing/validation/js-lint-after.png)

The corrections improved the formatting and quality of the JavaScript while keeping the original Wikimedia Commons functionality unchanged.

The JavaScript continues to:

- search Wikimedia Commons using the full parking location name;
- retry the search using the shortened location name;
- search for nearby Wikimedia images using latitude and longitude;
- display a Wikimedia Commons image when one is available; and
- display the ParkMate fallback image when no suitable Wikimedia Commons image can be found.


# Bugs and Fixes

During the development of ParkMate, I identified several issues within the
Django templates. These included an actual Django template syntax error,
template blocks and conditional statements that were difficult to read, and
HTML and JavaScript that required restructuring to make the code easier to
debug and maintain.

The fixes were completed across two commits:

`7f567ff - fix: correct template syntax errors`

`c939fc3 - fix: correct parking filter syntax`

The first commit updated three files:

- `templates/base.html`
- `templates/parking/list.html`
- `templates/parking/map.html`

This commit contained 237 additions and 66 deletions.

During further testing and review, I found that the nation parking filter still
contained an incorrect comparison operator. This was corrected in the second
commit:

`c939fc3 - fix: correct parking filter syntax`

This follow-up commit changed one file with one addition and one deletion.

The debugging process involved both correcting genuine syntax problems and
refactoring surrounding code to improve readability, maintainability and
consistency.

---

### Navigation Conditional

**File:** `templates/base.html`

The navigation contains a link that displays different text depending on
whether the logged-in user is a staff member.

Previously, the complete Django conditional was written inline:

```html
<a href="{% url 'parking:create' %}">
    {% if user.is_staff %} Add official parking {% else %} Add parking {% endif %}
</a>
```

This was changed to:

```html
<a href="{% url 'parking:create' %}">
    {% if user.is_staff %}
        Add official parking
    {% else %}
        Add parking
    {% endif %}
</a>
```

#### Why this was changed

The condition has two possible outcomes:

- Staff users see `Add official parking`.
- Other authenticated users see `Add parking`.

Writing the `{% if %}`, `{% else %}` and `{% endif %}` statements separately
makes the conditional easier to understand.

It also makes future changes to the navigation easier because the opening,
alternative and closing parts of the condition can be identified immediately.

The functionality of the link was retained.

---

## Parking List Template Fixes

### Template Inheritance

**File:** `templates/parking/list.html`

The Django template inheritance and static-file loading statements were
originally placed together:

```django
{% extends 'base.html' %} {% load static %}
```

They were separated into:

```django
{% extends 'base.html' %}
{% load static %}
```

#### Why this was changed

`{% extends %}` tells Django which parent template should be used.

`{% load static %}` loads Django's static template functionality.

Putting these statements on separate lines makes the template structure
clearer and makes template-related problems easier to identify during
debugging.

---

### Page Title and Content Blocks

The title and content blocks were originally written together:

```django
{% block title %} Find Parking - ParkMate {% endblock %} {% block content %}
```

They were changed to:

```django
{% block title %}
Find Parking - ParkMate
{% endblock %}

{% block content %}
```

#### Why this was changed

Django template blocks define sections that are inserted into the parent
template.

Separating each block makes it much easier to identify:

- Where the title block begins.
- Where the title block ends.
- Where the content block begins.
- Where the content block eventually ends.

This makes the template hierarchy clearer and reduces the risk of incorrectly
nesting template content.

---

### Parking Search Input

The parking search input originally appeared on a single line:

```html
<input name="q" value="{{ q }}" />
```

It was reformatted to:

```html
<input
    name="q"
    value="{{ q }}"
/>
```

#### Why this was changed

This was a readability improvement rather than a functional change.

Separating the attributes makes the input easier to read and makes it easier
to add additional attributes later.

The `{{ q }}` value remains in place so that the user's previous search term
can remain visible when the results page reloads.

---

### Parking Filter Syntax Error

**File:** `templates/parking/list.html`

While correcting the template structure, the nation filter was also reviewed.

The filter is responsible for checking which nation the user selected and
adding the HTML `selected` attribute to the correct option.

After the first template-fixing commit, the condition appeared as:

```django
{% if nation = value %}selected{% endif %}
```

This still contained a syntax error because a single equals sign was being
used for the comparison.

The issue was found during further review and corrected in:

`c939fc3 - fix: correct parking filter syntax`

The condition was changed to:

```django
{% if nation == value %}selected{% endif %}
```

The complete corrected option is:

```django
<option
    value="{{ value }}"
    {% if nation == value %}selected{% endif %}
>
    {{ label }}
</option>
```

#### Why this was a bug

The purpose of the condition is to compare two values:

```django
nation
```

and:

```django
value
```

The original condition used:

```django
nation = value
```

The comparison needed to use:

```django
nation == value
```

The corrected `==` operator checks whether the selected nation is equal to the
current nation option being processed by the template.

#### How the corrected filter works

The template loops through the available nations.

For each option Django checks:

```django
{% if nation == value %}
```

If the values match, Django outputs:

```html
selected
```

This allows the browser to keep that nation selected after the user submits
the search form.

For example, the resulting HTML could contain:

```html
<option value="ENG" selected>
    England
</option>
```

If the nation does not match the current option, the `selected` attribute is
not added.

#### Result of the fix

Changing:

```django
{% if nation = value %}
```

to:

```django
{% if nation == value %}
```

corrected the nation filter comparison.

The fix ensures that:

- The Django template uses the correct comparison syntax.
- The nation value can be compared correctly.
- The correct option can receive the `selected` attribute.
- The user's selected nation can remain selected after a search.
- The incorrect single `=` condition is no longer present.

---

### Search Button

The search button was changed from:

```html
<button type="submit" class="green-button">Search</button>
```

to:

```html
<button type="submit" class="green-button">
    Search
</button>
```

#### Why this was changed

This was a code readability improvement.

The functionality remained unchanged, but the button now follows the
multi-line formatting used by other interactive elements in the project.

---

### Parking Search Label

The parking search label changed from:

```html
<p class="mini-label">Parking search</p>
```

to:

```html
<p class="mini-label">
    Parking search
</p>
```

#### Why this was changed

This keeps the formatting consistent with the surrounding HTML and makes the
template easier to scan.

There was no functional change.

---

### Parking Search Results Heading

The search heading previously contained the whole conditional on one line:

```django
{% if q %} Results for “{{ q }}” {% else %} Parking locations {% endif %}
```

It was separated into:

```django
{% if q %}
    Results for “{{ q }}”
{% else %}
    Parking locations
{% endif %}
```

#### Why this was changed

The heading has two possible states.

If a search query exists, the page displays:

`Results for "search term"`

If no query exists, the page displays:

`Parking locations`

Separating these states makes the conditional much easier to understand and
maintain.

---

### Parking Result Count

The parking result count was reorganised into:

```django
{{ locations|length }}
parking location{{ locations|length|pluralize }}
shown
```

#### Why this was changed

The expression uses:

```django
locations|length
```

to determine the number of parking locations returned.

It also uses Django's:

```django
pluralize
```

filter to automatically display the correct singular or plural text.

For example:

```text
1 parking location shown
```

or:

```text
5 parking locations shown
```

The functionality was retained while the template became easier to read.

---

### Parking Result Card Structure

Each parking result is displayed inside an `<article>`.

The result card includes a Django condition that controls which CSS class is
applied depending on the verification status of the parking location.

The condition uses:

```django
{% if location.council_verified %}
```

to distinguish between verified and mapped parking locations.

#### Why this was changed

The `<article>` and conditional class structure were reorganised to make the
relationship between the parking data and its CSS class easier to understand.

This was mainly a readability improvement and did not remove the existing
verification functionality.

---

### Parking Image

The parking result card continues to use the location image when one is
available.

If no parking image is available, the template uses:

```django
{% static 'images/parking-fallback.svg' %}
```

as a fallback.

The image also retains descriptive alternative text and:

```html
loading="lazy"
```

#### Why this is important

The fallback prevents a parking card from being left without an image when no
specific image URL exists.

The alternative text helps describe the image.

Lazy loading prevents images further down the results page from being loaded
before they are required.

The surrounding code was reformatted for readability while this functionality
was retained.

---

### Parking Location Heading

The location heading changed from:

```html
<h2>{{ location.name }}</h2>
```

to:

```html
<h2>
    {{ location.name }}
</h2>
```

#### Why this was changed

This separates the Django variable from the surrounding HTML tags and makes
the result-card structure easier to read.

No functional change was made.

---

### Address and Postcode Conditional

The parking address and postcode had previously been placed together with the
postcode condition inline.

The code was changed so that the optional postcode condition is easier to
identify:

```django
<p>
    {{ location.address }}

    {% if location.postcode %}
        · {{ location.postcode }}
    {% endif %}
</p>
```

#### Why this was changed

Not every parking location is guaranteed to contain a postcode.

The condition ensures that:

```django
{{ location.postcode }}
```

is only displayed when the location contains a postcode.

It also avoids displaying the separator when no postcode exists.

The separated structure makes the optional nature of the postcode much easier
to understand.

---

### Parking Verification Badge

Council/NPP verified parking locations display:

```html
<span class="verified-pill">
    ✓ Council/NPP price verified
</span>
```

Other parking locations display:

```html
<span class="mapped-pill">
    Mapped parking
</span>
```

#### Why this was changed

The badge elements were separated from the surrounding Django conditional.

This makes the two possible verification states much easier to identify when
reading the source code.

It also makes the badge text and styling easier to modify later.

The underlying verification logic remained unchanged.

---

### Parking Tariff Information

The tariff information continues to use:

```django
{{ location.tariff_info|default:"Price not supplied"|truncatechars:80 }}
```

#### Why this was changed

The expression had previously been split awkwardly across multiple lines.

Keeping the Django variable and its filters together makes the expression
easier to understand.

The:

```django
default:"Price not supplied"
```

filter displays `Price not supplied` when no tariff information exists.

The:

```django
truncatechars:80
```

filter prevents a very long tariff description from taking up too much space
inside a parking result card.

---

### Parking Spaces

The number of parking spaces continues to use:

```django
{{ location.spaces_total|default:"Not supplied" }}
```

#### Why this is important

If the number of parking spaces has not been provided, ParkMate displays:

```text
Not supplied
```

instead of leaving the information blank.

No functional change was made to this expression during the restructuring.

---

### Local Authority

The local authority output changed from:

```html
<span> {{ location.local_authority }} </span>
```

to:

```html
<span>
    {{ location.local_authority }}
</span>
```

#### Why this was changed

This was a readability and formatting improvement.

Separating the Django variable makes it easier to identify the information
being displayed inside the result card.

---

### View Details Link

The parking details link was changed from a compact element to:

```html
<a
    class="detail-button"
    href="{{ location.get_absolute_url }}"
>
    View details
</a>
```

#### Why this was changed

Separating the attributes makes the HTML easier to read.

The link continues to use:

```django
{{ location.get_absolute_url }}
```

which directs the user to the detail page belonging to the selected parking
location.

The navigation behaviour was retained.

---

### Favourite Parking Form

Authenticated users can save parking locations to their favourites.

The form continues to contain:

```django
{% csrf_token %}
```

and:

```html
<input
    type="hidden"
    name="next"
    value="{{ request.get_full_path }}"
/>
```

#### Why these are needed

The CSRF token protects the POST request made when the user saves or removes a
parking location.

The hidden `next` field stores the current page location.

This allows the application to return the user to the same page after the
favourite action has been completed.

---

### Favourite Button Conditional

The favourite button previously contained its complete conditional inline.

It was restructured to:

```django
<button
    class="outline-button small-button"
    type="submit"
>
    {% if location.pk in favourite_ids %}
        ♥ Saved
    {% else %}
        ♡ Save
    {% endif %}
</button>
```

#### Why this was changed

The button has two possible states.

If the location already exists within:

```django
favourite_ids
```

the user sees:

```text
♥ Saved
```

Otherwise the user sees:

```text
♡ Save
```

Separating the `{% if %}`, `{% else %}` and `{% endif %}` statements makes
this logic much easier to follow.

The favourite functionality itself remained unchanged.

---

### Empty Parking Search State

When the parking search returns no matching locations, the `{% empty %}`
section of the Django loop is displayed.

The markup changed from:

```html
<h2>No parking found</h2>
<p>Try a broader town, postcode or parking name.</p>
```

to:

```html
<h2>
    No parking found
</h2>

<p>
    Try a broader town, postcode or parking name.
</p>
```

#### Why this was changed

The empty-state markup was reformatted so that it follows the same structure
as the other elements in the template.

The message shown to the user remained unchanged.

---

### Closing Parking List Content Block

The final:

```django
{% endblock %}
```

was placed clearly on its own line.

#### Why this was changed

This makes it easier to identify where the parking list's main content block
finishes.

It also makes it easier to match the closing tag with:

```django
{% block content %}
```

when editing or debugging the template later.

---

## Parking Map Template Fixes

### Template Inheritance

**File:** `templates/parking/map.html`

The map template originally contained:

```django
{% extends 'base.html' %} {% load static %}
```

This was changed to:

```django
{% extends 'base.html' %}
{% load static %}
```

#### Why this was changed

This separates the parent-template declaration from static-file loading.

It also keeps the beginning of the map template consistent with the corrected
parking list template.

---

### Parking Map Title and Content Blocks

The title and content blocks were originally written together:

```django
{% block title %} Parking Map - ParkMate {% endblock %} {% block content %}
```

They were changed to:

```django
{% block title %}
Parking Map - ParkMate
{% endblock %}

{% block content %}
```

#### Why this was changed

The change makes it immediately clear where the title block finishes and where
the main map content begins.

This makes the Django template hierarchy easier to understand and maintain.

---

### Parking Map Heading

The map page contains:

```html
<p class="mini-label">Parking map</p>

<h1>Parking map</h1>
```

The page also explains that its markers come from the ParkMate database rather
than depending on live parking APIs.

The surrounding template structure was reformatted to make the heading and
content easier to identify.

#### Why this was changed

The change improves the organisation of the HTML without altering what the
user sees.

---

### Map Search Input

The map search field changed from:

```html
<input name="q" value="{{ q }}" />
```

to:

```html
<input
    name="q"
    value="{{ q }}"
/>
```

The search icon markup was also cleaned up.

#### Why this was changed

The search field is easier to read when its attributes are separated.

The `{{ q }}` value remains so that the user's current search can remain
visible when the page reloads.

No search functionality was removed.

---

### Search Map Button

The button changed from:

```html
<button type="submit" class="green-button">Search map</button>
```

to:

```html
<button type="submit" class="green-button">
    Search map
</button>
```

#### Why this was changed

This makes the button formatting consistent with the other buttons within
ParkMate.

The functionality remained unchanged.

---

### Show All Link

When a map search is active, ParkMate provides a **Show all** link.

The link was reformatted to:

```html
<a
    class="outline-button"
    href="{% url 'parking:map' %}"
>
    Show all
</a>
```

It remains inside:

```django
{% if q %}
```

#### Why this was changed

The link should only be displayed when the user currently has an active search
query.

Selecting **Show all** returns the user to the complete parking map without
the current search filter.

Separating the class, URL and text makes the purpose of the link easier to
understand.

---

### Leaflet Map Container

The Leaflet map continues to use:

```html
<div
    id="parking-map"
    style="height: 580px; border-radius: 18px; overflow: hidden"
></div>
```

#### Why this is important

The JavaScript later searches for:

```text
parking-map
```

to find the HTML element where the Leaflet map should be created.

The map container remained functionally unchanged.

---

### Empty Map Search State

When no parking locations match the map search, the template checks:

```django
{% if not map_locations %}
```

and displays:

```html
<h2>No matching parking found</h2>

<p>
    Try another town, postcode or parking name.
</p>
```

#### Why this was changed

The paragraph was reformatted to make the empty-state structure consistent
with the rest of the template.

The behaviour and message shown to the user remained unchanged.

---

### Django Map Data and Scripts Block

An important structural change was made around the data passed from Django to
the Leaflet JavaScript.

Previously, the `json_script`, content closing block and scripts opening block
were placed together.

They were separated into:

```django
{{ map_locations|json_script:"parkmate-map-data" }}

{% endblock %}

{% block scripts %}
```

#### Why this was changed

The:

```django
json_script
```

template filter safely places the parking data into the page so that
JavaScript can access it.

The first:

```django
{% endblock %}
```

closes the main page content.

The:

```django
{% block scripts %}
```

statement then starts the JavaScript section.

Separating these statements makes the Django template hierarchy much clearer.

It also reduces the risk of accidentally placing JavaScript code inside the
wrong block when the template is updated later.

---

### Retrieving the Map and Parking Data

The JavaScript retrieves the map element and the Django JSON data using:

```javascript
const element = document.getElementById("parking-map");
const dataElement = document.getElementById("parkmate-map-data");
```

The code then checks:

```javascript
if (!element || !dataElement || typeof L === "undefined") {
    return;
}
```

#### Why this is important

The JavaScript requires:

- The `parking-map` HTML element.
- The parking data generated by Django.
- The Leaflet library.

If one of these is unavailable, the script returns before attempting to create
the map.

This is defensive programming because it prevents later map code from
attempting to work with missing elements or an unavailable Leaflet library.

---

### Converting Django Parking Data into JavaScript

The parking location data is converted using:

```javascript
const locations = JSON.parse(dataElement.textContent);
```

#### Why this is needed

Django's:

```django
json_script
```

output contains JSON text.

`JSON.parse()` converts that text into JavaScript data.

The resulting `locations` data can then be used when creating the Leaflet map
markers.

---

### Creating the Leaflet Map

The map is created using:

```javascript
const map = L.map(element).setView([54.2, -2.7], 6);
```

#### Why this is needed

This creates the Leaflet map inside the `parking-map` element.

The starting coordinates and zoom level provide an initial UK view before the
map adjusts according to the locations being displayed.

---

### OpenStreetMap Tile Layer

The OpenStreetMap tile layer was reformatted from a more compact function call
into:

```javascript
L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap contributors",
    }
).addTo(map);
```

#### Why this was changed

Separating the URL and configuration object makes the Leaflet setup easier to
understand.

The functionality remained the same.

ParkMate continues to:

- Use OpenStreetMap tiles.
- Use a maximum zoom level of `19`.
- Display OpenStreetMap attribution.
- Add the tile layer to the Leaflet map.

---

### Marker Bounds

Before creating markers, an empty array is created:

```javascript
const bounds = [];
```

#### Why this is needed

Each parking location's latitude and longitude can be added to this array.

The complete collection of coordinates is then used later to determine the
appropriate map zoom and position.

---

### Creating Parking Markers

Each parking location is processed using:

```javascript
locations.forEach((item) => {
```

Marker creation changed from:

```javascript
const marker = L.marker([item.lat, item.lon]).addTo(map);
```

to:

```javascript
const marker = L.marker([
    item.lat,
    item.lon,
]).addTo(map);
```

#### Why this was changed

The latitude and longitude are easier to identify when placed on separate
lines.

This makes the map code easier to read when debugging marker coordinates.

The actual marker functionality did not change.

---

### Marker Verification Status

The JavaScript determines which verification message should be displayed
using:

```javascript
const badge = item.verified
    ? "Council/NPP price verified"
    : "Mapped parking";
```

#### Why this is needed

Each map marker can tell the user whether its parking information is verified.

Verified locations display:

```text
Council/NPP price verified
```

Other locations display:

```text
Mapped parking
```

This functionality was retained during the restructuring.

---

### Parking Marker Popup

The Leaflet marker popup was also reformatted.

The popup now has a clearer structure:

```javascript
marker.bindPopup(`
    <strong>${item.name}</strong>
    <br>
    ${item.address}
    <br>
    ${item.postcode || ""}
    <br>
    <b>${item.price}</b>
    <br>
    <small>${badge}</small>
    <br>
    <a href="/parking/${item.id}/">
        View details
    </a>
`);
```

#### Why this was changed

The previous popup formatting was harder to read.

The reorganised structure makes each piece of information displayed in the
popup easy to identify.

The popup continues to contain:

- Parking location name.
- Address.
- Postcode.
- Price.
- Verification status.
- A `View details` link.

The actual popup functionality remained unchanged.

---

### Adding Marker Coordinates to Bounds

The coordinates were originally stored using:

```javascript
bounds.push([item.lat, item.lon]);
```

This was reformatted to:

```javascript
bounds.push([
    item.lat,
    item.lon,
]);
```

#### Why this was changed

The latitude and longitude are easier to distinguish when displayed
separately.

The coordinates are later used to determine how the map should be positioned.

---

### Single Parking Result Map View

When exactly one parking result exists, the map uses:

```javascript
if (bounds.length === 1) {
    map.setView(bounds[0], 15);
}
```

#### Why this is needed

If only one parking location matches the search, there is no need to calculate
the bounds of several markers.

Instead, ParkMate centres the map directly on the matching marker and uses a
zoom level of `15`.

This provides the user with a closer view of the individual parking location.

---

### Multiple Parking Result Map View

When more than one parking marker exists, the map uses:

```javascript
if (bounds.length > 1) {
    map.fitBounds(bounds, {
        padding: [30, 30],
    });
}
```

#### Why this is needed

`fitBounds()` automatically changes the Leaflet map position and zoom so that
all matching parking locations can be seen.

The:

```javascript
padding: [30, 30]
```

option provides additional space around the markers so they do not sit
directly against the edge of the map.

---

## Additional Code Quality Improvements

Not every line changed within the template-fixing commit represented a
separate functional bug.

A number of changes were refactoring and formatting improvements completed
while correcting the template problems.

These included:

- Separating Django template statements onto individual lines.
- Separating HTML attributes across multiple lines.
- Separating Django variables from surrounding HTML.
- Separating `{% if %}`, `{% else %}` and `{% endif %}` statements.
- Separating `{% block %}` and `{% endblock %}` statements.
- Making template inheritance easier to understand.
- Making the parking search form easier to read.
- Making optional postcode logic clearer.
- Improving the structure of parking result cards.
- Improving the structure of verification badges.
- Improving the readability of the favourite button conditional.
- Improving the structure of buttons and links.
- Improving the readability of the empty-state sections.
- Clearly separating the Django content and JavaScript scripts blocks.
- Improving the formatting of Leaflet configuration.
- Separating latitude and longitude values when creating map markers.
- Reformatting marker popup content.
- Reformatting the marker bounds array.
- Adding clearer spacing between logical sections of the templates.
- Making the overall formatting more consistent across the project.

These changes did not significantly alter the intended functionality of
ParkMate.

Instead, they made the code easier to:

- Read.
- Debug.
- Maintain.
- Extend with additional features.
- Review for future errors.

---

## Bug Fix Commits

### Commit `7f567ff`

**Commit message:**

`fix: correct template syntax errors`

**Files changed:**

- `templates/base.html`
- `templates/parking/list.html`
- `templates/parking/map.html`

**Changes:**

- 237 additions.
- 66 deletions.
- Restructured Django template blocks.
- Reorganised conditional statements.
- Reformatted parking result HTML.
- Improved favourite button structure.
- Reformatted parking search elements.
- Improved parking map template structure.
- Clearly separated the content and scripts blocks.
- Reformatted Leaflet map JavaScript.
- Improved marker, popup and bounds readability.

---

### Commit `c939fc3`

**Commit message:**

`fix: correct parking filter syntax`

**File changed:**

- `templates/parking/list.html`

**Changes:**

- 1 addition.
- 1 deletion.

The incorrect comparison:

```django
{% if nation = value %}selected{% endif %}
```

was corrected to:

```django
{% if nation == value %}selected{% endif %}
```

This follow-up commit corrected the remaining nation filter syntax problem
found after the larger template restructuring.

---

## Final Result

After completing both commits, the affected ParkMate templates had a clearer
and more consistent structure.

The main results of the debugging process were:

- The parking nation filter comparison was corrected.
- Django conditional statements became easier to understand.
- Template inheritance statements were clearly separated.
- Django content blocks became easier to identify.
- Search form markup became easier to maintain.
- Parking result cards became easier to read.
- Optional postcode handling became clearer.
- Verification badge logic became easier to follow.
- Favourite button logic became easier to understand.
- Empty search states became more consistently structured.
- The parking map template became easier to maintain.
- Django parking data and JavaScript were clearly separated.
- Leaflet map code became easier to read and debug.
- Marker coordinate handling became clearer.
- Marker popup content became easier to identify.
- Single-result and multiple-result map behaviour remained intact.
- Existing ParkMate functionality was retained while the code structure was
  improved.

This debugging process also helped me distinguish between an actual bug and a
code-quality improvement.

The incorrect nation comparison was a genuine syntax issue that required a
code fix, while many of the surrounding changes were refactoring improvements
made to improve readability and reduce the likelihood of similar errors being
introduced in the future.

### Parking Form Template Syntax Error

**Bug:**

While checking my parking form page, I noticed that some of my Django template syntax was not structured correctly. The `{% block title %}` and `{% block content %}` tags were placed together on the same line and the conditional used for the form button was also split awkwardly.

This made the template harder to read and could cause template syntax errors.

**Before:**

```html
{% block title %} {% if mode == 'edit' %} Edit Parking {% else %}
Add Parking {% endif %} - ParkMate {% endblock %} {% block content %}
```

The submit button was also written as:

```html
<button class="green-button" type="submit">
    {% if mode == 'edit' %} Save Changes {% else %} Add Parking {% endif %}
</button>
```

**Fix:**

I separated the Django template blocks and made sure the conditional statements were correctly structured.

```html
{% block title %}
    {% if mode == 'edit' %}Edit Parking{% else %}Add Parking{% endif %} - ParkMate
{% endblock %}

{% block content %}
```

I also corrected the submit button:

```html
<button class="green-button" type="submit">
    {% if mode == 'edit' %}Save Changes{% else %}Add Parking{% endif %}
</button>
```

**Result:**

The parking form template is now structured correctly and is much easier to read. The same form can still be used for both adding and editing parking locations, while correctly changing the page title and button text depending on the mode.

**Commit:** `48ab04e` - `fix: correct parking form template syntax`


### Parking Detail Template Syntax Error

**Bug:**

While checking my parking detail page, I noticed that a lot of the Django template syntax and HTML had been placed together on the same lines.

For example, the template originally started with:

```html
{% extends 'base.html' %} {% load static %}
```

The title and content blocks were also placed closely together:

```html
{% block title %} {{ location.name }} - ParkMate {% endblock %}
{% block content %}
```

There were similar formatting and syntax issues throughout the page, including the parking address, postcode, verification status, save parking button, payment information and edit/delete buttons.

**Fix:**

I went through `templates/parking/detail.html` and separated the Django template tags and HTML into a clearer structure.

I changed:

```html
{% extends 'base.html' %} {% load static %}
```

To:

```html
{% extends 'base.html' %}
{% load static %}
```

I also corrected the title and content blocks:

```html
{% block title %}
    {{ location.name }} - ParkMate
{% endblock %}

{% block content %}
```

The postcode conditional was also cleaned up:

```html
<p>
    {{ location.address }}
    {% if location.postcode %}
        , {{ location.postcode }}
    {% endif %}
</p>
```

I also corrected the verification status:

```html
{% if location.council_verified %}
    <span class="verified-pill">
        ✓ Council/NPP price verified
    </span>
{% else %}
    <span class="mapped-pill">
        Mapped parking
    </span>
{% endif %}
```

The save parking conditional was also made clearer:

```html
<button class="green-button" type="submit">
    {% if is_favourite %}
        ♥ Saved
    {% else %}
        ♡ Save parking
    {% endif %}
</button>
```

I went through the rest of the page and cleaned up the:

- Back to parking link
- Parking address and postcode
- Verification labels
- Save parking form
- Parking image
- Restrictions
- Payment information
- Verification source
- Official source link
- Edit button
- Delete button
- Django `{% endif %}` and `{% endblock %}` tags

**Result:**

The parking detail template is now structured much more clearly. The Django conditionals and HTML are easier to follow and maintain, while keeping all of the existing functionality working.

This also makes it easier for me to find and fix problems in the template in the future.

**Commit:** `ca268aa` - `fix: correct parking detail template syntax`


### Parking Image Fallback Search Bug

**Bug:**

I found a problem with the parking image fallback system.

My JavaScript already checked if the parking image had no `src` or if the image source was pointing back to the current page.

The original code was:

```javascript
if (
    !image.getAttribute("src") ||
    image.src === window.location.href
) {
    await useCommons();
}
```

The problem was that if the parking location was already displaying my default `parking-fallback.svg` image, neither of these conditions were true.

This meant that the default fallback image could stay on the page without the application trying to search for a more suitable parking image.

**Fix:**

I added a new `usingFallback` check:

```javascript
const usingFallback =
    fallback &&
    image.src.endsWith("parking-fallback.svg");

if (
    !image.getAttribute("src") ||
    image.src === window.location.href ||
    usingFallback
) {
    await useCommons();
}
```

The new condition checks whether the image currently being displayed is `parking-fallback.svg`.

If the image is missing, invalid or using the default fallback image, the application will now call `useCommons()` and attempt to find a more suitable image.

**Result:**

The parking image system now recognises when the default fallback image is being used and continues the image search instead of stopping there.
This gives parking locations a better chance of displaying a relevant image while still keeping the fallback image available if another suitable image cannot be found.

**Commit:** `202fd86` - `fix: restore parking image fallback search`