def response_generator(status_code: int, message: str, content_name=None, content=None) -> dict:
    response = {
        'status_code': status_code,
        'message': message,
    }
    if content_name:
        response.update({content_name: content})
    return response
