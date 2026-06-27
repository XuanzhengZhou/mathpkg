---
role: proof
locale: en
of_concept: fundamental-theorem-arithmetic
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of the Fundamental Theorem of Arithmetic (Theorem 5)

**Theorem.** Every positive integer $a > 1$ can be represented as a product of primes, and this representation is unique up to the order of the factors.

**Existence.** We proceed by induction (or equivalently, by repeated splitting). Let $a > 1$. If $a$ itself is prime, we are done. Otherwise, $a$ has a proper divisor $b$ with $1 < b < a$, and consequently $a = bc$ with $1 < c < a$. By the induction hypothesis (since both $b$ and $c$ are smaller than $a$), each of $b$ and $c$ can be represented as a product of primes; multiplying these representations yields a prime factorization of $a$.

Equivalently, one may argue constructively: let $p_1$ be the smallest divisor of $a$ that exceeds $1$; then $p_1$ must be prime. Write $a = p_1 a_1$. If $a_1 > 1$, let $p_2$ be the smallest divisor of $a_1$ exceeding $1$, and so on. Since $a > a_1 > a_2 > \cdots$ is a strictly decreasing sequence of positive integers, the process terminates after finitely many steps with $a_k = 1$, yielding $a = p_1 p_2 \cdots p_k$.

**Uniqueness.** It suffices to prove the following key lemma: if $p$ is a prime and $p \mid ab$, then $p \mid a$ or $p \mid b$.

*Proof of the lemma.* Suppose $p \mid ab$ but $p \nmid a$. Then $(p, a) = 1$ (since the only positive divisors of $p$ are $1$ and $p$, and $p \nmid a$). By Theorem 1, there exist integers $x, y$ such that

$$px + ay = 1.$$

Multiplying by $b$, we obtain $pbx + aby = b$. Since $p \mid pbx$ and $p \mid ab$ (by hypothesis), it follows that $p \mid b$. This proves the lemma.

By induction, the lemma extends to: if $p \mid a_1 a_2 \cdots a_k$, then $p$ divides at least one factor $a_i$.

Now suppose

$$a = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s$$

are two prime factorizations of $a$. Since $p_1$ divides the product $q_1 q_2 \cdots q_s$, the lemma implies $p_1$ divides some $q_j$. Since $q_j$ is prime, $p_1 = q_j$. Cancelling $p_1 = q_j$ from both sides and repeating the argument, we find that each $p_i$ matches a $q_j$, and $r = s$. Thus the factorization is unique up to the order of the factors.
