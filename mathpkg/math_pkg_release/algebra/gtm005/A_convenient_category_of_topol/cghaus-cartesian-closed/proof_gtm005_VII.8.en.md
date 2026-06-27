---
role: proof
locale: en
of_concept: cghaus-cartesian-closed
source_book: gtm005
source_chapter: "VII"
source_section: "8. Compactly Generated Spaces"
---

For $X, Y \in \mathbf{CGHaus}$, define $X^Y = K(\operatorname{Cop}(Y, X))$. Define $e: X^Y \mathbin{\square} Y \to X$ by evaluation $\langle f, y \rangle \mapsto f(y)$. We claim $e$ is continuous; it suffices to prove $e: X^Y \times Y \to X$ is continuous on compact sets, since $X^Y \mathbin{\square} Y$ is compactly generated.

Any compact subset of the product $X^Y \times Y$ is contained in the product of its projections. Thus it suffices to show $e$ is continuous on any set $D \times C$ where $D$ is compact in $\operatorname{Cop}(Y, X)$ and $C$ is compact in $Y$. Take $\langle f, y \rangle \in D \times C$ and an open set $U \subset X$ containing $f(y)$. Since $f: Y \to X$ is continuous, there exists a neighborhood $M$ of $y$ in $C$ whose closure satisfies $f(\overline{M}) \subset U$. Then $N(\overline{M}, U)$ is a neighborhood of $f$, and $N(\overline{M}, U) \times M$ is a neighborhood of $\langle f, y \rangle$ mapped by $e$ into $U$. Hence $e$ is continuous.

Now the adjunction: to each $f: Z \mathbin{\square} Y \to X$, associate $\hat{f}: Z \to X^Y$ defined by $(\hat{f}(z))(y) = f(z, y)$. Since $X^Y$ carries the Kelleyfication of $\operatorname{Cop}(Y, X)$, continuity of $\hat{f}$ reduces to proving $Z \to \operatorname{Cop}(Y, X)$ is continuous on compacta. For any compact $C \subset Z$, the restriction $f|_{C \times Y}$ factors through $C \mathbin{\square} Y$, and the standard argument for locally compact $Y$ goes through because we only need continuity on products of compact sets, which are automatically compactly generated. Thus we obtain the natural bijection
$$\mathbf{CGHaus}(Z \mathbin{\square} Y, X) \cong \mathbf{CGHaus}(Z, X^Y).$$

The homeomorphism $X^{Z \mathbin{\square} Y} \cong (X^Y)^Z$ follows from this adjunction by categorical reasoning (see Exercise IV.6.3). Since $\mathbin{\square}$ designates the product in $\mathbf{CGHaus}$, the category is cartesian closed.
