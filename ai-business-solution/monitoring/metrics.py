from prometheus_client import Summary, start_http_server

request_time = Summary('request_processing_seconds', 'Time spent processing request')

def start_monitoring():
    start_http_server(8000)
