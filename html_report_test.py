import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# Verilerinizi yükleyin
with open('./data/data.json') as f:
    data = json.load(f)

# Jinja2 ortamını ve şablon dosyasını ayarlayın
env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('report_template.html')

# Şablona verilerinizi geçin
rendered_html = template.render(date=datetime.now().strftime("%Y-%m-%d"), people=data)

# Render edilmiş HTML'yi bir dosyaya kaydedin
with open('./report/report.html', 'w') as f:
    f.write(rendered_html)

print("Rapor oluşturuldu: report.html")