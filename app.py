from website import create_app


#Open create_app function from website module
app = create_app()


if __name__ == '__main__':
    app.run()   #Initialize create_app function. This let us rerun the app without manual rerun
