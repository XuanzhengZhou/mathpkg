---
role: proof
locale: en
of_concept: order-of-an-element
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof: Order of an Element in a Finite Group

**Theorem.** In a finite group $\mathfrak{G}$, for each element $A$, the set of exponents $q$ for which $A^q = E$ forms a module (i.e., is closed under addition and subtraction), hence consists of all multiples of a unique positive integer $a$, called the *order* of $A$. Then $A^r = E$ if and only if $a \mid r$. The order $a$ divides the group order $h$.

**Proof.** Let $S = \{q \in \mathbb{Z} : A^q = E\}$.

**Step 1: $S$ is a module.** If $q, r \in S$, then $A^{q+r} = A^q A^r = E \cdot E = E$, so $q+r \in S$. Also $A^{-q} = (A^q)^{-1} = E^{-1} = E$, so $-q \in S$. Hence $S$ is closed under addition and negation, i.e., $S$ is a submodule of $\mathbb{Z}$.

**Step 2: $S \neq \{0\}$.** Since $\mathfrak{G}$ is finite, the powers $A, A^2, A^3, \ldots$ cannot all be distinct. There exist $m > n \geq 0$ such that $A^m = A^n$. Multiplying by $A^{-n}$ yields $A^{m-n} = E$, with $m-n > 0$. Thus $S$ contains a positive integer.

**Step 3: $S = a\mathbb{Z}$ for a unique $a > 0$.** By Theorem 1 (every submodule of $\mathbb{Z}$ is a principal ideal), there exists a unique positive integer $a$ such that $S = \{ka : k \in \mathbb{Z}\}$. This $a$ is the smallest positive exponent with $A^a = E$.

**Step 4: Characterization.** $A^r = E \iff r \in S \iff a \mid r$.

**Step 5: $a \mid h$.** The powers $E, A, A^2, \ldots, A^{a-1}$ are all distinct (if $A^i = A^j$ with $0 \leq i < j < a$, then $A^{j-i} = E$, contradicting minimality of $a$) and form a subgroup of order $a$. By Lagrange's Theorem, $a \mid h$.

Thus for each element $A$, $A^h = (A^a)^{h/a} = E^{h/a} = E$. ∎
