---
role: proof
locale: en
of_concept: nonstandard-limit-characterization
source_book: gtm022
source_chapter: "VIII"
source_section: "6"
---

Suppose $\lim_{x \to a} f(x) = \ell$ in the standard sense. Then for every standard $\varepsilon > 0$, there exists a standard $\delta > 0$ such that $|f(x) - \ell| < \varepsilon$ whenever $0 < |x - a| < \delta$. This statement is a theorem of $\mathcal{T}(\mathcal{O}^1(\mathbb{R}))$, hence holds in $*(\mathcal{O}^1(\mathbb{R}))$. If $x \in \mu(a)$ and $x \neq a$, then $0 < |x - a| < \delta$ for every standard $\delta > 0$, so $|*f(x) - \ell| < \varepsilon$ for every standard $\varepsilon > 0$, meaning $*f(x) \in \mu(\ell)$.

Conversely, suppose $*f(x) \in \mu(\ell)$ for all $x \neq a$ in $\mu(a)$. Fix a standard $\varepsilon > 0$. Let $n_0$ be an infinite natural number. Then for all $x$ with $0 < |x - a| < 1/n_0$, we have $x \in \mu(a)$ and $x \neq a$, so $|*f(x) - \ell| < \varepsilon$. Thus the statement $(\exists \delta)(\delta > 0 \wedge (\forall x)(0 < |x - a| < \delta \Rightarrow |f(x) - \ell| < \varepsilon))$, being true in $*(\mathcal{O}^1(\mathbb{R}))$, is a theorem of $\mathcal{T}(\mathcal{O}^1(\mathbb{R}))$, so it holds in $\mathbb{R}$. Hence $\lim_{x \to a} f(x) = \ell$.
