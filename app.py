from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
import imgkit
import os

app = Flask(__name__)

OUTPUT_DIR = "output"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

@app.route('/', methods=['GET', 'POST'])
def tip_calculator():
    if request.method == 'POST':
        try:
            bill = float(request.form['bill'])
            tip = int(request.form['tip'])
            people = int(request.form['people'])

            tip_percent = tip / 100
            tip_amount = round(bill * tip_percent, 2)
            total_bill = round(bill + tip_amount, 2)
            bill_per_person = round(total_bill / people, 2)

            details = {
                "bill": bill,
                "tip": tip,
                "tip_amount": tip_amount,
                "total_bill": total_bill,
                "people": people,
                "bill_per_person": bill_per_person
            }

            # Create PDF
            pdf_path = os.path.join(OUTPUT_DIR, "bill.pdf")
            generate_pdf(details, pdf_path)

            # Create Image
            create_image(details)

            return render_template('index.html', result=details)
        except Exception as e:
            return f"Error: {e}"

    return render_template('index.html', result=None)

def generate_pdf(details, filepath):
    c = canvas.Canvas(filepath)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, "Tip Calculator Bill Summary")
    c.drawString(100, 730, f"Total Bill: ${details['bill']}")
    c.drawString(100, 710, f"Tip Percentage: {details['tip']}%")
    c.drawString(100, 690, f"Tip Amount: ${details['tip_amount']}")
    c.drawString(100, 670, f"Total with Tip: ${details['total_bill']}")
    c.drawString(100, 650, f"Split between: {details['people']} people")
    c.drawString(100, 630, f"Each Person Pays: ${details['bill_per_person']}")
    c.save()

def create_image(details):
    html_content = f"""
    <html><body style='font-family:sans-serif;'>
    <h2>Tip Calculator Summary</h2>
    <p>Total Bill: ${details['bill']}</p>
    <p>Tip Percentage: {details['tip']}%</p>
    <p>Tip Amount: ${details['tip_amount']}</p>
    <p>Total Bill with Tip: ${details['total_bill']}</p>
    <p>Split between: {details['people']} people</p>
    <p><strong>Each Person Pays: ${details['bill_per_person']}</strong></p>
    </body></html>
    """
    img_path = os.path.join(OUTPUT_DIR, "bill_image.jpg")
    imgkit.from_string(html_content, img_path)

@app.route('/download_pdf')
def download_pdf():
    return send_file(os.path.join(OUTPUT_DIR, "bill.pdf"), as_attachment=True)

@app.route('/download_image')
def download_image():
    return send_file(os.path.join(OUTPUT_DIR, "bill_image.jpg"), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

