import datetime
import logging

import connexion
from connexion import NoContent

import orm

db_session = None


def get_bikes(limit):
    q = db_session.query(orm.Bike)
    return [p.dump() for p in q][:limit], 200


def get_bike(bike_id):
    bike = db_session.query(orm.Bike).filter(orm.Bike.id == bike_id).one_or_none()
    return bike.dump() if bike is not None else ('Not found', 404)


def put_bike(bike_id, bike):
    p = db_session.query(orm.Bike).filter(orm.Bike.id == bike_id).one_or_none()
    bike['id'] = bike_id
    if p is not None:
        logging.info('Updating bike %s..', bike_id)
        p.update(**bike)
    else:
        logging.info('Creating bike %s..', bike_id)
        bike['created'] = datetime.datetime.utcnow()
        db_session.add(orm.Bike(**bike))
    db_session.commit()
    return NoContent, (200 if p is not None else 201)


def delete_bike(bike_id):
    bike = db_session.query(orm.Bike).filter(orm.Bike.id == bike_id).one_or_none()
    if bike is not None:
        logging.info('Deleting bike %s..', bike_id)
        db_session.query(orm.Bike).filter(orm.Bike.id == bike_id).delete()
        db_session.commit()
        return NoContent, 204
    else:
        return NoContent, 404



logging.basicConfig(level=logging.INFO)
db_session = orm.init_db('postgres://organic_almond_milk:chiaseeds@localhost:7000/bikehike')
app = connexion.FlaskApp(__name__)
app.add_api('openapi.yaml')

application = app.app

@application.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, OPTIONS"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(port=8081, use_reloader=False, threaded=False)
