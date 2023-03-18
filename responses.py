from flask import jsonify, make_response

def responseObject(serialize_object, status=200):
    response = make_response(
        jsonify(serialize_object),
        status,
    )
    response.headers["Content-Type"] = "application/json"
    return response

def responseBadRequest():
    message = {"message": "Bad Request"}
    return responseObject (message, 400)

def responseServerError():
    message = {"message": "Server error"}
    return responseObject (message, 500)