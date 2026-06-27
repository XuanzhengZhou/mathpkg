---
role: proof
locale: en
of_concept: existence-of-transitive-homeomorphisms-of-square
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

Let $X = [0,1]^2$ be the closed unit square and let $H$ be the space of all automorphisms (homeomorphisms) of $X$, equipped with the uniform metric

$$\varrho(S, T) = \sup_{x \in X} |Sx - Tx|.$$

The space $H$ is topologically complete (a $G_{\delta}$ in the complete space of all continuous maps $X \to X$, by the same reasoning as the 1-dimensional case in Chapter 13). For each pair of basic open sets $U_i, U_j$ from a countable base for $X$, define

$$E_{ij} = \left\{ T \in H : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \right\}.$$

Each $E_{ij}$ is open in $H$ (the condition involves a countable union of open preimages). To show $E_{ij}$ is dense, take any $T \in H$ and $\varepsilon > 0$. Join a point of $U_i$ to a point of $U_j$ by a line segment and choose points $p_1, p_2, \ldots, p_{N+1}$ on this segment with $p_1 \in U_i$, $p_{N+1} \in U_j$, and $|p_k - p_{k+1}| < \varepsilon/2$. Choose $\delta < \frac{1}{2} \min |p_k - p_{k+1}|$ so that the $\delta$-neighborhoods of $p_1$ and $p_{N+1}$ are contained in $U_i$ and $U_j$ respectively. Using the fact that recurrent points under $T$ form a residual set (Theorem 17.3) and nonperiodic points also form a residual set, one can select a nonperiodic point $x_1$ in the $\delta$-neighborhood of $p_1$ whose positive semiorbit returns to this neighborhood. A small perturbation $S$ of $T$ can then be constructed such that $\varrho(S, T) < \varepsilon$ and some iterate of $S$ maps a point of $U_i$ into $U_j$, so $S \in E_{ij}$.

Thus each $E_{ij}$ is a dense open subset of $H$. Since $H$ is topologically complete, the Baire category theorem implies that

$$\bigcap_{i,j} E_{ij}$$

is a dense $G_{\delta}$ in $H$, hence nonempty. For any $T \in \bigcap_{i,j} E_{ij}$, each

$$G_j = \bigcup_{k=1}^{\infty} T^{-k} U_j$$

is open. Moreover, since $T \in \bigcap_i E_{ij}$, we have $U_i \cap G_j \neq \emptyset$ for every $i$, so each $G_j$ is dense in $X$. Applying the Baire category theorem in the complete metric space $X$,

$$\bigcap_{j=1}^{\infty} G_j \neq \emptyset.$$

For any point $x \in \bigcap_j G_j$, its positive semiorbit $\{x, Tx, T^2x, \ldots\}$ intersects every $U_j$, and since $\{U_j\}$ is a base, this semiorbit is dense in $X$. Therefore, any $T$ in the residual set $\bigcap_{i,j} E_{ij}$ is a transitive automorphism of the closed unit square.
