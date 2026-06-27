---
role: proof
locale: en
of_concept: linear-congruence-mod-ideal
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 78: Linear Congruences modulo an Ideal

We must show that $\alpha\xi \equiv \beta \pmod{\mathfrak{a}}$ has an integer
solution $\xi$ in $K$ if and only if $(\alpha, \mathfrak{a}) \mid \beta$, and
that when $(\alpha, \mathfrak{a}) = 1$, the solution is unique modulo $\mathfrak{a}$.

**Case 1:** $(\alpha, \mathfrak{a}) = 1$.

Let $\xi$ run through a complete system of $N(\mathfrak{a})$ residues modulo
$\mathfrak{a}$. If $\alpha\xi_1 \equiv \alpha\xi_2 \pmod{\mathfrak{a}}$, then
$\mathfrak{a} \mid \alpha(\xi_1 - \xi_2)$. Since $(\alpha, \mathfrak{a}) = 1$,
the Fundamental Theorem of ideal theory implies
$\mathfrak{a} \mid \xi_1 - \xi_2$, i.e. $\xi_1 \equiv \xi_2 \pmod{\mathfrak{a}}$.
Thus the mapping $\xi \mapsto \alpha\xi$ is injective on the residue classes
modulo $\mathfrak{a}$, and since there are only $N(\mathfrak{a})$ residue
classes, it must be bijective. Consequently, among the numbers $\alpha\xi$,
exactly one lies in the residue class of $\beta$. The solution is uniquely
determined modulo $\mathfrak{a}$.

**Case 2:** $(\alpha, \mathfrak{a}) = \mathfrak{d}$ in general.

Suppose there exists $\xi_0$ with $\alpha\xi_0 \equiv \beta \pmod{\mathfrak{a}}$.
Then $\alpha\xi_0 = \beta + \rho$ with $\mathfrak{a} \mid \rho$. Hence
$\mathfrak{d} \mid \rho$, and $\mathfrak{d} \mid \alpha\xi_0 - \rho = \beta$,
so $\mathfrak{d} \mid \beta$, i.e. $(\alpha, \mathfrak{a}) \mid \beta$.

Conversely, if $(\alpha, \mathfrak{a}) \mid \beta$, write
$\mathfrak{d} = (\alpha, \mathfrak{a})$. By choosing $\lambda, \mu$ such that
$\lambda\alpha + \mu\mathfrak{a} = \mathfrak{d}$ (in the sense of ideal GCD),
and using the fact that $\mathfrak{d} \mid \beta$, one reduces to the case
$(\alpha/\mathfrak{d}, \mathfrak{a}/\mathfrak{d}) = 1$ and applies Case 1. This
completes the proof.
