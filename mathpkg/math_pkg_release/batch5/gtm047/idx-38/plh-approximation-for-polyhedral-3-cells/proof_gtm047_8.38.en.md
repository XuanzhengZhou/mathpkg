---
role: proof
locale: en
of_concept: plh-approximation-for-polyhedral-3-cells
source_book: gtm047
source_chapter: "8"
source_section: "38"
---

Given such a $K$, there is a PLH $\phi: K \to \operatorname{Int} K$; and $\phi$ can be chosen so as to be arbitrarily close to the identity. Now the homeomorphism $h|_{\phi(K)}$ can be extended to a neighborhood of the polyhedral 3-cell $\phi(K)$. If $f'$ is a sufficiently close PLH approximation of $h|_{\phi(K)}$, then $f = f' \circ \phi$ will be an $\varepsilon$-approximation of $h$. Thus we may assume, with no loss of generality, that the original $h$ can be extended to a neighborhood $U$ of $K$.

We suppose that $K$ has been subdivided into "small" simplexes; the degree of smallness will be prescribed later. We also suppose that $K$ is subdivided in such a way that in the link $L(v)$ of a vertex $v$ (that is, the set of all simplexes of $\operatorname{St} v$ that do not contain $v$), the interior of an edge never separates two vertices from one another. (This condition will be needed in the proofs of Lemmas 9 and 10 below.)

Let $N$ be a regular neighborhood of the 1-skeleton $K^1$ of $K$, lying in $U$. $N$ can be chosen so as to lie in an arbitrarily small neighborhood of $K^1$. In $N$, we take splitting disks $D_e$, containing the mid-points of the edges $e$ of $K$. These decompose $N$ into dual cells $C_v$, each of these containing exactly one vertex $v$ of $K$. For each $v$, let $S(v)$ be the "half-star" of $v$ in $K$.

We shall show that the homeomorphism
$$h|_{K \cup N}: K \cup N \to \mathbb{R}^3$$
has an $\varepsilon$-approximation which is a PLH. The restriction of this PLH to $K$ will then satisfy the conditions of Theorem 1.

For each 2-simplex $\sigma$ of $K$, let $N_{\sigma}$ be the union of the dual cells of $N$ that contain vertices of $\sigma$. Then $N_{\sigma}$ is a solid torus.

**Lemma 1.** There is a regular neighborhood $N$ of $K^1$, and a PLH
$$f_1: N \leftrightarrow N'' \subset \mathbb{R}^3,$$
such that
(1) $N''$ is a neighborhood of $h(K^1)$.
(2) $D_e'' \cap \sigma' \neq \emptyset$ only if $e$ is an edge of $\sigma$.
(3) $C_v'' \cap \sigma' \neq \emptyset$ only if $v$ is a vertex of $\sigma$.
(4) $N_{\sigma}''$ is a neighborhood of $J' = \operatorname{Bd} \sigma'$.
(5) $f_1$ is an $(\varepsilon/3)$-approximation of $h|_N$.

The proof is by Theorem 33.1. Conditions (2)–(5) hold whenever $f_1$ is a sufficiently close approximation of $h|_N$. Note that in Lemma 1, $N$ can be chosen so as to lie in any given neighborhood of $K^1$, and so $N$ and $f_1$ can be chosen so that $N''$ lies in any given neighborhood of $h(K^1)$.

Now there are solid tori $S_1$ and $S_2$ such that (a) $N_{\sigma} \subset \operatorname{Int} S_2$, (b) $S_1$ is a neighborhood of the union of $\operatorname{Bd} \sigma$ and the half-stars $S(v)$ of the vertices $v$ of $\sigma$ in the complex $K^1$, (c) $\operatorname{Cl}(S_2 - S_1)$ is a polyhedral 3-cell. [Additional lemmas follow to complete the proof — see Lemmas 4, 5, 6 and Operations 1, 2 in the full proof, which culminate in extending $f$ to all of $N$ by repeated applications of Theorem 18.2.]
