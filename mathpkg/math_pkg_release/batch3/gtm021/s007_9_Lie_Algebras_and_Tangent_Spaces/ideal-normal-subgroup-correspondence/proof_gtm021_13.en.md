---
role: proof
locale: en
of_concept: ideal-normal-subgroup-correspondence
source_book: gtm021
source_chapter: "13"
source_section: "Correspondence Between Groups and Lie Algebras"
---
The "only if" part (normality $\implies$ ideal) is Corollary A of Theorem 10.4, which holds in any characteristic.

For the "if" part: Suppose $\mathfrak{h}$ is an ideal in $\mathfrak{g}$, and consider
$$N = \{x \in G \mid \operatorname{Ad} x(\mathfrak{h}) = \mathfrak{h}\}.$$

According to Proposition 13.2 (and the remark following it),
$$\mathfrak{n} = \{X \in \mathfrak{g} \mid d(\operatorname{Ad})(X)(\mathfrak{h}) \subset \mathfrak{h}\} = \{X \in \mathfrak{g} \mid \operatorname{ad} X(\mathfrak{h}) \subset \mathfrak{h}\}.$$

Since $\mathfrak{h}$ is an ideal, $\operatorname{ad} X(\mathfrak{h}) \subset \mathfrak{h}$ for all $X \in \mathfrak{g}$, so $\mathfrak{n} = \mathfrak{g}$. Because $G$ is connected and $\operatorname{char} K = 0$, the equality of Lie algebras implies $N = G$ (by Theorem 13.1: the injectivity of the correspondence forces the connected component of $N$, which has the same Lie algebra as $G$, to equal $G$).

Now if $x \in G$, then $\mathcal{L}(\operatorname{Int} x(H)) = \operatorname{Ad} x(\mathfrak{h}) = \mathfrak{h}$. The two connected groups $H$ and $xHx^{-1}$ have the same Lie algebra, so by Theorem 13.1 they must coincide: $xHx^{-1} = H$. Hence $H \trianglelefteq G$.
