from website import create_app

app = create_app()

# only if we run this file are we going to execute this line
if __name__ == '__main__':
    app.run(debug=True)
