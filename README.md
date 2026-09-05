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
