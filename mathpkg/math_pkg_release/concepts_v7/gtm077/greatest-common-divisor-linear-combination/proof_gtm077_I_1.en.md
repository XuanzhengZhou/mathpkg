---
role: proof
locale: en
of_concept: greatest-common-divisor-linear-combination
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Theorem 1: Greatest Common Divisor as Linear Combination

Let $a$ and $b$ be integers, not both zero. Consider the set

$$S = \{ax + by \mid x, y \in \mathbb{Z}\}.$$

$S$ is a **module** (closed under addition and under multiplication by arbitrary integers). Let $d$ be the smallest positive integer belonging to $S$. We claim that $S$ consists precisely of all multiples of $d$.

Indeed, let $n$ be any element of $S$. By the division algorithm, write $n = qd + r$ with $0 \leq r < d$. Since $d \in S$, we have $qd \in S$ (because a module is closed under integer multiples), and therefore $r = n - qd \in S$. But $0 \leq r < d$ and $d$ is the smallest positive element of $S$, so we must have $r = 0$. Hence $n = qd$, i.e., every element of $S$ is a multiple of $d$. Conversely, every multiple of $d$ belongs to $S$ because $d \in S$ and $S$ is a module.

Now, since $a = a 