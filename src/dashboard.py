"""Flask web dashboard for the VSOC demonstration."""
import asyncio
import threading

from flask import Flask, jsonify, render_template_string

import main

app = Flask(__name__)

DASHBOARD_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VSOC Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; background: #1a1a2e; color: #eaeaea; margin: 0; padding: 24px; }
    h1 { color: #35c9ff; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; }
    section { background: #16213e; padding: 16px; border-radius: 8px; min-width: 0; }
    h2 { margin-top: 0; color: #35c9ff; }
    .item { border-bottom: 1px solid #33456f; padding: 8px 0; overflow-wrap: anywhere; }
    .empty { color: #b7bfd3; font-style: italic; }
    .note { color: #b7bfd3; font-size: .9rem; margin-top: 24px; }
  </style>
</head>
<body>
  <h1>Virtual Security Operations Center (VSOC)</h1>
  <p>Demo dashboard showing sample logs, keyword-based detections, and simulated alerts.</p>
  <div class="grid">
    <section><h2>Logs</h2><div id="logs" class="empty">Waiting for logs…</div></section>
    <section><h2>Threats Detected</h2><div id="threats" class="empty">No threats detected</div></section>
    <section><h2>Alerts</h2><div id="alerts" class="empty">No alerts</div></section>
  </div>
  <p class="note">Educational demonstration only. Detection is keyword-based and response actions are simulated.</p>
  <script>
    function renderList(id, values, emptyText) {
      const root = document.getElementById(id);
      root.replaceChildren();
      if (!values || values.length === 0) {
        root.className = "empty";
        root.textContent = emptyText;
        return;
      }
      root.className = "";
      values.forEach(value => {
        const item = document.createElement("div");
        item.className = "item";
        item.textContent = value;
        root.appendChild(item);
      });
    }
    async function refresh() {
      try {
        const response = await fetch("/api/status");
        if (!response.ok) throw new Error("Status request failed");
        const data = await response.json();
        renderList("logs", data.logs, "No logs available");
        renderList("threats", data.threats, "No threats detected");
        renderList("alerts", data.alerts, "No alerts");
      } catch (error) {
        console.error(error);
      }
    }
    refresh();
    setInterval(refresh, 3000);
  </script>
</body>
</html>
"""


def run_monitor() -> None:
    asyncio.run(main.main())


@app.get("/")
def dashboard():
    return render_template_string(DASHBOARD_HTML)


@app.get("/api/status")
def api_status():
    return jsonify(main.shared_state)


if __name__ == "__main__":
    monitor_thread = threading.Thread(target=run_monitor, daemon=True)
    monitor_thread.start()
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
