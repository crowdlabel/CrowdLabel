async function fetch_json(url, method, data = {}) {
    const response = await fetch(url, {
        method: method,
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    return response.json();
}

async function send_file(url, method, data, file) {
    let form_data = new FormData();
    form_data.append('file', file);
    form_data.append('data', JSON.stringify(data));

    let response = await fetch(url, {
        method: method,
        body: form_data,
    });
    return response;
}