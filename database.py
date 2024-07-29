from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_sql(app):
    app.logger.info("Application configuration")
    app.config['SECRET_KEY'] = "c344dd60c2c03cefd4e0aa13ea06d0cf"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def config_postgre_sql(app):
    # Configure the PostgreSQL database connection
    config_sql(app)
    app.logger.info("Configuring POSTGRESQL DB")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/database_name'
    db.init_app(app)
    return db

def create_all_db(app):
    with app.app_context():
        db.create_all()
        app.logger.info("Database created successfully")
