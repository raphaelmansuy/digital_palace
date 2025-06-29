# Mastering Proof by Induction: A Comprehensive, Example-Driven Tutorial for the Impatient

## Introduction
Proof by induction is a powerful mathematical technique used to prove statements that involve natural numbers or recursively defined structures. In this tutorial, we'll dive into the world of induction, starting with the basics and progressing to advanced concepts. We'll explore various types of induction and provide plenty of practical examples to help you master this essential proof technique.

## 1. Ordinary Induction over N
Ordinary induction is the most common form of induction used to prove statements involving natural numbers. It consists of two steps:
1. Base case: Prove the statement holds for the smallest value (usually 0 or 1).
2. Inductive step: Assume the statement holds for n, and prove it holds for n+1.

### Example 1: Sum of the first n natural numbers
Let's prove that the sum of the first n natural numbers is given by the formula: $\frac{n(n+1)}{2}$.

**Proof:**
1. Base case (n=1): $\frac{1(1+1)}{2} = 1$, which is true.
2. Inductive step: Assume the formula holds for n. We'll prove it holds for n+1.
   - Sum of the first n+1 numbers = (Sum of the first n numbers) + (n+1)
   - By the inductive hypothesis: $\frac{n(n+1)}{2} + (n+1)$
   - Simplifying: $\frac{n(n+1)}{2} + \frac{2(n+1)}{2} = \frac{(n+1)(n+2)}{2}$
   - This is the formula for the sum of the first n+1 numbers, so the statement holds for n+1.

Therefore, by the principle of mathematical induction, the formula holds for all natural numbers.

### Example 2: Divisibility by 3
Prove that $3^n - 1$ is divisible by 2 for all natural numbers n.

**Proof:**
1. Base case (n=1): $3^1 - 1 = 2$, which is divisible by 2.
2. Inductive step: Assume $3^n - 1$ is divisible by 2 for some n. We'll prove that $3^{n+1} - 1$ is also divisible by 2.
   - $3^{n+1} - 1 = 3 \cdot 3^n - 1 = 3 \cdot (3^n - 1) + 2$
   - By the inductive hypothesis, $3^n - 1$ is divisible by 2, so $3 \cdot (3^n - 1)$ is also divisible by 2.
   - Adding 2 to a number divisible by 2 results in another number divisible by 2.
   - Therefore, $3^{n+1} - 1$ is divisible by 2.

By the principle of mathematical induction, $3^n - 1$ is divisible by 2 for all natural numbers n.

## 2. Two-Step Induction over N
Two-step induction is a variation of ordinary induction where the inductive step involves proving the statement for n+2 instead of n+1.

### Example 3: Fibonacci numbers
Prove that the nth Fibonacci number $F_n$ satisfies the inequality $F_n \leq 2^n$ for all n ≥ 6.

**Proof:**
1. Base cases:
   - n=6: $F_6 = 8 \leq 2^6 = 64$
   - n=7: $F_7 = 13 \leq 2^7 = 128$
2. Inductive step: Assume the inequality holds for n and n+1, where n ≥ 6. We'll prove it holds for n+2.
   - $F_{n+2} = F_n + F_{n+1}$
   - By the inductive hypothesis: $F_n \leq 2^n$ and $F_{n+1} \leq 2^{n+1}$
   - Adding the inequalities: $F_{n+2} \leq 2^n + 2^{n+1} = 2^n(1 + 2) = 3 \cdot 2^n$
   - Since n ≥ 6, we have $3 \cdot 2^n \leq 2^{n+2}$
   - Therefore, $F_{n+2} \leq 2^{n+2}$

By the principle of two-step induction, the inequality holds for all n ≥ 6.

## 3. Recursive Functions over Datatypes
Induction can also be used to prove properties of recursive functions defined over datatypes like lists and trees.

### Example 4: Length of a list
Consider a recursive function `length` that computes the length of a list:

```haskell
length :: [a] -> Int
length [] = 0
length (_:xs) = 1 + length xs
```

Prove that for any lists `xs` and `ys`, `length (xs ++ ys) = length xs + length ys`, where `++` denotes list concatenation.

**Proof:**
We'll proceed by induction on the structure of `xs`.

1. Base case (`xs = []`):
   - `length ([] ++ ys) = length ys`
   - `length [] + length ys = 0 + length ys = length ys`
2. Inductive step (`xs = x:xs'`):
   - Assume the property holds for `xs'`, i.e., `length (xs' ++ ys) = length xs' + length ys`
   - `length ((x:xs') ++ ys)`
   - `= length (x:(xs' ++ ys))` (by the definition of `++`)
   - `= 1 + length (xs' ++ ys)` (by the definition of `length`)
   - `= 1 + length xs' + length ys` (by the inductive hypothesis)
   - `= length (x:xs') + length ys` (by the definition of `length`)

Therefore, the property holds for all lists `xs` and `ys`.

## 4. Structural Induction over Datatypes
Structural induction is a generalization of induction that works on recursively defined datatypes.

### Example 5: Binary trees
Consider a datatype for binary trees:

```haskell
data Tree a = Empty | Node a (Tree a) (Tree a)
```

Prove that for any binary tree `t`, the number of nodes in `t` is always odd.

**Proof:**
We'll proceed by structural induction on `t`.

1. Base case (`t = Empty`):
   - An empty tree has 0 nodes, which is odd.
2. Inductive step (`t = Node x l r`):
   - Assume the property holds for the left subtree `l` and the right subtree `r`.
   - Let `nl` and `nr` be the number of nodes in `l` and `r`, respectively.
   - By the inductive hypothesis, `nl` and `nr` are odd.
   - The number of nodes in `t` is `1 + nl + nr`.
   - The sum of two odd numbers is even, and adding 1 to an even number results in an odd number.
   - Therefore, the number of nodes in `t` is odd.

By the principle of structural induction, the property holds for all binary trees.

## 5. Complete (Strong) Induction
Complete induction, also known as strong induction, is a variant of induction where the inductive hypothesis assumes the statement holds for all values up to n, rather than just n.

### Example 6: Postage stamps
Prove that any amount of postage of 12 cents or more can be formed using just 4-cent and 5-cent stamps.

**Proof:**
We'll use complete induction on the amount of postage.

1. Base cases:
   - 12 cents: 3 × 4-cent stamps
   - 13 cents: 2 × 4-cent stamps + 1 × 5-cent stamp
   - 14 cents: 1 × 4-cent stamp + 2 × 5-cent stamps
   - 15 cents: 3 × 5-cent stamps
2. Inductive step: Assume the statement holds for all amounts less than or equal to n, where n ≥ 15. We'll prove it holds for n+1.
   - Consider the amount n+1.
   - If we remove one 4-cent stamp, the remaining amount is n+1-4 = n-3, which is at least 12 cents.
   - By the inductive hypothesis, n-3 can be formed using 4-cent and 5-cent stamps.
   - Adding one 4-cent stamp to this formation gives the desired amount of n+1.
   - Therefore, n+1 can be formed using 4-cent and 5-cent stamps.

By the principle of complete induction, any amount of postage of 12 cents or more can be formed using just 4-cent and 5-cent stamps.

## 6. Infinite Descent
Infinite descent is a proof technique that relies on the well-ordering principle of the natural numbers. It is often used to prove statements by contradiction.

### Example 7: Irrationality of sqrt(2)
Prove that sqrt(2) is irrational using infinite descent.

**Proof:**
Assume, for contradiction, that sqrt(2) is rational. Then, there exist positive integers p and q with no common factors such that sqrt(2) = p/q.

Squaring both sides: 2 = p^2/q^2
Multiplying by q^2: 2q^2 = p^2

This implies that p^2 is even, and therefore, p must be even. Let p = 2r for some integer r.

Substituting p = 2r into the equation 2q^2 = p^2:
2q^2 = (2r)^2
2q^2 = 4r^2
q^2 = 2r^2

This implies that q^2 is even, and therefore, q must be even. But this contradicts our assumption that p and q have no common factors.

By infinite descent, we have shown that the assumption that sqrt(2) is rational leads to a contradiction. Therefore, sqrt(2) must be irrational.

## Conclusion
In this tutorial, we've explored various types of induction and provided practical examples to help you master this essential proof technique. By understanding and applying induction, you'll be well-equipped to tackle a wide range of mathematical problems and prove complex statements with ease.

Remember, the key to mastering induction is practice. Don't be afraid to experiment with different examples and challenge yourself with increasingly difficult problems. With time and dedication, you'll become a pro at proof by induction!

Happy proving!