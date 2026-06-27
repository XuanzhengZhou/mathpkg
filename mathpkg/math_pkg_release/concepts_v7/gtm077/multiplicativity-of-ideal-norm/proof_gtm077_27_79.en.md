---
role: proof
locale: en
of_concept: multiplicativity-of-ideal-norm
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 79: Multiplicativity of the Ideal Norm

We must prove $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) \cdot N(\mathfrak{b})$ for any two
ideals $\mathfrak{a}, \mathfrak{b}$.

Choose an integer $\alpha$ divisible by $\mathfrak{a}$ such that
$(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$. (Such an $\alpha$ exists
by the properties of ideal factorization.)

Let $\xi_i$ ($i = 1, 2, \ldots, N(\mathfrak{b})$) run through a complete system
of residues modulo $\mathfrak{b}$, and let $\eta_k$
($k = 1, 2, \ldots, N(\mathfrak{a})$) run through a complete system of residues
modulo $\mathfrak{a}$.

**Step 1: Distinctness.** We claim no two of the $N(\mathfrak{a}) \cdot N(\mathfrak{b})$
numbers $\alpha\xi_i + \eta_k$ are congruent modulo $\mathfrak{a}\mathfrak{b}$.
Suppose $\alpha\xi_i + \eta_k \equiv \alpha\xi_{i'} + \eta_{k'} \pmod{\mathfrak{a}\mathfrak{b}}$.
Reducing modulo $\mathfrak{a}$ (and noting that $\alpha$ is divisible by
$\mathfrak{a}$), we get $\eta_k \equiv \eta_{k'} \pmod{\mathfrak{a}}$, hence
$k = k'$ since the $\eta$'s form a complete residue system. Then
$\alpha\xi_i \equiv \alpha\xi_{i'} \pmod{\mathfrak{a}\mathfrak{b}}$, which
implies $\mathfrak{a}\mathfrak{b} \mid \alpha(\xi_i - \xi_{i'})$. Since
$(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$, we obtain
$\mathfrak{b} \mid \xi_i - \xi_{i'}$, so $i = i'$.

**Step 2: Completeness.** Every integer $\rho$ is congruent modulo
$\mathfrak{a}\mathfrak{b}$ to some $\alpha\xi_i + \eta_k$. First, determine
$\eta_k$ such that $\eta_k \equiv \rho \pmod{\mathfrak{a}}$. Then solve for
$\xi$ the congruence

$$\alpha\xi \equiv \rho - \eta_k \pmod{\mathfrak{a}\mathfrak{b}}.$$

Since $(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$ and
$\mathfrak{a} \mid \rho - \eta_k$, this congruence is solvable by Theorem 78,
and $\xi$ may be chosen from the complete residue system modulo $\mathfrak{b}$,
i.e. $\xi = \xi_i$ for some $i$.

Thus the $N(\mathfrak{a}) \cdot N(\mathfrak{b})$ numbers $\alpha\xi_i + \eta_k$
form a complete system of residues modulo $\mathfrak{a}\mathfrak{b}$. Hence
$N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) \cdot N(\mathfrak{b})$.
