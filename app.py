from api import create_app

config={
    "dev":"config.Development",
    "prod":"config.Production"
}


if __name__ == '__main__':
    app = create_app(config)
    app.run()
