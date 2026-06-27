---
role: proof
locale: en
of_concept: norm-multiplicativity
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 79: Multiplicativity of the Ideal Norm

For ideals $\mathfrak{a}, \mathfrak{b}$ we prove $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) N(\mathfrak{b})$.

Select an integer $\alpha$ such that $\mathfrak{a} \mid \alpha$ and
$(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$. Let $\xi_1, \ldots, \xi_{N(\mathfrak{b})}$
run through a complete residue system modulo $\mathfrak{b}$, and
$\eta_1, \ldots, \eta_{N(\mathfrak{a})}$ through a complete residue system
modulo $\mathfrak{a}$.

Consider the $N(\mathfrak{a}) N(\mathfrak{b})$ numbers $\alpha\xi_i + \eta_k$.

*Injectivity.* If $\alpha\xi_i + \eta_k \equiv \alpha\xi_{i'} + \eta_{k'}
\pmod{\mathfrak{a}\mathfrak{b}}$, then reducing modulo $\mathfrak{a}$ yields
$\eta_k \equiv \eta_{k'} \pmod{\mathfrak{a}}$, so $k = k'$. Then
$\mathfrak{a}\mathfrak{b} \mid \alpha(\xi_i - \xi_{i'})$. Since
$(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$, we deduce
$\mathfrak{b} \mid \xi_i - \xi_{i'}$, hence $i = i'$. Thus all these numbers
are pairwise incongruent modulo $\mathfrak{a}\mathfrak{b}$.

*Surjectivity.* For any integer $\rho$, first pick $\eta_k$ with
$\eta_k \equiv \rho \pmod{\mathfrak{a}}$. Then solve
$\alpha\xi \equiv \rho - \eta_k \pmod{\mathfrak{a}\mathfrak{b}}$, which is
possible by Theorem 78 since $(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$
and $\mathfrak{a} \mid \rho - \eta_k$. The solution $\xi$ can be chosen from
the residue system $\{\xi_i\}$ modulo $\mathfrak{b}$.

Therefore the numbers $\alpha\xi_i + \eta_k$ form a complete residue system
modulo $\mathfrak{a}\mathfrak{b}$, and $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) N(\mathfrak{b})$.
