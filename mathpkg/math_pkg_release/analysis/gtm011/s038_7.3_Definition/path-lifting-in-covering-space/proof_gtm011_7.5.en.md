---
role: proof
locale: en
of_concept: path-lifting-in-covering-space
source_book: gtm011
source_chapter: "7"
source_section: "7.5"
---

Define $F: [0, 1] \times [0, 1] \rightarrow \Omega$ by $F(s, t) = \gamma(s)$; so $F$ is continuous and $F(0, 0) = \omega_0$. According to Theorem 7.4 there is a unique function $\tilde{F}: [0, 1] \times [0, 1] \rightarrow X$ such that $\tilde{F}(0, 0) = x_0$ and $\rho \circ \tilde{F} = F$. Let $\tilde{\gamma}(s) = \tilde{F}(s, 0)$; then $\tilde{\gamma}$ has initial point $x_0$ and is a lifting of $\gamma$. To prove the uniqueness of $\tilde{\gamma}$, suppose $\tilde{\sigma}$ is also a path in $X$ with initial point $x_0$ and which lifts $\gamma$. Define $\tilde{K}: [0, 1] \times [0, 1] \rightarrow X$ by $\tilde{K}(s, t) = \tilde{\sigma}(s)$. Then $\tilde{K}(0, 0) = x_0$ and $\rho \circ \tilde{K}(s, t) = \rho \circ \tilde{\sigma}(s) = \gamma(s) = F(s, t)$. By the uniqueness part of Theorem 7.4, $\tilde{F} = \tilde{K}$. Thus $\tilde{\gamma}(s) = \tilde{F}(s, 0) = \tilde{K}(s, 0) = \tilde{\sigma}(s)$.
