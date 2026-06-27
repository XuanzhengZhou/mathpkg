---
role: proof
locale: en
of_concept: birational-invariance-of-geometric-genus
source_book: gtm052
source_chapter: "II"
source_section: "8"
---

Recall that $X$ and $X'$ birationally equivalent means there exist rational maps $\varphi: X \dashrightarrow X'$ and $\psi: X' \dashrightarrow X$ inverse to each other. Let $f: V \to X'$ be a morphism representing $\varphi$ on the largest open set $V \subseteq X$. From Proposition 8.11 we have a map $f^* \Omega_{X'/k} \to \Omega_{V/k}$ on $V$. Taking $n$-th exterior powers where $n = \dim X = \dim X'$ (birational equivalence preserves dimension), we obtain $\omega_{X'}|_V \to \omega_V \cong \omega_X|_V$.

Since $\omega_X$ is an invertible sheaf, this gives a global section of $\mathcal{H}om(\omega_{X'}|_V, \omega_X|_V)$, hence an injective map on global sections $\Gamma(X', \omega_{X'}) \hookrightarrow \Gamma(V, \omega_X|_V)$. But $X - V$ has codimension $\geq 2$ in $X$, and $X$ is nonsingular (hence normal), so by (6.3A), every section of $\omega_X$ on $V$ extends uniquely to $X$. Thus $\Gamma(V, \omega_X|_V) \cong \Gamma(X, \omega_X)$, and we obtain $p_g(X') \leq p_g(X)$. By symmetry, $p_g(X) \leq p_g(X')$, so $p_g(X) = p_g(X')$.
