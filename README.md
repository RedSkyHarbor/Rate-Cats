# Rate Cats
Randomly picks an image of a cat, vote whether or not you like this cat
[Rate some cats here](https://rate-cats.herokuapp.com/)

# Built with
[Flask](https://palletsprojects.com/p/flask/) - Python web framework

[Gunicorn](https://gunicorn.org/) - Production ready WSGI server 

[The Cat API](https://docs.thecatapi.com/) - Holds images of cats


## Installation
```bash
$ pip install -r requirements.txt
```

## Usage
```bash
$ export FLASK_APP=app/app.py
$ flask run
```

## TODO
* add favorite button, store favorite images in users cache, add another page to view favorites
* add page that retrieves most popular cat images


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for detailss
