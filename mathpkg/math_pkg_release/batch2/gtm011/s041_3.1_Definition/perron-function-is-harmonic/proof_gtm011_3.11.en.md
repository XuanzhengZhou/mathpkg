---
role: proof
locale: en
of_concept: perron-function-is-harmonic
source_book: gtm011
source_chapter: "3"
source_section: "3.11"
---

Let $|f(a)| \leq M$ for all $a \in \partial_\infty G$. The proof begins by noting that

$$\varphi(z) \leq M \quad \text{for all } z \in G,\ \varphi \in \mathcal{P}(f, G). \tag{3.12}$$

This follows because, by definition, $\limsup \varphi(z) \leq M$ whenever $\varphi \in \mathcal{P}(f, G)$; so (3.12) is a direct consequence of the Maximum Principle.

Fix $a \in G$ and let $\bar{B}(a; r) \subset G$. Then $u(a) = \sup \{ \varphi(a): \varphi \in \mathcal{P}(f, G) \}$; so there is a sequence $\{\varphi_n\}$ in $\mathcal{P}(f, G)$ such that $u(a) = \lim \varphi_n(a)$. Let $\Phi_n = \max \{ \varphi_1, \ldots, \varphi_n \}$; by Corollary 3.6, $\Phi_n$ is subharmonic. Let $\Phi_n'$ be the subharmonic function on $G$ obtained from $\Phi_n$ by Poisson modification on $B(a; r)$ (Corollary 3.7), so that $\Phi_n'(z) = \Phi_n(z)$ for $z \in G \setminus B(a; r)$ and $\Phi_n'$ is harmonic on $B(a; r)$.

It is left to the reader to verify:

$$\Phi_n' \leq \Phi_{n+1}' \quad \text{for all } n. \tag{3.13}$$

Thus $\{\Phi_n'\}$ is an increasing sequence of subharmonic functions that are harmonic on $B(a; r)$. By Harnack's Theorem, the limit $\Phi = \lim \Phi_n'$ is harmonic on $B(a; r)$. Moreover, $\Phi(a) = u(a)$ and one can show that $\Phi(z) = u(z)$ for all $z \in B(a; r)$. Since $a \in G$ was arbitrary, $u$ is harmonic on $G$.
