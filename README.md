## ✨ Ecommcerce-app
Open-source ecommcerce app for students who wants to learn more about Flask.
<br />

> Features

- `Up-to-date dependencies`
- Database: `postgreSQL`
- `DB Tools`: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- Session-Based authentication (via **flask_login**), Forms validation

<br />

## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ # Get the code
$ git clone https://github.com/Dimand-sok/Ecommcerce-app.git
$ cd Ecommerce-app
```

<br />

> **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5000` in your browser. The app should be up & running.

<br />



## ✨ Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- api
   |    |-- app/
   |    |    |
   |    |    | home/                        # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- dao
   |    |    |  
   |    |    |  
   |    |    | 
   |    |-- migration                       # versions of migration database via alembic
   |    |    |
   |    |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |    |    |-- index.html            # Index page
   |    |    |    |-- 404-page.html         # 404 page
   |    |    |    |-- *.html                # All other pages
   |    |    |
   |    |    |
   |    |--route                         
   |    |  
   |    |__init__.py                        # Initialize the app
   |    |-- requirements.txt                # App Dependencies
   |    |-- .env                            # Inject Configuration via Environment
   |    |-- run.py                          # Start the app - WSGI gateway
   |
   |-- database
   |    |    
   |    |    
   |    |    
   |-- nginx                                #Set up web server
   |    |    
   |    |    
   |-- docker-compose.yml                   #Set up docker file
   |-- ************************************************************************
```

<br />

