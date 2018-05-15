# Coffee Cart Application

This Coffee Cart Application serves as an interface for a potential manager of a coffee cart. This application helps keep inventory of drinks, snacks, ingredients, and recommended sides. The user can:

- Create a new drink or snack and add it to the menu
- Click on a drink or snack in the menu and view a new page that displays the features of the product
- View a list of all drinks and snacks available at the coffee cart
- Modify an existing drink or snack on the menu
- Remove a drink or snack from the menu

Each drink feature has:
- A name
- A basic list of ingredients (example: espresso, milk, and vanilla flavor)
- A list of recommended snacks from the menu that pair well with the drink

Each snack feature has:
- A name
- A basic list of ingredients (example: chocolate, nuts)
- A list of recommended drinks from the menu that pair well with the snack

## Getting Started

Install Python and Django.

### Installing


- From coffeecart directory run python(3) manage.py createsuperuser and input credentials as asked
- From coffeecart directory run python(3) manage.py makemigrations
- From coffeecart directory run python(3) manage.py migrate


## Deployment

- From coffeecart directory run python(3) manage.py runserver
- Type http://localhost:8000/admin in your browser to use application and log in to your user using credentials that were made in the steps above

Type http://localhost:8000/cart/ in your browser to use the application

## Author

* **Dennys Morales**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

