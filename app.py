from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-appointment', methods=['POST'])
def submit_appointment():
    data = (
        request.form['name'],
        request.form['age'],
        request.form['gender'],
        request.form['phone'],
        request.form.get('email'),
        request.form['reason'],
        request.form['date'],
        request.form['time_slot']
    )

    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (name, age, gender, phone, email, reason, date, time_slot)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

    return redirect('/')  # or render a success page

@app.route('/appointments')
def view_appointments():
    conn = sqlite3.connect('appointments.db')
    conn.row_factory = sqlite3.Row  # This lets us access columns by name
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments ORDER BY date, time_slot")
    appointments = cursor.fetchall()
    conn.close()
    return render_template('appointments.html', appointments=appointments)

@app.route('/available-slots')
def available_slots():
    date = request.args.get('date', '')
    all_slots = ["5:30 PM", "6:00 PM", "6:30 PM", "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM"]
    
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    if date:
        cursor.execute("SELECT time_slot FROM appointments WHERE date = ?", (date,))
    else:
        cursor.execute("SELECT time_slot FROM appointments")
    
    booked = {row[0].split('-')[0].strip().lower() for row in cursor.fetchall()}
    conn.close()

    slot_status = []
    for slot in all_slots:
        label = "Booked" if slot.strip().lower() in booked else "Available"
        slot_status.append(f"{slot}: {label}")

    return render_template('available_slots.html', available_slots=slot_status, date=date)



if __name__ == '__main__':
    app.run(debug=True)
