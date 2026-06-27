---
role: proof
locale: en
of_concept: godels-incompleteness-theorem
source_book: gtm022
source_chapter: "6"
source_section: "6"
---

We construct a formula $\pi(x_1, x_2)$ such that $\pi(m, n)$ is true in $\mathbb{N}$ if and only if $n = G(w(m))$ and $n$ is the Godel number of a theorem of $\mathcal{T}$. Since $\varphi(m, n) = G(w(m))$, we see that $n$ must be both the Godel number of $w(m)$ and the Godel number of a theorem. Hence $\pi(m, n)$ is true in $\mathbb{N}$ if and only if $\mathcal{T} \vdash w(m)$.

We now choose $w(x_0) = \sim \pi(x_0, x_0)$, so that $n = G(\sim \pi(x_0, x_0))$, and put $q = w(n)$. Then $\pi(n, n)$ is true in $\mathbb{N}$ if and only if $\mathcal{T} \vdash q$. But $q = \sim \pi(n, n)$, hence $\mathcal{T} \vdash q$ if and only if $q$ is false in $\mathbb{N}$. Since $\mathbb{N}$ is a model of $\mathcal{T}$, $\mathcal{T} \vdash q$ implies $q$ is true in $\mathbb{N}$. Hence $q$ cannot be a theorem of $\mathcal{T}$, which from the condition above implies $q$ is true in $\mathbb{N}$, which then implies that $\sim q$ cannot be a theorem of $\mathcal{T}$.

Thus $q = \sim \pi(n, n)$ has the property required to demonstrate the incompleteness of $\mathcal{T}$.

We note that this incompleteness cannot be cured by adding $q$ as an axiom to form a new theory $\mathcal{T}' \supseteq \mathcal{T}$, because replacing the formula defining theorem $x_3$ by a formula defining theorem $x_3'(x_3)$ in our construction provides another element $q'$ with the requisite properties. The proof shows that no effective axiomatisation of $\mathbb{N}$ can lead to a complete theory. $\square$
