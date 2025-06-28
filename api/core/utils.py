def get_response_headers():
    return {
        "Acess-Control-Allow-headers": "Content-Type",
        "Acess-Control-Allow_Origin": "*",
        "Acess-Control-Allow_Methods": "OPTIONS,POST,GET"
    }