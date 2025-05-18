from app import app, request, jsonify, send_file
import models
from utils import download_utils

@app.route('/api')
def send_request():
    url = request.args.get('url')
    format = request.args.get('format')
    reso = request.args.get('reso')

    model = models.url_model.Urls(url, format, reso)
    res = model.get_info()

    return jsonify(res)

@app.route('/download/<uuid>')
def download_from_uuid(uuid):
    file_path = download_utils.get_file_path_from_uuid(uuid)
    return send_file(file_path, as_attachment=True)
