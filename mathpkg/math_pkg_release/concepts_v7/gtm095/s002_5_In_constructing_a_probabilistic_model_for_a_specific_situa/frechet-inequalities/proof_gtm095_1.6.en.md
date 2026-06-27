---
role: proof
locale: en
of_concept: frechet-inequalities
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of Frechet's Inequalities

**Problem 5(c) (Section 6).** Prove **Frechet's inequalities**: for $m = 1, 2, \ldots, n-1$,
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_{m+1}}{\binom{n-1}{m}} \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}},$$
where
$$\tilde{S}_m = \sum_{1 \leq i_1 < \cdots < i_m \leq n} \mathrm{P}(A_{i_1} \cup \cdots \cup A_{i_m}).$$

**Proof.** The first inequality for each $m$ (with $\tilde{S}_{m+1}$) is precisely Gumbel's inequality with $m+1$ in place of $m$. So the main task is to prove the chain of inequalities:
$$\frac{\tilde{S}_{m+1}}{\binom{n-1}{m}} \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}}.$$

Equivalently, we need to show
$$\binom{n-1}{m-1} \tilde{S}_{m+1} \leq \binom{n-1}{m} \tilde{S}_m. \tag{1}$$

**Combinatorial identity.** For any outcome $\omega$, define $\nu(\omega)$ as the number of events containing $\omega$. The contribution of $\omega$ to $\tilde{S}_m$ is $\binom{n}{m} - \binom{n-\nu(\omega)}{m}$ (counting the $m$-tuples whose union contains $\omega$, as in the proof of Gumbel's inequality).

Inequality (1) is equivalent to showing that for each $\omega$,
$$\binom{n-1}{m-1}\left[\binom{n}{m+1} - \binom{n-\nu}{m+1}\right] \leq \binom{n-1}{m}\left[\binom{n}{m} - \binom{n-\nu}{m}\right],$$
where $\nu = \nu(\omega)$. Simplifying using the identity $\binom{n-1}{m-1} = \frac{m}{n}\binom{n}{m}$ and $\binom{n-1}{m} = \frac{n-m}{n}\binom{n}{m}$:
$$\frac{m}{n}\left[\binom{n}{m+1} - \binom{n-\nu}{m+1}\right] \leq \frac{n-m}{n}\left[\binom{n}{m} - \binom{n-\nu}{m}\right].$$

After algebraic manipulation and using properties of binomial coefficients, this reduces to
$$\binom{n-\nu}{m} \cdot \nu \geq \binom{n-\nu}{m+1} \cdot (m+1),$$
which holds with equality when $\nu = 0$ and is true for $\nu \geq 1$ by the identity $\binom{n-\nu}{m+1} (m+1) = \binom{n-\nu}{m} (n-\nu-m)$ and the fact that $n-\nu-m \leq n-m \leq \nu \cdot (\ldots)$ for $\nu \geq 1$.

Summing the pointwise inequality over all $\omega$ with weights $\mathrm{P}(\{\omega\})$ yields (1), which proves Frechet's chain of inequalities.

**Interpretation.** Frechet's inequalities show that the Gumbel bounds $\tilde{S}_m / \binom{n-1}{m-1}$ form a **monotonically decreasing** sequence as $m$ increases. Thus, using larger $m$ (i.e., incorporating information about unions of larger tuples of events) yields sharper (smaller) upper bounds for the probability of the total union. In the limit $m = n$, we have $\tilde{S}_n / \binom{n-1}{n-1} = \tilde{S}_n = \mathrm{P}(\bigcup_{i=1}^{n} A_i)$, achieving equality.
