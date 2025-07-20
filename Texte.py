from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def clean_text(text):
    # Tabs und mehrere Leerzeichen zu einem einzigen ersetzen
    text = re.sub(r'\s+', ' ', text)
    # Führende und folgende Leerzeichen entfernen
    return text.strip()

@app.route('/clean', methods=['POST'])
def clean():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "❌ Kein 'text' Feld vorhanden."}), 400

    original = data['text']
    cleaned = clean_text(original)

    return jsonify({
        "original": original,
        "cleaned": cleaned
    })

if __name__ == '__main__':
    app.run(debug=True)
