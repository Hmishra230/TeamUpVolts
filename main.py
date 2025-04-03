from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            input_voltage = float(request.form['input_voltage'])
            transistor_type = request.form['transistor_type']
            conductor_type = request.form['conductor_type']
            resistance = float(request.form['resistance'])
            num_turns = int(request.form['num_turns'])

            # Example calculations (simplified)
            current_output = input_voltage / resistance
            power_output = input_voltage * current_output
            inductance = 0.01 * num_turns  # Simplified formula for demonstration

            results = {
                'input_voltage': input_voltage,
                'transistor_type': transistor_type,
                'conductor_type': conductor_type,
                'resistance': resistance,
                'num_turns': num_turns,
                'current_output': round(current_output, 2),
                'power_output': round(power_output, 2),
                'inductance': round(inductance, 2)
            }
            return render_template('index.html', results=results)
        except Exception as e:
            return f"Error: {e}"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
