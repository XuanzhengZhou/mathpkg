---
role: proof
locale: en
of_concept: fundamental-theorem-of-arithmetic
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Theorem 5: The Fundamental Theorem of Arithmetic

**Theorem.** Every positive integer $a > 1$ can be represented as a product of primes, and this representation is unique up to the order of the factors.

**Existence of factorization.** We proceed constructively. Let $a > 1$, and let $p_1$ be the smallest divisor of $a$ that exceeds $1$. Then $p_1$ must be prime: if $p_1$ had a proper divisor $q$ with $1 < q < p_1$, then $q$ would also divide $a$ and be smaller than $p_1$, contradicting the minimality of $p_1$.

Write $a = p_1 a_1$. If $a_1 = 1$, we are done. Otherwise $a_1 > 1$, and we repeat the process: let $p_2$ be the smallest divisor of $a_1$ exceeding $1$, so $a_1 = p_2 a_2$. Continuing, we obtain a strictly decreasing sequence of positive integers:

$$a > a_1 > a_2 > \cdots$$

Since a strictly decreasing sequence of positive integers cannot be infinite, the process must terminate after finitely many steps: some $a_k$ must equal $1$. Then

$$a = p_1 p_2 \cdots p_k$$

is the desired prime factorization.

**Uniqueness of factorization.** We first prove the key lemma:

*Lemma.* If $p$ is a prime and $p \mid ab$, then $p \mid a$ or $p \mid b$.

*Proof of the lemma.* Suppose $p \mid ab$ but $p \nmid a$. Then $(p, a) = 1$ (since the only positive divisors of $p$ are $1$ and $p$, and $p$ does not divide $a$). By Theorem 1, there exist integers $x, y$ with $px + ay = 1$. Multiplying by $b$:

$$pbx + aby = b.$$

Since $p \mid pbx$ and $p \mid ab$ (by hypothesis), $p$ divides the left-hand side, hence $p \mid b$. $\square$

Now suppose a positive integer $a$ admits two prime factorizations:

$$a = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s,$$

all $p_i, q_j$ prime. We prove by induction on $r$ that $r = s$ and the primes are the same up to order.

For $r = 1$, $a$ is prime. Then $a = q_1 q_2 \cdots q_s$. Since $a$ is prime, we must have $s = 1$ and $q_1 = a = p_1$.

Assume the statement holds for all products of fewer than $r$ primes. Consider $a = p_1 p_2 \cdots p_r = q_1 \cdots q_s$ with $r > 1$. Since $p_1$ divides the product $q_1 \cdots q_s$, the lemma (extended by induction to $s$ factors) implies that $p_1$ divides some $q_j$. Reordering the $q_j$'s, assume $p_1 \mid q_1$. Since $q_1$ is prime, $p_1 = q_1$. Cancelling $p_1 = q_1$ from both sides:

$$p_2 \cdots p_r = q_2 \cdots q_s.$$

The left-hand side has $r - 1$ factors. By the induction hypothesis, $r - 1 = s - 1$, so $r = s$, and after reordering, $p_i = q_i$ for all $i = 2, \ldots, r$. This completes the proof. $\square$
