---
role: proof
locale: en
of_concept: lcm-prime-factorization
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of LCM via Prime Factorization

Let $a$ and $b$ be positive integers. By the Fundamental Theorem of Arithmetic (Theorem 5), we can write them in terms of the same set of primes $p_1, \ldots, p_r$ by allowing zero exponents:

$$a = p_1^{a_1} p_2^{a_2} \cdots p_r^{a_r}, \qquad b = p_1^{b_1} p_2^{b_2} \cdots p_r^{b_r},$$

where $a_i, b_i \geq 0$.

**Divisibility criterion.** $b \mid a$ if and only if $b_i \leq a_i$ for all $i = 1, \ldots, r$.

*Proof.* If $b_i \leq a_i$ for all $i$, then $a/b = \prod p_i^{a_i - b_i}$ is an integer. Conversely, if $b \mid a$, then $a = bc$ for some integer $c$. By unique factorization, the prime powers in $b$ cannot exceed those in $a$, so $b_i \leq a_i$.

**GCD formula.** From the divisibility criterion, a common divisor must have exponents not exceeding $\min(a_i, b_i)$. The greatest common divisor is obtained by taking precisely these maxima:

$$(a, b) = p_1^{d_1} p_2^{d_2} \cdots p_r^{d_r}, \qquad d_i = \min(a_i, b_i).$$

**LCM formula.** Similarly, a common multiple must have exponents at least $\max(a_i, b_i)$. The least common multiple $v$ is obtained by taking precisely these minima:

$$v = \operatorname{lcm}(a, b) = p_1^{c_1} p_2^{c_2} \cdots p_r^{c_r}, \qquad c_i = \max(a_i, b_i).$$

*Proof.* Let $v$ be defined by this formula. Any common multiple $m$ of $a$ and $b$ must satisfy $\max(a_i, b_i) \leq \text{exponent of } p_i \text{ in } m$, so $v \mid m$. Thus $v$ is the least positive common multiple.

**Relation between GCD and LCM.** Since $\min(a_i, b_i) + \max(a_i, b_i) = a_i + b_i$, we have

$$(a, b) \cdot \operatorname{lcm}(a, b) = \prod p_i^{\min(a_i, b_i) + \max(a_i, b_i)} = \prod p_i^{a_i + b_i} = a \cdot b.$$

Hence $\operatorname{lcm}(a, b) = ab / (a, b)$.
