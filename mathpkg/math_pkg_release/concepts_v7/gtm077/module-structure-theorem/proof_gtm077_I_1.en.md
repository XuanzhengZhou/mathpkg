---
role: proof
locale: en
of_concept: module-structure-theorem
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Theorem 2: Structure of Integer Modules

A set $M$ of integers is called a **module** (or $\mathbb{Z}$-module) if it is closed under addition and subtraction, i.e., if $m_1, m_2 \in M$ implies $m_1 \pm m_2 \in M$. It then follows that $M$ is also closed under multiplication by arbitrary integers — for any $m \in M$ and integer $t$, $t \cdot m$ can be obtained by repeated addition (or subtraction) of $m$.

**Theorem.** Every module $M$ of integers is **principal**; that is, there exists a non-negative integer $d$ such that $M$ consists precisely of all multiples of $d$:

$$M = \{d \cdot x \mid x \in \mathbb{Z}\}.$$

If $M \neq \{0\}$, then $d$ is the greatest common divisor of all (non-zero) numbers in $M$.

*Proof.* If $M = \{0\}$, then $d = 0$ works. Otherwise, $M$ contains non-zero integers; since $M$ is closed under sign change (take $m_2 = 0$, then $-m_1 \in M$), it contains positive integers. Let $d$ be the smallest positive integer in $M$.

We claim that every integer $n \in M$ is a multiple of $d$. By the division algorithm, write $n = qd + r$ with $q \in \mathbb{Z}$ and $0 \leq r < d$. Since $d \in M$ and $M$ is a module, the integer $qd$ (obtained by adding or subtracting $d$ repeatedly) belongs to $M$. Then $r = n - qd \in M$. But $0 \leq r < d$ and $d$ is the smallest positive element of $M$, so $r = 0$. Hence $n = qd$.

Conversely, every multiple $d \cdot x$ belongs to $M$ because $d \in M$ and $M$ is closed under integer multiplication.

Now let the non-zero elements of $M$ be $\{\ldots, m_{-1}, m_1, m_2, \ldots\}$. Since each $m_i$ is a multiple of $d$, we have $d \mid m_i$ for all $i$, so $d$ is a common divisor. Moreover, $d$ itself belongs to $M$, so it can be expressed as a linear combination (with integer coefficients) of the generators of $M$; any common divisor of all $m_i$ must therefore divide $d$. Hence $d$ is their greatest common divisor. $\square$

**Uniqueness.** If $d'$ is another non-negative integer such that $M$ consists of all multiples of $d'$, then $d$ must be a multiple of $d'$ (since $d \in M$) and $d'$ must be a multiple of $d$ (since $d' \in M$). Hence $d' = \pm d$; restricting to non-negative gives $d' = d$.
