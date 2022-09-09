from json import dumps
from uuid import uuid4
from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from flask import json, jsonify
from entities.user import User
from .repository import repository

class Service:
    @utils.handle_service_error
    def sign_up(self, data):
        new_user = User(**data, id=uuid4())
        user = repository.get_user_by_username(data['username'])
        if user != None:
            return json.dumps({
                "status": "failed",
                "message": f"user {data['username']} already existed"
            })
        repository.add_data_flush(new_user)

        repository.commit()

        return json.dumps({
            "id": new_user.id,
            "username": new_user.username,
        })

    @utils.handle_service_error
    def sign_in(self, data):
        stdout(data)
        user = repository.get_user_by_username(data['username'])
        
        if user == None:
            return json.dumps({
                "status": "failed",
                "message": "user not existed"
            })
        if user.password != data['password']:
            return json.dumps({
                "status": "failed",
                "message": "wrong password"
            })
        else:
            return json.dumps({
                "id": user.id,
                "username": user.username,
            })

service = Service()