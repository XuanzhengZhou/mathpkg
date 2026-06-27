---
role: proof
locale: en
of_concept: "godels-incompleteness-theorem"
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---
Proof. By Theorem 6.9, there is a strongly definable formula $\pi(x_0, x_1)$ such that $\pi(m, n)$ is true in $\mathbb{N}$ iff $n$ is the Godel number of a proof in $\mathcal{T}$ of the formula obtained by substituting the numeral for $m$ into the formula with Godel number $m$. Let $n = G(\sim\pi(x_0, x_0))$ and put $q = \sim\pi(n, n)$. Then $\pi(n, n)$ is true in $\mathbb{N}$ iff $\mathcal{T} \vdash q$. But $q = \sim\pi(n, n)$, so $\mathcal{T} \vdash q$ iff $q$ is false in $\mathbb{N}$. Since $\mathbb{N}$ is a model, $\mathcal{T} \vdash q$ implies $q$ is true. Hence $q$ is not provable, and $\sim q$ is not provable either. Adding $q$ as an axiom does not help because the construction can be iterated. $\square$
