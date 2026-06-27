---
role: proof
locale: en
of_concept: alpha-string-and-cartan-integers
source_book: gtm009
source_chapter: "8"
source_section: "8.4-8.5"
---

**(a)** Since $H = C_L(H)$, the only elements of $L$ commuting with $H$ are those in $H$ itself. If $c\alpha \in \Phi$ for $c \in F$, then $\mathrm{ad} h$ acts on $L_{c\alpha}$ with eigenvalue $c\alpha(h)$. The representation theory of $\mathfrak{sl}(2)$ applied to the subalgebra $S_\alpha$ shows that the only possible multiples are $\pm \alpha$.

**(b)** Fix $\alpha \in \Phi$. Consider the subalgebra $S_\alpha = L_\alpha + L_{-\alpha} + H_\alpha$ where $H_\alpha = [L_\alpha L_{-\alpha}]$. This is isomorphic to $\mathfrak{sl}(2, F)$ or a quotient thereof. $L$ becomes an $S_\alpha$-module via the adjoint representation. For any $\beta \in \Phi$, consider the $\alpha$-string through $\beta$ and the subspace $K = \bigoplus_{i \in \mathbb{Z}} L_{\beta+i\alpha}$. By the corollary of Theorem 7.2 (complete reducibility for $\mathfrak{sl}(2)$), $K$ decomposes into irreducible $S_\alpha$-modules. The weight spaces correspond to distinct integral weights $\beta(h_\alpha) + 2i$, so each root space $L_{\beta+i\alpha}$ is at most one-dimensional. In particular, $\dim L_\alpha = 1$. The existence of $y_\alpha \in L_{-\alpha}$ with $[x_\alpha y_\alpha] = h_\alpha$ follows from Proposition 8.3 parts (b) and (f).

**(c) and (e)** For fixed $\alpha, \beta \in \Phi$ with $\beta \neq \pm \alpha$, consider $K = \bigoplus L_{\beta+i\alpha}$. $K$ is an $S_\alpha$-submodule of $L$ with one-dimensional weight spaces for distinct integral weights $\beta(h_\alpha) + 2i$ ($i \in \mathbb{Z}$ such that $\beta + i\alpha \in \Phi$). By Theorem 7.2, $K$ is irreducible, and its weights form an arithmetic progression with difference 2. Let $r, q$ be the largest integers with $\beta - r\alpha, \beta + q\alpha \in \Phi$. The highest weight is $\beta(h_\alpha) + 2q$, the lowest is $\beta(h_\alpha) - 2r$, and they are negatives of each other: $(\beta + q\alpha)(h_\alpha) = -(\beta - r\alpha)(h_\alpha)$, giving $\beta(h_\alpha) = r - q$. The weights form an unbroken string, so all $\beta + i\alpha$ for $-r \leq i \leq q$ are roots.

**(f)** From (c), $\beta(h_\alpha) \in \mathbb{Z}$. Also $\beta(h_\alpha) = 2\kappa(t_\beta, t_\alpha)/\kappa(t_\alpha, t_\alpha) = 2(\beta, \alpha)/(\alpha, \alpha)$, so the Cartan integers are integral.

**(d)** If $\alpha, \beta, \alpha+\beta \in \Phi$, then in the $\alpha$-string through $\beta$, $q \geq 1$. By Lemma 7.2, $\mathrm{ad} x_\alpha$ maps $L_\beta$ onto $L_{\alpha+\beta}$ for nonzero $x_\alpha \in L_\alpha$, so $[L_\alpha L_\beta] = L_{\alpha+\beta}$.
