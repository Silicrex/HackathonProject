from flask_app import app, db
from flask_app.models import (User, Post, PhysicalSubmission, MentalSubmission, HazardSubmission,
                              DiversitySubmission, ResourceSubmission, MiscSubmission)


@app.shell_context_processor
def make_shell_context():  # For flask shell
    return {'db': db, 'User': User, 'Post': Post, 'PhysicalSubmission': PhysicalSubmission,
            "MentalSubmission": MentalSubmission, "HazardSubmission": HazardSubmission,
            "DiversitySubmission": DiversitySubmission, "ResourceSubmission": ResourceSubmission,
            "MiscSubmission": MiscSubmission}


if __name__ == '__main__':
    app.run(debug=True)