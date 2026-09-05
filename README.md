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

| Technology | Use in ParkMate |
| --- | --- |
| Python 3.13.15 | Runs the backend Python code |
| Django 5.2.17 | Provides routing, templates, authentication, forms, validation and database functionality |
| HTML | Structures the website pages |
| CSS | Controls the appearance and responsive layouts |
| JavaScript | Controls interactive map behaviour and parking image loading |
| SQLite | Used as the local development database |
| PostgreSQL | Supported as the production database |
| Django ORM | Handles database queries and relationships |
| Leaflet | Displays the interactive parking map |
| OpenStreetMap | Provides the map tiles |
| Wikimedia Commons API | Attempts to find relevant parking and location images |
| WhiteNoise | Serves static files in production |
| Gunicorn | Runs the Django application in production |
| dj-database-url | Reads the production database connection |
| Heroku | Used as the intended deployment platform |
| Git | Tracks changes made during development |
| GitHub | Stores the project repository and commit history |


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

| Research Finding | Evidence Source | ParkMate Response |
| --- | --- | --- |
| Drivers may search using a location, postcode or parking name. | Medway Council Car Park Directory | ParkMate supports location, postcode and parking-name searching. |
| Official parking pages provide prices and charging information. | Lewisham Council Car Parks | ParkMate stores tariff information, charging times and official source details. |
| Parking restrictions depend on signs and operating conditions. | GOV.UK Highway Code - Waiting and Parking | Parking detail pages contain restriction information and users are reminded that mapped information can change. |
| Drivers benefit from having parking information in one place. | GOV.UK Plan for Drivers | ParkMate brings different parking information together in one application. |
| Interactive maps help users understand where a location is. | Leaflet Documentation | ParkMate uses a Leaflet map with OpenStreetMap tiles. |


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