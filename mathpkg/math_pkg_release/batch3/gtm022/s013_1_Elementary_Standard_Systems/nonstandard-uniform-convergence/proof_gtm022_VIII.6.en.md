---
role: proof
locale: en
of_concept: nonstandard-uniform-convergence
source_book: gtm022
source_chapter: "VIII"
source_section: "6"
---

The proof is obtained by suitably modifying the argument leading to Theorem 6.13. 

For the forward direction: suppose $s_n \to r$ uniformly on $U$. The uniform convergence condition $(\forall \varepsilon > 0)(\exists n_0 \in \mathbb{N})(\forall n > n_0)(\forall x \in U)(|s_n(x) - r(x)| < \varepsilon)$ is a theorem of $\mathcal{T}(\mathcal{O}^1(\mathbb{R}))$. By transfer to $*(\mathcal{O}^1(\mathbb{R}))$, for any standard $\varepsilon > 0$, there exists $n_0 \in *\mathbb{N}$ such that for all $n > n_0$ and all $x \in *U$, $|*s_n(x) - *r(x)| < \varepsilon$. In particular, for infinite $n$, we have $n > n_0$ for any standard $n_0$, so $|*s_n(x) - *r(x)| < \varepsilon$ for all standard $\varepsilon > 0$, meaning $*s_n(x) \cong *r(x)$.

For the converse: suppose the non-standard condition holds but uniform convergence fails. Then there exists a standard $\varepsilon > 0$ such that for each $m \in \mathbb{N}$, there exist $n_m > m$ and $x_m \in U$ with $|s_{n_m}(x_m) - r(x_m)| \geq \varepsilon$. Define a function $f$ on $\mathbb{N}$ by $f(m) = n_m$. Its star extension $*f$ yields, for any infinite $m_0$, an $n = *f(m_0)$ which is infinite, and by concurrent relation arguments, a corresponding $x \in *U$ with $|*s_n(x) - *r(x)| \geq \varepsilon$, contradicting the non-standard condition.
