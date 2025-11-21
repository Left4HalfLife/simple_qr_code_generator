from flask import Flask, render_template, request, send_file
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get('data', '').strip()
    
    if not data:
        return render_template('index.html', error='Please enter text or URL')
    
    # Validate input length to prevent abuse
    if len(data) > 4096:
        return render_template('index.html', error='Input too long (max 4096 characters)')
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64 for display
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.getvalue()).decode()
    
    return render_template('index.html', qr_code=img_base64, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)
