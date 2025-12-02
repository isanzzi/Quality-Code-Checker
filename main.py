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

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <dsl_file> <java_file>")
        sys.exit(1)
    
    dsl_file = sys.argv[1]
    java_file = sys.argv[2]
    
    print(f"📖 Parsing DSL rules from: {dsl_file}")
    rules = parse_dsl_file(dsl_file)
    print(f"✅ Loaded {len(rules)} rules\n")
    
    print(f"🔍 Analyzing Java code: {java_file}")
    metrics = analyze_java_file(java_file)
    print(f"✅ Found {len(metrics.methods)} methods, {len(metrics.classes)} classes, {len(metrics.variables)} variables\n")
    
    print("⚙️  Evaluating rules...")
    evaluator = RuleEvaluator(rules, metrics)
    violations = evaluator.evaluate_all()
    print()
    
    print_violations(violations)

if __name__ == "__main__":
    main()