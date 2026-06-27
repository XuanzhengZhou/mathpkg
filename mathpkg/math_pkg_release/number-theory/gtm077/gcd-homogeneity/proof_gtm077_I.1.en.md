---
role: proof
locale: en
of_concept: gcd-homogeneity
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Homogeneity of the GCD (Theorem 4)

**Theorem.** For every three integers $a, b, c$ with $c > 0$,

$$(a, b) \cdot c = (ac, bc).$$

*Proof.* Let $d = (a, b)$. Then $d \mid a$ and $d \mid b$, so $dc \mid ac$ and $dc \mid bc$; hence $dc$ is a common divisor of $ac$ and $bc$, and therefore $dc \mid (ac, bc)$.

Conversely, write $d = ax_0 + by_0$ using Theorem 1. Multiplying by $c$, we obtain

$$dc = (ac)x_0 + (bc)y_0.$$

Now $(ac, bc)$ divides every linear combination of $ac$ and $bc$, hence $(ac, bc) \mid dc$. Since both $dc$ and $(ac, bc)$ are positive (as $c > 0$) and divide each other, they are equal:

$$(ac, bc) = dc = (a, b) \cdot c.$$

This is the homogeneity property of the GCD.

As a corollary, if $c$ is a common divisor of $a$ and $b$, then

$$\left(\frac{a}{c}, \frac{b}{c}\right) = \frac{(a, b)}{c}.$$

**Relation to the Least Common Multiple.** Let $v$ be the least common multiple (LCM) of $a$ and $b$, i.e., the smallest positive integer divisible by both $a$ and $b$. Since the numbers divisible by both $a$ and $b$ form a module, and $v$ is the smallest positive element in it, every common multiple is a multiple of $v$. Now $ab/d$ is a common multiple of $a$ and $b$, and it can be shown that $ab/d = \pm v$, i.e.,

$$\operatorname{lcm}(a, b) = \frac{|ab|}{(a, b)}.$$
