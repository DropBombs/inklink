# This project will be a link aggregator for users to showcase all their desired links.
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
