from flask_restful import Resource, reqparse
from models import EmployeeModel, AddressModel, ProductModel
from flask import request
from sqlalchemy import func

class AddEmployee(Resource):
    def post(self):
        data = request.get_json(force=True)
        a = EmployeeModel(
            name=data['name'],
            email=data['email']
            )
        a.save_to_db()
        return {'message':'employee added'}


class EmployeeEdit(Resource):
    def post(self):
        data = request.get_json(force=True)
        record = EmployeeModel.query.filter_by(empid=data['empid']).first()
        if record:
            # change the values you want to update
            record.name = data['name']
            record.email = data['email']
            # commit changes
            record.save_to_db()
            EmpHistory = EmployeeModel.__history_mapper__.class_
            past_states = EmpHistory.query.filter_by(empid=record.empid).first().name
            print(past_states)
            return {"message": "Employee basic details edited successfully"}

        else:
            return {"message": "No details found"}

class AddAddress(Resource):
    def post(self):
        data = request.get_json(force=True)
        a = AddressModel(
            city=data['city'],
            state=data['state']
            )
        a.save_to_db()
        return {'message':'address added'}

class AddressEdit(Resource):
    def post(self):
        data = request.get_json(force=True)
        record = AddressModel.query.filter_by(addid=data['addid']).first()
        if record:
            # change the values you want to update
            record.city = data['city']
            record.state = data['state']
            # commit changes
            record.save_to_db()
            return {"message": "Address details edited successfully"}

        else:
            return {"message": "No details found"}

class AddProduct(Resource):
    def post(self):
        data = request.get_json(force=True)
        a = ProductModel(
            name=data['name'],
            type=data['type']
            ) 
        a.save_to_db()
        return {'message':'product added'}


class ProductEdit(Resource):
    def post(self):
        data = request.get_json(force=True)
        record = ProductModel.query.filter_by(proid=data['proid']).first()
        if record:
            # change the values you want to update
            record.name = data['name']
            record.type = data['type']
            # commit changes
            record.save_to_db()
            return {"message": "product details edited successfully"}

        else:
            return {"message": "No details found"}