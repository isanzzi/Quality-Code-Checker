import sys
from analyzer.dsl_parser import parse_dsl_file
from analyzer.java_analyzer import analyze_java_file
from analyzer.rule_evaluator import RuleEvaluator

def print_violations(violations):
    """Print violations in a formatted way"""
    if not violations:
        print("✅ No violations found!")
        return
    
    print("=" * 50)
    print("CODE QUALITY REPORT")
    print("=" * 50)
    print()
    
    errors = [v for v in violations if v['severity'] == 'error']
    warnings = [v for v in violations if v['severity'] == 'warning']
    infos = [v for v in violations if v['severity'] == 'info']
    
    for violation in errors:
        print(f"[ERROR] {violation['rule']}")
        print(f"  → Line {violation['line']}: {violation['name']}")
        print(f"  → {violation['message']}")
        print()
    
    for violation in warnings:
        print(f"[WARNING] {violation['rule']}")
        print(f"  → Line {violation['line']}: {violation['name']}")
        print(f"  → {violation['message']}")
        print()
    
    for violation in infos:
        print(f"[INFO] {violation['rule']}")
        print(f"  → Line {violation['line']}: {violation['name']}")
        print(f"  → {violation['message']}")
        print()
    
    print("=" * 50)
    print(f"Summary: {len(errors)} Error(s), {len(warnings)} Warning(s), {len(infos)} Info(s)")
    print("=" * 50)

def run_cli():
    """Run in CLI mode"""
    if len(sys.argv) < 3:
        print("Usage: python main.py <dsl_file> <java_file>")
        print("   or: python main.py --gui")
        sys.exit(1)
    
    dsl_file = sys.argv[1]
    java_file = sys.argv[2]
    
    # Parse DSL with error handling
    print(f"📖 Parsing DSL rules from: {dsl_file}")
    try:
        rules = parse_dsl_file(dsl_file)
        print(f"✅ Loaded {len(rules)} rules\n")
    except Exception as e:
        print(f"\n{str(e)}")
        print("\n💡 Please fix the DSL file and try again.")
        sys.exit(1)
    
    # Analyze Java code with error handling
    print(f"🔍 Analyzing Java code: {java_file}")
    try:
        metrics = analyze_java_file(java_file)
        print(f"✅ Found {len(metrics.methods)} functions, {len(metrics.classes)} classes, {len(metrics.variables)} variables\n")
    except FileNotFoundError:
        print(f"❌ Java file not found: {java_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error analyzing Java code: {str(e)}")
        sys.exit(1)
    
    print("⚙️  Evaluating rules...")
    evaluator = RuleEvaluator(rules, metrics)
    violations = evaluator.evaluate_all()
    print()
    
    print_violations(violations)

def run_gui():
    """Run in GUI mode"""
    from gui.main_window import main as gui_main
    gui_main()

def main():
    if len(sys.argv) >= 3 and not sys.argv[1].startswith('--'):
        run_cli()
    else:
        print("Starting GUI mode...")
        print("To use CLI mode: python main.py <dsl_file> <java_file>")
        print()
        run_gui()

if __name__ == "__main__":
    main()