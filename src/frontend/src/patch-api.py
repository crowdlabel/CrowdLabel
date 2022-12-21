source_path = 'crowdlabel-api/src/ApiClient.js'

with open(source_path) as f:
    source = f.read()

source = source.replace("if (returnType === 'Blob')", "if (returnType === 'Blob' || returnType === Object)")


default_headers = """    this.defaultHeaders = {
            'User-Agent': 'OpenAPI-Generator/0.1.0/Javascript'
        };"""
source = source.replace(default_headers, '/*' + default_headers.strip() + '*/')

set_headers = '    request.set(this.defaultHeaders)'
source = source.replace(set_headers, '//' + set_headers.strip())

with open(source_path, 'w') as f:
    f.write(source)