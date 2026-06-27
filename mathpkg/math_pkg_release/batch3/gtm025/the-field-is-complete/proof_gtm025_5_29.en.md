---
role: proof
locale: en
of_concept: "the-field-is-complete"
source_book: gtm025
source_chapter: "Set Theory and Algebra"
source_section: "5.29"
---

Let $(\alpha_p)$ be any Cauchy sequence in $\bar{F}$. If $(\alpha_p)$ is ultimately constant, there is nothing to prove; if not, there exists a subsequence $(\alpha_{p_l})_{l=1}^{\infty}$ such that $\alpha_{p_l} \neq \alpha_{p_{l+1}}$ for $l=1, 2, \ldots$. By (5.26), it suffices to prove that $(\alpha_{p_l})_{l=1}^{\infty}$ has a limit. Hence we suppose with no loss of generality that $(\alpha_p)_{p=1}^{\infty}$ is such that $\alpha_p \neq \alpha_{p+1}$ ($p=1, 2, 3, \ldots$). Write $\bar{0} < |\alpha_p - \alpha_{p+1}| = \mu_p$.

For all $\varepsilon > \bar{0}$ in $\bar{F}$, there exists $N(\varepsilon)$ such that

$$|\alpha_p - \alpha_q| < \varepsilon \text{ if } p, q \geq N(\varepsilon);$$

in particular,

$$\mu_p < \varepsilon \text{ if } p \geq N(\varepsilon).$$

Using (5.28), we choose $a_p \in F$ such that $|\bar{a}_p - \alpha_p| < \mu_p$ ($p=1, 2, 3, \ldots$). Now choose any $e >
