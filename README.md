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


## Bugs and Fixes

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