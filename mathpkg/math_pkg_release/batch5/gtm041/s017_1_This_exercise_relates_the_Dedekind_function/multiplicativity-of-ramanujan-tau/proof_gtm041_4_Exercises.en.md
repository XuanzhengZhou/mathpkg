---
role: proof
locale: en
of_concept: multiplicativity-of-ramanujan-tau
source_book: gtm041
source_chapter: "4"
source_section: "Exercises"
---

The proof is outlined in Exercises 3 through 8 of Chapter 4, following Mordell [28]. The strategy proceeds as follows:

**Step 1 (Exercise 3).** For a prime $p$ and $1 \leq k \leq p-1$, there exists an integer $h$ such that
$$\tau^{12} \Delta\left(\frac{\tau + h}{p}\right)$$
can be expressed in terms of $\Delta(\tau)$ and related modular forms. This step uses the transformation properties of $\Delta(\tau)$ under the modular group action.

**Step 2 (Exercises 4-7).** Using the $q$-expansion and comparing coefficients, one establishes that the sum
$$\sum_{h=0}^{p-1} \Delta\left(\frac{\tau + h}{p}\right)$$
is a modular form of weight $12$ for the full modular group, and its Fourier coefficients yield relations among the $\tau(n)$.

**Step 3 (Exercise 8).** From these relations one deduces the identity
$$\tau(m)\tau(n) = \sum_{d \mid (m,n)} d^{11} \tau\left(\frac{mn}{d^2}\right).$$
The key mechanism is the action of the Hecke operator $T_p$ on the space of cusp forms of weight $12$, which is one-dimensional (spanned by $\Delta$). Therefore $\Delta$ is an eigenform for all Hecke operators, with eigenvalues $\tau(p)$. The multiplicativity then follows from the general theory of Hecke operators.

See Mordell, L. J. (1917), "On Mr. Ramanujan's empirical expansions of modular functions", *Proc. Cambridge Philos. Soc.*, 19, 117--124.
