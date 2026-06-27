---
role: proof
locale: en
of_concept: sigma-functionality-lemma
source_book: gtm037
source_chapter: "3"
source_section: "Decidable and Undecidable Theories"
---

Assume that $\sigma(x, y, z)$ and $\sigma(x, y, w)$. Let $f$ and $g$ be the functions mentioned in $\sigma(x, y, z)$ and $\sigma(x, y, w)$ respectively. Now we aim to prove

$$\operatorname{Dmn}(f \cap g, \mathbf{U} y).$$

Note that $f \cap g$ has its usual meaning, since $\mathbf{J} f$ follows from our choice of $f$. To prove (1) choose $t$ so that $\operatorname{Dmn}(f \cap g, t)$; this is possible because $\mathbf{D} f$ and $f \cap g \subseteq f$. Since $\operatorname{Dmn}(f, \mathbf{U} y)$ and $f \cap g \subseteq f$, it is clear that $t \subseteq \mathbf{U} y$. Note that $\mathbf{U} y \sim t$ has its usual meaning, since $\Omega\,\mathbf{U} y$ by 16.20. It now suffices to show that $\mathbf{U} y \sim t = 0$. Assume that $\mathbf{U} y \sim t \neq 0$. We may choose $u \in \mathbf{U} y \sim t$ so that $u \in v$ or $u = v$ for any $v \in \mathbf{U} y \sim t$. From 16.22 we infer that $\Omega u$. Clearly $0 \in t$, so $u \neq 0$. Hence by 16.23 there is an $r$ with $u = \mathbf{U} r$. Note that $\Omega r$ by 16.20.
