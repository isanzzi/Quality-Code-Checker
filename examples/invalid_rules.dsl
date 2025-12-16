// Test case 1: Missing severity and message
rule "MissingAttributes" {
    target: function
    condition: parameter_count > 5
}

// Test case 2: Invalid target type
rule "InvalidTarget" {
    target: interface
    condition: parameter_count > 5
    severity: error
    message: "Too many parameters"
}

// Test case 3: Invalid severity level
rule "InvalidSeverity" {
    target: function
    condition: parameter_count > 5
    severity: critical
    message: "Too many parameters"
}
