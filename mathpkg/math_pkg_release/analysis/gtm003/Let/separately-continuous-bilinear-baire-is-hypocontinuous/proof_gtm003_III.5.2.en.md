---
role: proof
locale: en
of_concept: separately-continuous-bilinear-baire-is-hypocontinuous
source_book: gtm003
source_chapter: "III"
source_section: "5.2"
---

Let $f: E \times F \to G$ be a separately continuous bilinear map. Assume first that $F$ is barreled and $G$ is locally convex. Fix a bounded set $B \subset E$ and a closed, convex, circled 0-neighborhood $W$ in $G$. For each $x \in B$, the partial map $f_x: F \to G$ is continuous, so $f_x^{-1}(W)$ is a closed, convex, circled 0-neighborhood in $F$. Define $D = \bigcap_{x \in B} f_x^{-1}(W)$. For any $y \in F$, the set $\{f(x, y) : x \in B\}$ is bounded in $G$ (since the map $x \mapsto f(x, y)$ is continuous and $B$ is bounded). Hence there exists $\lambda > 0$ such that $f(B, \lambda^{-1}y) \subset W$, i.e., $\lambda^{-1}y \in D$. Thus $D$ is radial; being an intersection of closed, convex, circled sets, $D$ is a barrel in $F$. Since $F$ is barreled, $D$ is a 0-neighborhood. Then $f(B \times D) \subset W$, which proves $\mathfrak{B}$-hypocontinuity of $f$.

If $F$ is a Baire space (instead of barreled), the result follows from (III, 5.1) which states that separately equicontinuous families on Baire domains are equicontinuous. Applying this to the family $\{f_x : x \in B\}$ for each bounded $B \subset E$, we obtain the same conclusion.
