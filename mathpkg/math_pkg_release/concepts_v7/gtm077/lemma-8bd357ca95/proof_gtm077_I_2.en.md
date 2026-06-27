---
role: proof
locale: en
of_concept: lemma-8bd357ca95
source_book: gtm077
source_chapter: "I"
source_section: "2"
---

# Proof of Lemma: Multiplicativity of Euler's Totient Function

**Lemma.** If $(a, b) = 1$, then $\varphi(ab) = \varphi(a) \varphi(b)$.

*Proof.* By Theorem 8, since $a$ and $b$ are coprime, a complete residue system modulo $ab$ can be written in the form

$$L(x, y) = \frac{ab}{a} \cdot c_1 \cdot x + \frac{ab}{b} \cdot c_2 \cdot y = b c_1 x + a c_2 y,$$

where $x$ runs through a complete residue system modulo $b$ and $y$ runs through a complete residue system modulo $a$. The constants $c_1, c_2$ are integers satisfying $(c_1, a) = 1$ and $(c_2, b) = 1$.

We may simplify by choosing $c_1$ and $c_2$ such that $b c_1 \equiv 1 \pmod{a}$ and $a c_2 \equiv 1 \pmod{b}$ (possible since $(b, a) = 1$ and $(a, b) = 1$). With this choice, the representation simplifies further, and the linear form becomes essentially

$$L(x, y) = a x + b y,$$

which, as $x$ runs through residues modulo $b$ and $y$ through residues modulo $a$, yields a complete residue system modulo $ab$ (a standard form of the Chinese Remainder Theorem).

Now, $\varphi(ab)$ counts the number of residue classes modulo $ab$ that are relatively prime to $ab$. A residue class modulo $ab$ is relatively prime to $ab$ if and only if it is relatively prime to $a$ and also relatively prime to $b$ (since $a$ and $b$ are coprime).

For the representative $a x + b y$, being coprime to $ab$ means:

$$(a x + b y, a b) = 1.$$

Since $(a, b) = 1$, this is equivalent to the two conditions:

$$(a x + b y, a) = 1 \quad \text{and} \quad (a x + b y, b) = 1.$$

Now $(a x + b y, a) = (b y, a) = (y, a)$ because $(b, a) = 1$. Similarly, $(a x + b y, b) = (a x, b) = (x, b)$ because $(a, b) = 1$.

Therefore, $a x + b y$ is relatively prime to $ab$ if and only if $(x, b) = 1$ and $(y, a) = 1$.

The number of choices for $x$ with $(x, b) = 1$ among a complete residue system modulo $b$ is precisely $\varphi(b)$. The number of choices for $y$ with $(y, a) = 1$ among a complete residue system modulo $a$ is $\varphi(a)$. Since $x$ and $y$ vary independently, the total number of such pairs is $\varphi(a) \cdot \varphi(b)$. Hence

$$\varphi(ab) = \varphi(a) \varphi(b).$$

$\square$

**Corollary.** By repeated application of the Lemma, if $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_r^{\alpha_r}$ is the prime factorization of $n$, then

$$\varphi(n) = \prod_{i=1}^{r} \varphi(p_i^{\alpha_i}) = \prod_{i=1}^{r} p_i^{\alpha_i} \left(1 - \frac{1}{p_i}\right) = n \prod_{i=1}^{r} \left(1 - \frac{1}{p_i}\right).$$

For a prime power $p^k$, we have $\varphi(p^k) = p^k - p^{k-1} = p^k(1 - 1/p)$, since among the numbers $1, 2, \ldots, p^k$, exactly $p^{k-1}$ are multiples of $p$.
