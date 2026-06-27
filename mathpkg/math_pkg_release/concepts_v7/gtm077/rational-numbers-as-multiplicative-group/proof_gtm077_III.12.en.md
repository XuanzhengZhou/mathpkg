---
role: proof
locale: en
of_concept: rational-numbers-as-multiplicative-group
source_book: gtm077
source_chapter: "III"
source_section: "12"
---
# Proof: Positive Rational Numbers as a Multiplicative Group

We show that $\mathfrak{M} = \mathbb{Q}_{>0}$, the set of positive rational numbers, is an infinite Abelian torsion-free group under multiplication with the primes as a basis.

**1. Group axioms under multiplication.** The positive integers alone do not form a group under multiplication, because axiom (iv) — existence of an integer $x$ with $ax = b$ — fails in general: for $a, b \in \mathbb{N}$, the equation $ax = b$ has an integer solution $x$ only if $a \mid b$. However, by including all positive rationals, this defect is remedied.

For $a, b, c \in \mathbb{Q}_{>0}$:
- $ab \in \mathbb{Q}_{>0}$ (closure);
- $a(bc) = (ab)c$ (associativity);
- $ab = ba$ (commutativity);
- $a \cdot 1 = a$ (identity element is $1$);
- For each $a = r/s$, the inverse $a^{-1} = s/r$ lies in $\mathbb{Q}_{>0}$ and satisfies $a a^{-1} = 1$.

Thus $\mathfrak{M}$ is an infinite Abelian group.

**2. Torsion-free.** If $a^n = 1$ for $a \in \mathfrak{M}$ and $n \geq 1$, write $a = p/q$ in lowest terms with $(p,q) = 1$. Then $p^n = q^n$, so $p = q$ and $a = 1$. Hence no non-identity element has finite order; $\mathfrak{M}$ is torsion-free.

**3. Basis of primes.** By the unique factorization theorem for integers, each $a \in \mathfrak{M}$ can be written as
$$a = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k},$$
where the $p_i$ are distinct positive primes and $e_i \in \mathbb{Z} \setminus \{0\}$. This representation is unique (up to reordering). In group-theoretic terms, the set of positive prime numbers forms an infinite basis of $\mathfrak{M}$: every element is a unique finite product of basis elements raised to integer exponents. The group $\mathfrak{M}$ is thus a free Abelian group of countably infinite rank.

**4. Extension by negative numbers.** If one adjoins the negative rational numbers (excluding $0$), the resulting group $\mathbb{Q}^\times$ contains the element $-1$, which has order 2: $(-1)^2 = 1$. Thus the extended group is no longer torsion-free; it acquires one element of finite order. $\square$
