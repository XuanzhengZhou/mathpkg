---
role: proof
locale: en
of_concept: principal-module-theorem
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Principal Module Theorem (Theorem 2)

A set $M$ of integers is called a **module** (or $\mathbb{Z}$-module) if it is closed under addition and under multiplication by arbitrary integers, i.e., if $m_1, m_2 \in M$ implies $m_1 \pm m_2 \in M$, and for any integer $t$, $t \cdot m_1 \in M$.

**Theorem.** Every module $M$ of integers is **principal**; that is, there exists a non-negative integer $d$ such that $M$ consists precisely of all multiples of $d$:

$$M = \{d \cdot x \mid x \in \mathbb{Z}\}.$$

*Proof.* If $M = \{0\}$, then $d = 0$ works. Otherwise, $M$ contains non-zero integers; since $M$ is closed under sign change, it contains positive integers. Let $d$ be the smallest positive integer in $M$.

We claim that every integer $n \in M$ is a multiple of $d$. By the division algorithm, write $n = qd + r$ with $q \in \mathbb{Z}$ and $0 \leq r < d$. Since $d \in M$ and $M$ is a module, $qd \in M$. Then $r = n - qd \in M$. But $0 \leq r < d$ and $d$ is the smallest positive element of $M$, so $r = 0$. Hence $n = qd$.

Conversely, every multiple $d \cdot x$ ($x \in \mathbb{Z}$) belongs to $M$ because $d \in M$ and $M$ is closed under integer multiplication. Thus $M = \{d \cdot x \mid x \in \mathbb{Z}\}$.

If $d'$ is another integer with the same property ($M$ equals the multiples of $d'$), then $d$ must be a multiple of $d'$ and $d'$ a multiple of $d$, so $d' = \pm d$. Hence the generator $d$ is uniquely determined up to sign.

In particular, for two integers $a, b$, the set

$$S = \{ax + by \mid x, y \in \mathbb{Z}\}$$

is a module. By the theorem, $S$ consists of all multiples of some $d \geq 0$. By Theorem 1, this $d$ is precisely the greatest common divisor $(a, b)$.
