---
role: proof
locale: en
of_concept: rados-triangulation-theorem-for-2-manifolds
source_book: gtm047
source_chapter: "7"
source_section: "The triangulation theorem for 2-manifolds"
---

Let $M$ be the given 2-manifold. The theorem can be interpreted to mean either: (1) there is a Euclidean complex $K$ with $M \cong |K|$, or (2) there is a PL complex $\mathcal{K}$ in $M$ with $|\mathcal{K}| = M$. By Theorem 7.5, (2) $\Rightarrow$ (1) (by taking the Euclidean complex defined by the barycentric coordinate systems on PL simplexes), and the converse is obvious. We prove (2).

Let $\{N_i\}, \{N_i'\}$ and $h_i: \overline{N_i} \leftrightarrow \overline{D}, \overline{N_i'} \leftrightarrow \overline{D}'$ be as in Theorem 1 (countable covering of $M$ by Euclidean ball pairs). Throughout the proof, all PL complexes mentioned will be in $M$.

Evidently there is a PL complex $\mathcal{K}_1$ such that (1) $|\mathcal{K}_1|$ is a 2-manifold with boundary, and (2) $\overline{N}_1' \subset |\mathcal{K}_1'|$, where $\mathcal{K}_1'$ is the set of all simplexes $[g]$ of $\mathcal{K}_1$ such that $|[g]| \cap \operatorname{Bd} |\mathcal{K}_1| = \emptyset$. (This is achieved by taking a suitable finite triangulation of the closed ball $\overline{D}$ and transferring it to $\overline{N}_1$ via the homeomorphism $h_1$.)

Now suppose recursively that we have constructed a PL complex $\mathcal{K}_n$ such that (3) $|\mathcal{K}_n|$ is a 2-manifold with boundary, and (4) $\bigcup_{i=1}^{n} \overline{N_i'} \subset |\mathcal{K}_n'|$, where $\mathcal{K}_n'$ is the set of simplexes whose image-sets are disjoint from $\operatorname{Bd} |\mathcal{K}_n|$.

Consider the next chart $(N_{n+1}, N_{n+1}')$. To incorporate it into the existing complex while preserving the manifold-with-boundary property, one works on the preimage under the chart map. Let $f_n: |K_n| \to |\mathcal{K}_n|$ be the Euclidean complex underlying $\mathcal{K}_n$. Let $V$ be an open neighborhood of $N_{n+1} \cap \operatorname{Bd} |\mathcal{K}_n|$ in $|\mathcal{K}_n|$, lying in $|\mathcal{K}_n| \cap N_{n+1}$ and not intersecting $|\mathcal{K}_n'|$, and let $U = f_n^{-1}(V)$. Then $U$ is open in $|K_n|$. By Theorem 2, there is a complex $K_U$ such that $|K_U| = U$ and every simplex of $K_U$ is a subsimplex of a simplex of $K_n$. Then $K_U$ is a combinatorial 2-manifold with boundary.

Using $K_U$, one constructs $\mathcal{K}_{n+1}$ extending $\mathcal{K}_n$ so that conditions (3) and (4) hold with $n$ replaced by $n+1$, and such that $\mathcal{K}_n' \subset \mathcal{K}_{n+1}'$. This gives an ascending sequence of complexes whose union $\mathcal{K} = \bigcup_n \mathcal{K}_n$ satisfies $|\mathcal{K}| = M$, completing the proof.
