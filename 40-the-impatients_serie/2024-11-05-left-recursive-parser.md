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