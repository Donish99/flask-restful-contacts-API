from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ContactModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(8), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Contact(name={name}, number={number}, year={year}'


cont_create_args = reqparse.RequestParser()
cont_create_args.add_argument('name', type=str, help='Name is required', required=True)
cont_create_args.add_argument('number', type=str, help='Number is required', required=True)
cont_create_args.add_argument('year', type=int, help='Year is required', required=True)

cont_update_args = reqparse.RequestParser()
cont_update_args.add_argument('name', type=str, help='Name is required')
cont_update_args.add_argument('number', type=str, help='Number is required')
cont_update_args.add_argument('year', type=int, help='Year is required')


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'number': fields.String,
    'year': fields.Integer
}

class All(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = ContactModel.query.order_by(ContactModel.id).all()
        return result



class Contact(Resource):
    @marshal_with(resource_fields)
    def get(self, cont_id):
        result = ContactModel.query.filter_by(id=cont_id).first()
        if not result:
            abort(404, message=f'Contact with id: {cont_id} not found')
        return result, 200

    @marshal_with(resource_fields)
    def post(self, cont_id):
        args = cont_create_args.parse_args()
        try:
            contact = ContactModel(id=cont_id, name=args['name'], number=args['number'], year=args['year'] )
            db.session.add(contact)
            db.session.commit()
            return contact, 201
        except Exception:
            abort(409, message="Id is taken try other")

    @marshal_with(resource_fields)
    def put(self, cont_id):
        args = cont_update_args.parse_args()
        result = ContactModel.query.filter_by(id=cont_id).first()
        if not result:
            abort(404, f'Contact with id: {cont_id}, not found')
        if args['name']:
            result.name = args['name']
        if args['number']:
            result.number = args['number']
        if args['year']:
            result.year = args['year']

        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, cont_id):
        result = ContactModel.query.filter_by(id=cont_id).first()
        db.session.delete(result)
        db.session.commit()
        return result


api.add_resource(Contact, '/contact/<int:cont_id>')

api.add_resource(All, '/all')


if __name__ == "__main__":
    app.run(debug=True)
