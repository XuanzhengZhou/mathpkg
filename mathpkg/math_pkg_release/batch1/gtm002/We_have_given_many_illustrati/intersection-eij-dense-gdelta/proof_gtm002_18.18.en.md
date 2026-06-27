---
role: proof
locale: en
of_concept: intersection-eij-dense-gdelta
source_book: gtm002
source_chapter: "18"
source_section: "18"
---
For any pair of positive integers $i$ and $j$, define
$$E_{ij} = \{ T \in M : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \}.$$

First, each $E_{ij}$ is open in $M$. Indeed, the condition $U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset$ means there exists a finite $k$ and a point $x \in U_i$ such that $T^k x \in U_j$. For any $T'$ sufficiently close to $T$ in the uniform metric, $|T^k x - T'^k x|$ can be made arbitrarily small, so $T'^k x$ remains in $U_j$ for $T'$ close enough to $T$. Thus $T' \in E_{ij}$, proving openness.

Second, each $E_{ij}$ is dense in $M$. Given any $T \in M$ and any $\varepsilon > 0$, we must find $S \in E_{ij}$ with $\varrho(S, T) < \varepsilon$. Since $M \setminus P$ is residual (as shown in the periodic-points theorem), there exist automorphisms arbitrarily close to $T$ that have nonperiodic points in every nonempty open set. Choose such an automorphism $T_0$ with $\varrho(T_0, T) < \varepsilon/2$. Join a point of $U_i$ to a point of $U_j$ by a line segment. Choose points $p_1, p_2, \ldots, p_{N+1}$ on this segment such that $p_1 \in U_i$, $p_{N+1} \in U_j$, and $|p_k - p_{k+1}| < \varepsilon/2$ for $k = 1, \ldots, N$. Choose $\delta < \frac{1}{2} \min |p_k - p_{k+1}|$ such that the $\delta$-neighborhoods of $p_1$ and $p_{N+1}$ are contained in $U_i$ and $U_j$ respectively. Choose a nonperiodic point $x_1$ in the $\delta$-neighborhood of $p_1$ whose positive semiorbit under $T_0$ returns to the same neighborhood (possible because recurrent points are residual by Theorem 17.3, and nonperiodic points are also residual). Then modify $T_0$ slightly near the successive images to obtain $S$ with $S \in E_{ij}$ and $\varrho(S, T) < \varepsilon$.

Therefore each $E_{ij}$ is a dense open set in $M$. Since $M$ is topologically complete, the Baire category theorem implies
$$\bigcap_{i,j=1}^{\infty} E_{ij}$$
is a dense $G_\delta$ in $M$, and in particular nonempty.
