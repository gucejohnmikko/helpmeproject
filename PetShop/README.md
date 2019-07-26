Catalog - Petshop


Synopsis

Catalog is a basic information organizing web service with a clean and 
simple interface. It is made to demonstrate implementation of common 
concepts used in full stack projects, including:

1. persistent data storage
2. CRUD operations mapped to HTTP methods
3. third-party OAuth authentication
4. password-based login
5. RESTful API


Requirements

1. Python 2.7.x
2. VirtualBox
3. Vagrant
4. See the `requirements.txt` file for project-specific requirements.
+ Note that all the packages in the `requirement.txt` file are installed
  by the Vagrantfile when `vagrant up` is first run.


Setting Up Third-party Login

You will need to register this application with a service below to enable
the OAuth login feature. After registering, you need to obtain the necessary keys
and tokens to fill in `client_secrets` JSON files in the login directory.



Development Environment Setup

1. Install VirtualBox (See Reference section for link).
2. Install Vagrant (See Reference section for link).
3. Create a directory and name it `vagrant`.
4. Download the project repo.
5. Place the repo content inside the `vagrant` directory.


Installation & Usage

1. Open your terminal application.
2. `cd` to the vagrant directory and run `vagrant up`.
   (Installs the Linux OS and project dependencies when first run)
3. Run the following commands:
    + `vagrant ssh`  
    + `cd /vagrant`
4. Open a second terminal.
5. `cd` to the vagrant directory.
6. Repeat step 3.
7. Go back to the first terminal and run:  
    + `python petshop/database_setup.py` (do this only once)
    + `python petshop/lotsofpets.py` (do this only once)
    + `python Catalog.py`
8. Open your web browser to `http://localhost:5000/login`.



API: Request & Response Example


        http://localhost:5000/store/3/pets/JSON  

        {
  "PetsItems": [
    {
      "description": "Pomeranian", 
      "id": 13, 
      "name": "Johnson", 
      "pet_type": "Dog", 
      "price": "$2.99"
    }, 
    {
      "description": "Shit-tzu", 
      "id": 14, 
      "name": "Odette", 
      "pet_type": "Dog", 
      "price": "$5.50"
    }, 
    {
      "description": "Clownfish", 
      "id": 15, 
      "name": "Nemo", 
      "pet_type": "Fish", 
      "price": "$3.99"
    }, 
    {
      "description": "Sphynx", 
      "id": 16, 
      "name": "Jynx", 
      "pet_type": "Cat", 
      "price": "$7.99"
    }, 
    {
      "description": "Burmese Python", 
      "id": 17, 
      "name": "Rudolph", 
      "pet_type": "Reptile", 
      "price": "$1.99"
    }, 
    {
      "description": "Turtle", 
      "id": 18, 
      "name": "Spidey", 
      "pet_type": "Reptile", 
      "price": "$.99"
    }
  ]
}

