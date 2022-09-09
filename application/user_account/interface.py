import click
from application.share.utils import utils, print_all
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import app, user_cli_group

from .service import service

@app.route(f"{ApiGroup.USER.value}/sign-up", methods=["POST"])
# @secure.user_auth
@utils.request_with_body
# @utils.validate(SignUpDto)
def sign_up(data):
    return service.sign_up(data)

@app.route(f"{ApiGroup.USER.value}/sign-in", methods=["POST"])
# @secure.user_auth
@utils.request_with_body
# @utils.validate(SignUpDto)
def sign_in(data):
    return service.sign_in(data)
