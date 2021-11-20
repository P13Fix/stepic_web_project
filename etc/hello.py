def app(environ, start_response):
    status = '200 OK'
    start_response(status, [('Content-type', 'text/plain; charset=utf-8')])
    resp = "\n".join(environ.get('QUERY_STRING').split("&"))
    return resp
