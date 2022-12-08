from app import build_app

myapp = build_app()

if __name__ == "__main__":
    myapp.run(debug=True, host='localhost')
