rule "TooManyParameters" {
    target: function
    condition: parameter_count > 4
    severity: error
    message: "Method {name} memiliki {parameter_count} parameter, maksimal 4"
}

rule "DeepNesting" {
    target: function
    condition: nesting_level > 3
    severity: warning
    message: "Nesting terlalu dalam di method {name}"
}

rule "TooManyVariables" {
    target: function
    condition: local_variable_count > 8
    severity: warning
    message: "Method {name} memiliki {local_variable_count} variabel, maksimal 8"
}

rule "VariableNameTooShort" {
    target: variable
    condition: name_length < 5
    severity: info
    message: "Nama variable {name} terlalu pendek, minimal 5 karakter"
}

rule "TooManyMethodCalls" {
    target: function
    condition: method_call_count > 3
    severity: warning
    message: "Method {name} memanggil {method_call_count} method lain, maksimal 3"
}