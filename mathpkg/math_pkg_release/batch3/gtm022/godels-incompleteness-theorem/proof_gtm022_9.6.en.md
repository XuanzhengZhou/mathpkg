---
role: proof
locale: en
of_concept: godels-incompleteness-theorem
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---

By the strong definability of recursive functions, there is a formula $\pi(x,y)$ such that $\pi(m,n)$ is true in $\mathbb{N}$ iff $n$ is the Gödel number of a formula $w(x_0)$ and $m$ is the Gödel number of a proof of $w(\overline{G(w)})$ in $\mathcal{T}$. Choose $w(x_0) = \sim \pi(x_0, x_0)$ and let $q = w(\overline{G(w)})$. Then $\mathcal{T} \vdash q$ would imply $q$ is true in $\mathbb{N}$ (since $\mathbb{N}$ is a model), but $\mathcal{T} \vdash q$ would also mean some $m$ is a proof of $q$, so $\pi(n,n)$ would be true where $n = G(w)$, contradicting $q = \sim\pi(n,n)$. Thus $\not\vdash q$. But $q$ is true in $\mathbb{N}$, so $\sim q$ is false in $\mathbb{N}$ and hence $\not\vdash \sim q$ (by soundness).
