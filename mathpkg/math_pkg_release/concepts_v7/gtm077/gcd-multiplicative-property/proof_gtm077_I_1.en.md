---
role: proof
locale: en
of_concept: gcd-multiplicative-property
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Theorem 4: Homogeneity and Distribution of the GCD

**Part 1 (Homogeneity).** For every three integers $a, b, c$ with $c > 0$,

$$(a, b) \cdot c = (ac, bc).$$

*Proof.* Let $d = (a, b)$. Then $d \mid a$ and $d \mid b$, so $dc \mid ac$ and $dc \mid bc$; hence $dc$ is a common divisor of $ac$ and $bc$, and therefore $dc \mid (ac, bc)$.

Conversely, by Theorem 1 there exist integers $x_0, y_0$ such that $d = ax_0 + by_0$. Multiplying by $c$, we obtain

$$dc = (ac)x_0 + (bc)y_0.$$

Now $(ac, bc)$ divides every linear combination of $ac$ and $bc$, and in particular it divides the right-hand side $dc$. Hence $(ac, bc) \mid dc$.

Combining both divisibilities, we have $dc = (ac, bc)$. $\square$

**Part 2 (LCM relation).** The least common multiple $v$ of $|a|$ and $|b|$ (i.e., the smallest positive integer divisible by both $a$ and $b$) satisfies

$$v = \frac{|ab|}{(a, b)}.$$

*Proof.* Let $d = (a, b)$. Write $a = d a'$, $b = d b'$ where $(a', b') = 1$. Then any number divisible by both $a$ and $b$ must be a multiple of $d a' b' = ab/d$. Indeed, the numbers divisible by both $a$ and $b$ form a module, and the smallest positive number in it is $v$. Since $ab/d$ is divisible by $a$ (because $ab/d = a \cdot b'$ with $b'$ integer) and by $b$ (because $ab/d = b \cdot a'$), we have $v \leq ab/d$. On the other hand, $v$ is a multiple of both $a$ and $b$, say $v = ma = nb$. Then $m d a' = n d b'$, so $m a' = n b'$. Since $(a', b') = 1$, we get $b' \mid m$, hence $m = k b'$ and $v = m a = k b' a = k \cdot ab/(d)$. Thus $v \geq ab/d$. Hence $v = ab/(a, b)$. $\square$

**Part 3 (Cancellation).** If $(a, b) = 1$ and $a \mid bc$, then $a \mid c$.

*Proof.* Since $(a, b) = 1$, by Theorem 1 there exist $x, y$ with $ax + by = 1$. Multiplying by $c$: $acx + bcy = c$. Since $a \mid acx$ and $a \mid bc$ (by hypothesis), $a$ divides the sum $acx + bcy = c$. $\square$
