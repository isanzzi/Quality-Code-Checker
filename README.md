# Quality Code Checker
ANTLR4

run
python main.py examples/rules.dsl examples/Sample.java

parse tree 
antlr4-parse grammar/Java20Parser.g4 grammar/Java20Lexer.g4 start_ -gui examples/Sample.java