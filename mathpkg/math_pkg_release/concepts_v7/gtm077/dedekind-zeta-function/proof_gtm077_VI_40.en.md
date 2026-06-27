---
role: proof
locale: en
of_concept: dedekind-zeta-function
source_book: gtm077
source_chapter: "VI"
source_section: "40"
---
# Proof of Theorem 123: The Dedekind Zeta Function

**Theorem 123.** $\zeta_k(s)$ is defined by the convergent series

$$\zeta_k(s) = \sum_{n=1}^{\infty} \frac{F(n)}{n^s} \tag{92}$$

for $s > 1$ as a continuous function of $s$, and as $s$ approaches 1 from above,

$$\lim_{s \to 1^+} (s - 1)\zeta_k(s) = h\varkappa.$$

Here $F(m)$ denotes the number of integral ideals of the field $k$ whose norm equals the positive integer $m$, $h$ is the class number of $k$, and $\varkappa$ is the constant from Theorem 121.

*Proof.* Let $F(m)$ be the number of integral ideals of $k$ with norm equal to $m$. By definition,

$$Z(t) = \sum_{m=1}^{t} F(m)$$

is the total number of integral ideals of $k$ with norm $\leq t$. Here $\sum_{m=1}^{t}$ means the summation index $m$ runs through all rational integers $1 \leq m \leq t$.

The function $F(m)$ is multiplicative for coprime arguments: if $(a, b) = 1$, then

$$F(ab) = F(a) \cdot F(b). \tag{89}$$

Indeed, given two integral ideals $\mathfrak{a}$ and $\mathfrak{b}$ with $N(\mathfrak{a}) = a$, $N(\mathfrak{b}) = b$, their product $\mathfrak{c} = \mathfrak{ab}$ is an integral ideal with $N(\mathfrak{c}) = ab$. Conversely, if $\mathfrak{c}$ is an integral ideal with norm $ab$, set

$$\mathfrak{a}_1 = (\mathfrak{c}, a), \quad \mathfrak{b}_1 = (\mathfrak{c}, b). \tag{90}$$

Multiplying gives $\mathfrak{a}_1 \mathfrak{b}_1 = \mathfrak{c}$. Passing to norms, $N(\mathfrak{a}_1)$ divides $a^n$ and is coprime to $b$, while $N(\mathfrak{b}_1)$ is coprime to $a$, and $N(\mathfrak{a}_1)N(\mathfrak{b}_1) = ab$. Hence $N(\mathfrak{a}_1) = a$, $N(\mathfrak{b}_1) = b$, establishing the unique decomposition and the multiplicativity of $F$.

Now, Theorem 122 (the class-independent density result) states that

$$Z(t) \sim h\varkappa t \quad \text{as } t \to \infty,$$

i.e.,

$$\lim_{t \to \infty} \frac{Z(t)}{t} = h\varkappa.$$

This follows from Theorem 121 by summing over all $h$ ideal classes, since density is the same in each class.

Viewing the coefficients $a_n = F(n)$ and setting $S(m) = \sum_{n=1}^{m} F(n) = Z(m)$, we have

$$\lim_{m \to \infty} \frac{S(m)}{m} = h\varkappa.$$

The Dirichlet series (92) defines $\zeta_k(s)$. Applying Lemma (b) with $\sigma = 1$ (since $|S(m)| < A m$ for some constant $A$, which follows from the asymptotic $S(m) \sim h\varkappa m$), the series

$$\zeta_k(s) = \sum_{n=1}^{\infty} \frac{F(n)}{n^s}$$

converges for all $s > 1$ and represents a continuous function of $s$ on $(1, \infty)$.

Applying Lemma (c) with $c = h\varkappa$, we obtain the limit relation:

$$\lim_{s \to 1^+} (s - 1)\zeta_k(s) = h\varkappa.$$

This completes the proof. $\square$
