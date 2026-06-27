---
role: proof
locale: en
of_concept: serre-lemma-ad-xk-yij
source_book: gtm009
source_chapter: "VI"
source_section: "18"
---

Consider $y_{ij} = (\operatorname{ad} y_i)^{-c_{ji}+1}(y_j)$ for fixed $i \neq j$.

\textbf{Case (a): $k \neq i$.} By relation (S2), $[x_k y_i] = 0$, so $\operatorname{ad} x_k$ and $\operatorname{ad} y_i$ commute as operators on $L_o$. Therefore,
$$\operatorname{ad} x_k(y_{ij}) = \operatorname{ad} x_k((\operatorname{ad} y_i)^{-c_{ji}+1}(y_j)) = (\operatorname{ad} y_i)^{-c_{ji}+1}(\operatorname{ad} x_k(y_j)).$$

If $k = j$, then $\operatorname{ad} x_k(y_j) = [x_j y_j] = h_j$. Now compute
$$\operatorname{ad} y_i(h_j) = -[h_j y_i] = c_{ij} y_i$$
by (S3), since $[h_j y_i] = -\langle \alpha_i, \alpha_j \rangle y_i = -c_{ij} y_i$, so $\operatorname{ad} y_i(h_j) = c_{ij} y_i$.

If $c_{ij} = 0$, then $\operatorname{ad} y_i(h_j) = 0$, so $(\operatorname{ad} y_i)^{-c_{ji}+1}(h_j) = 0$ because $-c_{ji}+1 \geq 1$. If $c_{ij} \neq 0$, then since $i \neq j$, we have $c_{ij} < 0$ (the off-diagonal entries of a Cartan matrix are non-positive), hence $c_{ji} < 0$ as well. Then $-c_{ji} + 1 \geq 2$, and $\operatorname{ad} y_i(h_j) = c_{ij} y_i$, so applying $\operatorname{ad} y_i$ again gives $(\operatorname{ad} y_i)^2(h_j) = 0$. Thus $(\operatorname{ad} y_i)^{-c_{ji}+1}(h_j) = 0$.

If $k \neq j$, then $[x_k y_j] = 0$ by (S2), so $\operatorname{ad} x_k(y_j) = 0$ trivially.

\textbf{Case (b): $k = i$.} Recall from the proof of Theorem 18.2 that $S = F x_i + F y_i + F h_i$ is a subalgebra of $L_o$ isomorphic to $\mathfrak{sl}(2, F)$. The adjoint action of $S$ on $L_o$ decomposes $L_o$ into a direct sum of finite-dimensional irreducible $S$-modules. Since $\operatorname{ad} x_i$ is locally nilpotent, the theory of $\mathfrak{sl}(2)$-representations applies.

The element $y_{ij}$ is a highest weight vector of weight $-c_{ji}$ for the adjoint action of $S$ (as can be verified from the relations). In an irreducible $\mathfrak{sl}(2)$-module, a highest weight vector $v$ satisfies $\operatorname{ad} x_i(v) = 0$ by definition, so $\operatorname{ad} x_i(y_{ij}) = 0$.

Thus in all cases, $\operatorname{ad} x_k(y_{ij}) = 0$ for all $k$.
