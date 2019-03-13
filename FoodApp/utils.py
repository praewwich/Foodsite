def get_filename(filename):
    return filename.upper()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP')
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("remoter")
    return ip
