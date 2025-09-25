from flask import Flask, render_template, redirect, url_for, flash
import ansible_runner
import psutil
import threading
import time
import subprocess

app = Flask(__name__)
app.secret_key = "supersecretkey"

CPU_THRESHOLD = 50
CHECK_INTERVAL = 5
monitoring = True
cpu_status = 0  # Track current CPU usage

# Function to run Ansible playbook
def run_playbook():
    r = ansible_runner.run(private_data_dir='.', playbook='cpu_alert.yml')
    return r.status, r.rc

# CPU monitoring thread
def cpu_monitor():
    global cpu_status
    while monitoring:
        cpu_status = psutil.cpu_percent(interval=1)
        if cpu_status > CPU_THRESHOLD:
            print("⚡ High CPU detected, running playbook automatically...")
            status, rc = run_playbook()
            print(f"Playbook finished with status: {status}, rc: {rc}")
        time.sleep(CHECK_INTERVAL)

threading.Thread(target=cpu_monitor, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html", cpu_status=cpu_status)

@app.route("/run-playbook")
def trigger_playbook():
    status, rc = run_playbook()
    flash(f"Playbook executed! Status: {status}, rc: {rc}")
    return redirect(url_for('index'))

@app.route("/simulate-high-cpu")
def simulate_cpu():
    subprocess.Popen(["stress", "--cpu", "2", "--timeout", "10"])
    flash("⚡ Simulated high CPU scenario using stress command.")
    return redirect(url_for('index'))

@app.route("/kill-stress")
def kill_stress():
    subprocess.Popen(["pkill", "-f", "stress"])
    flash("Stress process killed (if running).")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
