# Mastering First-order logic: A Comprehensive, Example-Driven Tutorial for the Impatient

## Introduction

Welcome to this comprehensive tutorial on first-order logic! If you're an impatient learner who prefers practical examples and wants to dive into advanced concepts quickly, you've come to the right place. In this tutorial, we'll cover all the essential concepts of first-order logic, starting from the basics and progressing to expert-level topics. By the end of this tutorial, you'll be proficient in first-order logic and ready to apply your knowledge to real-world problems.

## First-order languages, terms, and formulas

First-order logic is a powerful tool for reasoning about objects and their relationships. It consists of three main components: a language, terms, and formulas.

### Language

A first-order language is made up of the following elements:

- Variables: x, y, z, ...
- Constants: a, b, c, ...
- Function symbols: f, g, h, ...
- Predicate symbols: P, Q, R, ...
- Logical connectives: ∧ (and), ∨ (or), ¬ (not), → (implies), ↔ (if and only if)
- Quantifiers: ∀ (for all), ∃ (there exists)

Example:
Let's consider a first-order language for talking about family relationships:
- Variables: x, y, z
- Constants: Alice, Bob, Charlie
- Function symbols: father(x), mother(x)
- Predicate symbols: Male(x), Female(x), Parent(x, y), Sibling(x, y)

### Terms

Terms are expressions that refer to objects in the domain of discourse. They can be variables, constants, or function symbols applied to other terms.

Example:
- Variables: x, y
- Constants: Alice, Bob
- Function symbols: father(x), mother(Alice)

In this example, `father(x)` and `mother(Alice)` are terms. `father(x)` represents the father of some person `x`, while `mother(Alice)` represents the mother of Alice.

### Formulas

Formulas are statements that can be either true or false. They are built using predicate symbols, terms, logical connectives, and quantifiers.

Example:
- Atomic formulas: Male(x), Parent(Alice, Bob)
- Complex formulas: ∀x(Male(x) → ¬Female(x)), ∃y(Sibling(y, Charlie) ∧ Female(y))

In this example, `Male(x)` and `Parent(Alice, Bob)` are atomic formulas. `∀x(Male(x) → ¬Female(x))` is a complex formula stating that for all `x`, if `x` is male, then `x` is not female. `∃y(Sibling(y, Charlie) ∧ Female(y))` is another complex formula stating that there exists a `y` who is a sibling of Charlie and is female.

## Translating English to first-order formulas and vice versa

One of the essential skills in first-order logic is translating English sentences into first-order formulas and vice versa. Let's look at some more examples.

Example 1:
English: "Every person has a biological mother."
First-order formula: ∀x(Person(x) → ∃y(Mother(y, x)))

Example 2:
English: "No one is their own grandparent."
First-order formula: ∀x¬∃y(Parent(x, y) ∧ Parent(y, x))

Example 3:
First-order formula: ∃x(Teacher(x) ∧ ∀y(Student(y) → Teaches(x, y)))
English: "There exists a teacher who teaches every student."

In these examples, we see how to translate complex English sentences into first-order formulas and vice versa. It's important to identify the objects, properties, and relationships in the sentence and represent them using the appropriate symbols in the first-order language.

## First-order structures and valuations

A first-order structure is an interpretation of a first-order language. It consists of a non-empty set called the domain and an assignment of meanings to the constants, function symbols, and predicate symbols in the language.

Example:
Let's consider a first-order language with the following elements:
- Constants: Alice, Bob
- Function symbol: father(x)
- Predicate symbols: Male(x), Parent(x, y)

A possible structure for this language could be:
- Domain: {Alice, Bob, Charlie, David}
- Alice: Alice
- Bob: Bob
- father: {(Alice, Charlie), (Bob, David)}
- Male: {Charlie, David}
- Parent: {(Alice, Charlie), (Bob, David)}

In this structure, the domain consists of four individuals: Alice, Bob, Charlie, and David. The constants Alice and Bob are assigned to the corresponding individuals in the domain. The function symbol `father` is interpreted as a function that maps Alice to Charlie and Bob to David. The predicate symbols `Male` and `Parent` are interpreted as sets of individuals and pairs of individuals, respectively.

A valuation is a function that assigns values to the variables in a formula.

Example:
Given the formula Parent(x, father(y)) and the valuation v(x) = Alice, v(y) = Bob, we can determine the truth value of the formula in the given structure.

In this case, the formula evaluates to true because Alice is the parent of father(Bob), which is David according to the structure.

## Semantics of formulas

The semantics of a formula determine its meaning in a given structure under a specific valuation. We use the notation (M, v) ⊨ φ to denote that the formula φ is true in the structure M under the valuation v.

Example:
Consider the formula ∀x(Male(x) → ∃y(Parent(x, y) ∧ Female(y))) and the following structure:
- Domain: {Alice, Bob, Charlie, David}
- Male: {Charlie, David}
- Female: {Alice}
- Parent: {(Charlie, Alice), (David, Alice)}

To determine the truth value of the formula, we need to check if for every x in the domain, if x is Male, then there exists a y such that x is a Parent of y and y is Female.

In this structure, the formula is true because:
- For Charlie: Charlie is Male, and there exists Alice such that Charlie is a Parent of Alice, and Alice is Female.
- For David: David is Male, and there exists Alice such that David is a Parent of Alice, and Alice is Female.
- For Alice and Bob: The implication is trivially true since they are not Male.

## Satisfaction and validity (in a structure)

A formula is satisfiable in a structure if there exists a valuation under which the formula is true. A formula is valid in a structure if it is true under all possible valuations.

Example:
Consider the formula ∀x(P(x) → Q(x)) and the following structures:

Structure 1:
- Domain: {1, 2, 3}
- P: {1, 2}
- Q: {1, 2, 3}

Structure 2:
- Domain: {a, b, c}
- P: {a, b}
- Q: {a}

In Structure 1, the formula is valid because for every x in the domain, if P(x) holds, then Q(x) also holds.

In Structure 2, the formula is not valid because there exists an x (namely, b) for which P(x) holds but Q(x) does not hold. However, the formula is satisfiable in Structure 2 under the valuation v(x) = a.

## Logical equivalences

Two formulas are logically equivalent if they have the same truth value under all possible valuations in all structures.

Example:
The formulas ∀x(P(x) → Q(x)) and ¬∃x(P(x) ∧ ¬Q(x)) are logically equivalent.

To prove this, we can use the following logical equivalences:
- (p → q) ≡ (¬p ∨ q)
- ¬∀x(P(x)) ≡ ∃x(¬P(x))
- ¬(p ∧ q) ≡ (¬p ∨ ¬q)

Proof:
∀x(P(x) → Q(x))
≡ ∀x(¬P(x) ∨ Q(x))
≡ ¬∃x¬(¬P(x) ∨ Q(x))
≡ ¬∃x(P(x) ∧ ¬Q(x))

## Prenex formulas

A formula is in prenex normal form if all the quantifiers appear at the beginning of the formula, followed by a quantifier-free formula.

Example:
The formula ∀x∃y(P(x, y) ∧ ∀z(Q(y, z) → R(x, z))) is in prenex normal form.

To convert a formula to prenex normal form, we can use the following steps:
1. Eliminate implications (→) and equivalences (↔) using logical equivalences.
2. Move negations (¬) inward using De Morgan's laws and the equivalence ¬∀x(P(x)) ≡ ∃x(¬P(x)).
3. Rename variables to avoid name clashes.
4. Move quantifiers to the front of the formula using the equivalences:
   - (∀x(P(x)) ∧ Q) ≡ ∀x(P(x) ∧ Q), where x is not free in Q
   - (∃x(P(x)) ∨ Q) ≡ ∃x(P(x) ∨ Q), where x is not free in Q

Example:
Convert the formula ∀x(P(x) → ∃y(Q(y) ∧ R(x, y))) to prenex normal form.

Solution:
1. Eliminate implication: ∀x(¬P(x) ∨ ∃y(Q(y) ∧ R(x, y)))
2. Move negation inward: ∀x(∃y(Q(y) ∧ R(x, y)) ∨ ¬P(x))
3. No variable renaming needed.
4. Move quantifiers to the front: ∀x∃y((Q(y) ∧ R(x, y)) ∨ ¬P(x))

The resulting prenex normal form is: ∀x∃y((Q(y) ∧ R(x, y)) ∨ ¬P(x))

## Conclusion

Congratulations! You've completed this comprehensive tutorial on first-order logic. Throughout this tutorial, we've covered the essential concepts of first-order logic, including:

- First-order languages, terms, and formulas
- Translating English sentences to first-order formulas and vice versa
- First-order structures and valuations
- Semantics of formulas
- Satisfaction and validity in a structure
- Logical equivalences
- Prenex formulas

We've provided numerous examples to illustrate these concepts and help you grasp them more easily. You should now have a solid understanding of first-order logic and be well-equipped to apply your knowledge to solve real-world problems.

Remember, mastering first-order logic takes practice, so don't hesitate to work on additional exercises and explore more advanced topics on your own. With dedication and persistence, you'll soon become a proficient user of first-order logic.

Happy learning!