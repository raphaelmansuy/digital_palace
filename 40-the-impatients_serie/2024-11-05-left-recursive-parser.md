## How to implement a parser

## 1. Grammar Design

First, let's define our grammar for arithmetic expressions. We need to handle basic arithmetic operations while respecting operator precedence.

### Initial Grammar (with left recursion)
```
expr    → expr + term | expr - term | term
term    → term * factor | term / factor | factor
factor  → NUMBER | ( expr )
```

## Understanding Left Recursion

Left recursion occurs when a non-terminal (let's call it A) has a production rule that starts with itself. For example:

```
A → A α | β
```

Where:
- A is the non-terminal
- α is some sequence of terminals/non-terminals (not empty)
- β is some sequence of terminals/non-terminals (could be empty, but doesn't start with A)

## Algorithm to Eliminate Left Recursion

### 1. General Method

For a left-recursive rule of the form:
```
A → A α₁ | A α₂ | ... | A αₙ | β₁ | β₂ | ... | βₘ
```

Transform it into:
```
A  → β₁ A' | β₂ A' | ... | βₘ A'
A' → α₁ A' | α₂ A' | ... | αₙ A' | ε
```

Where:
- A' is a new non-terminal
- ε represents an empty string

### 2. Practical Example with Arithmetic Expressions

Let's apply this to our arithmetic grammar:

#### Original Grammar (with left recursion):
```
expr → expr + term   | expr - term   | term
term → term * factor | term / factor | factor
factor → NUMBER | ( expr )
```

#### Step-by-Step Elimination

1. First, let's eliminate left recursion from `expr`:

Original form:
```
expr → expr + term | expr - term | term
```

Can be rewritten as:
```
expr → term expr'
expr' → + term expr' | - term expr' | ε
```

2. Similarly for `term`:

Original form:
```
term → term * factor | term / factor | factor
```

Can be rewritten as:
```
term → factor term'
term' → * factor term' | / factor term' | ε
```

#### Final Grammar (without left recursion):
```
expr  → term expr'
expr' → + term expr' | - term expr' | ε
term  → factor term'
term' → * factor term' | / factor term' | ε
factor → NUMBER | ( expr )
```

## Implementation in Python

Here's how this translates to Python code:

```python
class Node:
    """A simple tree node base class"""

    def __repr__(self):
        return self.__str__()

    def __str__(self, level=0):
        raise NotImplementedError("Subclasses should implement this!")


class NumberNode(Node):
    """A node representing a numeric value"""

    def __init__(self, value):
        try:
            self.value = float(value)
        except ValueError:
            raise ValueError(f"Invalid numeric value: {value}")

    def __str__(self, level=0):
        return "  " * level + f"{self.value}\n"


class BinaryOpNode(Node):
    """A node representing a binary operation"""

    VALID_OPERATORS = {"+", "-", "*", "/"}

    def __init__(self, left, operator, right):
        if operator not in self.VALID_OPERATORS:
            raise ValueError(f"Invalid operator: {operator}")
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self, level=0):
        result = "  " * level + f"{self.operator}\n"
        result += self.left.__str__(level + 1)
        result += self.right.__str__(level + 1)
        return result


class Parser:
    """A recursive descent parser for arithmetic expressions"""

    def __init__(self, tokens):
        if not tokens:
            raise ValueError("Empty token list")
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        """Return current token without consuming it"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        """Consume and return current token"""
        if self.pos >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        """Parse the entire expression"""
        result = self.expr()
        if self.peek() is not None:
            raise SyntaxError(f"Unexpected token at end: {self.peek()}")
        return result

    def expr(self):
        """Parse expression: expr → term expr'"""
        node = self.term()
        return self.expr_prime(node)

    def expr_prime(self, left):
        """Parse expression prime: expr' → + term expr' | - term expr' | ε"""
        if self.peek() in ["+", "-"]:
            operator = self.consume()
            right = self.term()
            new_left = BinaryOpNode(left, operator, right)
            return self.expr_prime(new_left)
        return left

    def term(self):
        """Parse term: term → factor term'"""
        node = self.factor()
        return self.term_prime(node)

    def term_prime(self, left):
        """Parse term prime: term' → * factor term' | / factor term' | ε"""
        if self.peek() in ["*", "/"]:
            operator = self.consume()
            right = self.factor()
            new_left = BinaryOpNode(left, operator, right)
            return self.term_prime(new_left)
        return left

    def factor(self):
        """Parse factor: factor → NUMBER | ( expr )"""
        token = self.peek()
        if token is None:
            raise SyntaxError("Unexpected end of input")

        if str(token).replace(".", "").isdigit():  # Handle floating point numbers
            return NumberNode(self.consume())
        elif token == "(":
            self.consume()  # consume '('
            node = self.expr()
            if self.peek() != ")":
                raise SyntaxError("Expected closing parenthesis")
            self.consume()  # consume ')'
            return node
        raise SyntaxError(f"Unexpected token: {token}")


def evaluate_ast(node):
    """Evaluate the abstract syntax tree"""
    if isinstance(node, NumberNode):
        return node.value

    if isinstance(node, BinaryOpNode):
        left = evaluate_ast(node.left)
        right = evaluate_ast(node.right)

        if node.operator == "+":
            return left + right
        if node.operator == "-":
            return left - right
        if node.operator == "*":
            return left * right
        if node.operator == "/":
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right

    raise ValueError(f"Invalid node type: {type(node)}")


# Example usage
def test_parser():
    try:
        # Test cases
        test_expressions = [
            ["5", "*", "2", "+", "41", "/", "4", "-", "7"],
            ["2", "+", "3", "*", "4"],
            ["(", "2", "+", "3", ")", "*", "4"],
        ]

        for tokens in test_expressions:
            print(f"\nParsing: {' '.join(tokens)}")
            parser = Parser(tokens)
            ast = parser.parse()
            print(f"AST: {ast}")
            result = evaluate_ast(ast)
            print(f"Result: {result}")

    except (SyntaxError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_parser()

```

## Key Points to Remember

1. **Pattern Recognition**: 
   - Original pattern: `A → A α | β`
   - Transformed pattern: `A → β A'` and `A' → α A' | ε`

2. **Recursion Direction**:
   - Left recursion: recursion at start of production
   - After transformation: recursion at end (right recursion)

3. **Implementation Benefits**:
   - Enables top-down parsing
   - Works well with recursive descent
   - Maintains operator precedence
   - Easier to implement in code

4. **Trade-offs**:
   - Introduces new non-terminals
   - May increase the size of the grammar
   - Changes the structure of the parse tree

### Example Parsing Process

For the expression "5 * 2 + 3":

1. `expr` calls `term`
2. `term` calls `factor` (gets 5)
3. `term_prime` sees '*', creates operation
4. `factor` gets 2
5. `expr_prime` sees '+', creates operation
6. `term` gets 3

Resulting AST:
```
       (+)
      /   \
    (*)    3
   /   \
  5     2
```

This transformation makes the grammar suitable for recursive descent parsing while preserving the original semantics and operator precedence.


##  👉 How to transform a "Left Recursion Free Grammar" into code

I'll explain how to transform a grammar without left recursion into Python parser methods in a didactic way.

## Step 1: Understanding the Grammar Structure

Let's start with a simple arithmetic grammar without left recursion:

```
expr → term expr'
expr' → + term expr' | - term expr' | ε
term → factor term'
term' → * factor term' | / factor term' | ε
factor → NUMBER | ( expr )
```

## Step 2: Basic Parser Class Structure

First, let's create the basic Parser class structure:

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  # List of tokens to parse
        self.pos = 0         # Current position in token list
    
    def peek(self):
        """Look at current token without consuming it"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def consume(self):
        """Consume and return current token"""
        token = self.peek()
        self.pos += 1
        return token
```

## Step 3: Transforming Grammar Rules to Methods

### Rule 1: Converting Simple Productions

For a simple rule like `factor → NUMBER | ( expr )`, we create a method that handles alternatives:

```python
def factor(self):
    """factor → NUMBER | ( expr )"""
    token = self.peek()
    
    if token.type == 'NUMBER':
        return NumberNode(self.consume())
    elif token == '(':
        self.consume()  # consume '('
        expr_node = self.expr()
        if self.peek() != ')':
            raise SyntaxError("Expected )")
        self.consume()  # consume ')'
        return expr_node
    else:
        raise SyntaxError(f"Expected number or (, got {token}")
```

### Rule 2: Converting Rules with Prime (ε alternatives)

For rules like `expr' → + term expr' | - term expr' | ε`, we create a method that handles repetition:

```python
def expr_prime(self, left):
    """expr' → + term expr' | - term expr' | ε"""
    token = self.peek()
    
    # Handle ε case (return what we have if no more operators)
    if token not in ['+', '-']:
        return left
        
    # Handle operator cases
    operator = self.consume()  # consume operator
    right = self.term()       # parse right side
    # Create new node combining left and right
    new_left = BinaryOpNode(left, operator, right)
    # Recursively handle any remaining operations
    return self.expr_prime(new_left)
```

### Rule 3: Converting Sequential Rules

For rules like `expr → term expr'`, we create a method that combines results:

```python
def expr(self):
    """expr → term expr'"""
    # First parse the term
    term_node = self.term()
    # Then handle any additional operations
    return self.expr_prime(term_node)
```

## Step 4: Complete Example

Let's see how this works with a complete example:

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        token = self.peek()
        self.pos += 1
        return token

    def parse(self):
        """Entry point for parsing"""
        return self.expr()

    def expr(self):
        """expr → term expr'"""
        term_node = self.term()
        return self.expr_prime(term_node)

    def expr_prime(self, left):
        """expr' → + term expr' | - term expr' | ε"""
        token = self.peek()
        if token not in ['+', '-']:
            return left
        
        operator = self.consume()
        right = self.term()
        new_left = BinaryOpNode(left, operator, right)
        return self.expr_prime(new_left)

    def term(self):
        """term → factor term'"""
        factor_node = self.factor()
        return self.term_prime(factor_node)

    def term_prime(self, left):
        """term' → * factor term' | / factor term' | ε"""
        token = self.peek()
        if token not in ['*', '/']:
            return left
        
        operator = self.consume()
        right = self.factor()
        new_left = BinaryOpNode(left, operator, right)
        return self.term_prime(new_left)

    def factor(self):
        """factor → NUMBER | ( expr )"""
        token = self.peek()
        
        if str(token).replace('.', '').isdigit():
            return NumberNode(self.consume())
        elif token == '(':
            self.consume()
            expr_node = self.expr()
            if self.peek() != ')':
                raise SyntaxError("Expected )")
            self.consume()
            return expr_node
        else:
            raise SyntaxError(f"Expected number or (, got {token}")
```

## Step 5: Testing the Parser

```python
# Test the parser with an expression
tokens = ["2", "+", "3", "*", "4"]
parser = Parser(tokens)
ast = parser.parse()
result = evaluate_ast(ast)
print(f"Result: {result}")  # Should print: Result: 14
```

## Key Points to Remember:

1. Each grammar rule becomes a method
2. ε (epsilon) productions become base cases in recursive methods
3. Left-hand side of rules becomes method name
4. Right-hand side becomes method implementation
5. Alternatives (|) become if/elif statements
6. Sequential rules become sequential method calls

This transformation approach ensures that the parser correctly handles operator precedence and creates an appropriate Abstract Syntax Tree (AST) for the input expression.
