---
role: proof
locale: en
of_concept: norm-multiplicative-property
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 79

We prove $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) \cdot N(\mathfrak{b})$.

Pick an integer $\alpha$ with $\mathfrak{a} \mid \alpha$ and
$(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$. Let $\{\xi_i\}_{i=1}^{N(\mathfrak{b})}$
be a complete residue system modulo $\mathfrak{b}$, and
$\{\eta_k\}_{k=1}^{N(\mathfrak{a})}$ a complete residue system modulo $\mathfrak{a}$.

The $N(\mathfrak{a}) \cdot N(\mathfrak{b})$ numbers $\alpha\xi_i + \eta_k$ are
pairwise incongruent modulo $\mathfrak{a}\mathfrak{b}$, because
$\alpha\xi_i + \eta_k \equiv \alpha\xi_{i'} + \eta_{k'} \pmod{\mathfrak{a}\mathfrak{b}}$
implies $\eta_k \equiv \eta_{k'} \pmod{\mathfrak{a}}$ (reduce modulo $\mathfrak{a}$),
so $k = k'$, and then $\alpha(\xi_i - \xi_{i'}) \equiv 0 \pmod{\mathfrak{a}\mathfrak{b}}$.
With $(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$, this gives
$\mathfrak{b} \mid \xi_i - \xi_{i'}$, hence $i = i'$.

Moreover, every $\rho$ satisfies $\rho \equiv \alpha\xi_i + \eta_k \pmod{\mathfrak{a}\mathfrak{b}}$
for some $i, k$: choose $\eta_k \equiv \rho \pmod{\mathfrak{a}}$, then solve
$\alpha\xi \equiv \rho - \eta_k \pmod{\mathfrak{a}\mathfrak{b}}$ using
Theorem 78. Thus the set $\{\alpha\xi_i + \eta_k\}$ is a complete residue
system modulo $\mathfrak{a}\mathfrak{b}$ with $N(\mathfrak{a}) \cdot N(\mathfrak{b})$
elements, establishing $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) N(\mathfrak{b})$.
