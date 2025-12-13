"""
HTML Report Generator for Quality Code Checker
"""
from datetime import datetime
import os


def generate_html_report(violations, output_file):
    """Generate HTML report with interactive features"""
    
    # Count violations by severity
    errors = [v for v in violations if v['severity'] == 'error']
    warnings = [v for v in violations if v['severity'] == 'warning']
    infos = [v for v in violations if v['severity'] == 'info']
    
    # Group by file
    files_dict = {}
    for v in violations:
        file = v['file']
        if file not in files_dict:
            files_dict[file] = []
        files_dict[file].append(v)
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quality Code Checker - Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            opacity: 0.9;
            font-size: 1.1em;
        }}
        
        .summary {{
            display: flex;
            justify-content: space-around;
            padding: 30px;
            background: #f5f5f5;
            border-bottom: 3px solid #e0e0e0;
        }}
        
        .summary-card {{
            text-align: center;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            min-width: 150px;
        }}
        
        .summary-card h3 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .summary-card p {{
            color: #666;
            font-weight: bold;
        }}
        
        .error {{ color: #F44336; }}
        .warning {{ color: #FF9800; }}
        .info {{ color: #2196F3; }}
        .success {{ color: #4CAF50; }}
        
        .content {{
            padding: 30px;
        }}
        
        .filter-bar {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 8px;
        }}
        
        .filter-btn {{
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }}
        
        .filter-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        
        .filter-btn.active {{
            transform: scale(1.05);
        }}
        
        .btn-all {{ background: #9E9E9E; color: white; }}
        .btn-error {{ background: #F44336; color: white; }}
        .btn-warning {{ background: #FF9800; color: white; }}
        .btn-info {{ background: #2196F3; color: white; }}
        
        .file-section {{
            margin-bottom: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
        }}
        
        .file-header {{
            background: #2196F3;
            color: white;
            padding: 15px 20px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .file-header:hover {{
            background: #1976D2;
        }}
        
        .file-header h3 {{
            font-size: 1.2em;
        }}
        
        .badge {{
            background: rgba(255,255,255,0.3);
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.9em;
        }}
        
        .violations {{
            background: white;
        }}
        
        .violation {{
            padding: 15px 20px;
            border-bottom: 1px solid #f0f0f0;
            transition: background 0.2s;
        }}
        
        .violation:hover {{
            background: #f9f9f9;
        }}
        
        .violation:last-child {{
            border-bottom: none;
        }}
        
        .violation-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }}
        
        .violation-title {{
            font-weight: bold;
            font-size: 1.1em;
        }}
        
        .violation-line {{
            color: #666;
            font-family: monospace;
        }}
        
        .violation-message {{
            color: #555;
            margin-top: 5px;
        }}
        
        .severity-badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .severity-error {{
            background: #FFEBEE;
            color: #C62828;
        }}
        
        .severity-warning {{
            background: #FFF3E0;
            color: #EF6C00;
        }}
        
        .severity-info {{
            background: #E3F2FD;
            color: #1565C0;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            background: #f5f5f5;
            color: #666;
            border-top: 1px solid #e0e0e0;
        }}
        
        .hidden {{
            display: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Quality Code Checker</h1>
            <p>Code Analysis Report - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="summary">
            <div class="summary-card">
                <h3 class="error">{len(errors)}</h3>
                <p>Errors</p>
            </div>
            <div class="summary-card">
                <h3 class="warning">{len(warnings)}</h3>
                <p>Warnings</p>
            </div>
            <div class="summary-card">
                <h3 class="info">{len(infos)}</h3>
                <p>Info</p>
            </div>
            <div class="summary-card">
                <h3 class="success">{len(files_dict)}</h3>
                <p>Files</p>
            </div>
        </div>
        
        <div class="content">
            <div class="filter-bar">
                <button class="filter-btn btn-all active" onclick="filterViolations('all')">
                    All ({len(violations)})
                </button>
                <button class="filter-btn btn-error" onclick="filterViolations('error')">
                    Errors ({len(errors)})
                </button>
                <button class="filter-btn btn-warning" onclick="filterViolations('warning')">
                    Warnings ({len(warnings)})
                </button>
                <button class="filter-btn btn-info" onclick="filterViolations('info')">
                    Info ({len(infos)})
                </button>
            </div>
            
            <div id="violations-container">
    """
    
    # Add file sections
    for file_path, file_violations in files_dict.items():
        file_name = os.path.basename(file_path)
        violation_count = len(file_violations)
        
        html += f"""
                <div class="file-section">
                    <div class="file-header" onclick="toggleFile(this)">
                        <h3>📄 {file_name}</h3>
                        <span class="badge">{violation_count} violation(s)</span>
                    </div>
                    <div class="violations">
        """
        
        for v in file_violations:
            severity_class = f"severity-{v['severity']}"
            
            html += f"""
                        <div class="violation" data-severity="{v['severity']}">
                            <div class="violation-header">
                                <div>
                                    <span class="severity-badge {severity_class}">{v['severity']}</span>
                                    <span class="violation-title">{v['rule']}</span>
                                </div>
                                <span class="violation-line">Line {v['line']}: {v['name']}</span>
                            </div>
                            <div class="violation-message">{v['message']}</div>
                        </div>
            """
        
        html += """
                    </div>
                </div>
        """
    
    html += f"""
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Quality Code Checker</strong> - Powered by ANTLR4</p>
            <p>Total Violations: {len(violations)} | Files Analyzed: {len(files_dict)}</p>
        </div>
    </div>
    
    <script>
        function toggleFile(element) {{
            const violations = element.nextElementSibling;
            violations.style.display = violations.style.display === 'none' ? 'block' : 'none';
        }}
        
        function filterViolations(severity) {{
            // Update active button
            document.querySelectorAll('.filter-btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            event.target.classList.add('active');
            
            // Filter violations
            const violations = document.querySelectorAll('.violation');
            violations.forEach(violation => {{
                if (severity === 'all' || violation.dataset.severity === severity) {{
                    violation.style.display = 'block';
                }} else {{
                    violation.style.display = 'none';
                }}
            }});
            
            // Hide empty file sections
            document.querySelectorAll('.file-section').forEach(section => {{
                const visibleViolations = section.querySelectorAll('.violation[style="display: block;"], .violation:not([style*="display"])');
                const hasVisible = severity === 'all' || Array.from(visibleViolations).some(v => 
                    v.dataset.severity === severity
                );
                section.style.display = hasVisible ? 'block' : 'none';
            }});
        }}
    </script>
</body>
</html>
    """
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return output_file
