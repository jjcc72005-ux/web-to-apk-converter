from flask import Flask, render_template, request, jsonify
import os
from converter import WebToAPKConverter

app = Flask(__name__)
converter = WebToAPKConverter()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_website():
    try:
        data = request.json
        website_url = data.get('url')
        app_name = data.get('app_name', 'MyWebApp')
        
        if not website_url:
            return jsonify({'error': 'يجب ادخال رابط الموقع'}), 400
        
        # استخدام الكلاس اللي عملناه
        result = converter.create_android_project(website_url, app_name)
        
        return jsonify({
            'success': True,
            'message': result,
            'app_name': app_name
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
