from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

# تعريف الكلاس هنا مباشرة بدل الاستيراد
class WebToAPKConverter:
    def __init__(self):
        self.version = "1.0.0"
        self.author = "مشروعك الشخصي"
    
    def create_android_project(self, website_url, app_name):
        """إنشاء مشروع Android"""
        
        project_data = {
            "app_name": app_name,
            "website_url": website_url,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": self.version
        }
        
        # حفظ بيانات المشروع
        with open("project_config.json", "w", encoding="utf-8") as f:
            json.dump(project_data, f, ensure_ascii=False, indent=4)
        
        return f"✅ تم إنشاء مشروع {app_name} للموقع {website_url}"
    
    def generate_apk(self):
        """توليد ملف APK"""
        return "🚀 جاري بناء ملف APK ..."

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
    app.run(debug=True, host='0.0.0.0', port=5000)
