---
role: proof
locale: en
of_concept: uniqueness-of-limit-indefinite-integral
source_book: gtm018
source_chapter: "V"
source_section: "24"
---
**Proof.** For $\epsilon > 0$, let $E_n = \{x : |f_n(x) - g_n(x)| \geq \epsilon\}$. Then $E_n \subset \{x : |f_n-f| \geq \epsilon/2\} \cup \{x : |f-g_n| \geq \epsilon/2\}$, so $\mu(E_n) \to 0$. For a measurable set $E$ of finite measure,
$$\int_E |f_n - g_n| d\mu \leq \epsilon\mu(E) + \int_{E \cap E_n} |f_n| d\mu + \int_{E \cap E_n} |g_n| d\mu.$$
The last two terms become arbitrarily small as $n \to \infty$ by uniform absolute continuity (Theorem C). Hence $\lim_n |\nu_n(E) - \lambda_n(E)| = 0$, so $\nu(E) = \lambda(E)$ for all $E$ of finite measure. By countable additivity, this extends to all measurable sets of $\sigma$-finite measure, and then to all measurable sets since simple functions have finite measure support.
