---
role: proof
locale: en
of_concept: projective-cover-of-simple-module
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** (a) $\Rightarrow$ (b). Clearly $P$ is the projective cover of a simple module iff $P$ contains a superfluous maximal submodule. But $JP$ is contained in every maximal submodule of $P$; and $JP$ contains every superfluous submodule of $P$ ((9.13) and (17.10)).

(b) $\Rightarrow$ (c). If $JP$ is a superfluous maximal submodule of $P$, then by (17.12) and Schur's Lemma (13.1)

$$\operatorname{End}({}_R P)/J(\operatorname{End}({}_R P)) \cong \operatorname{End}_R(P/JP)$$

is a division ring. Thus by (15.15), (b) implies that $\operatorname{End}({}_R P)$ is local.

(c) $\Rightarrow$ (a). Suppose $\operatorname{End}({}_R P)$ is a local ring. Then $P \neq 0$. By (17.14) there is a maximal submodule $K < P$. We claim that the natural epimorphism $P \to P/K \to 0$ is a projective cover, i.e., $K \ll P$. Suppose $K + L = P$ for some $L \leq P$. Then

$$P/K \cong (L + K)/K \cong L/(L \cap K);$$

so there is a non-zero homomorphism $f: P \to L/(L \cap K)$. Since $P$ is projective, there is an endomorphism $s: P \to L \leq P$ making the diagram commute. But since $\operatorname{End}({}_R P)$ is local, either $s$ or $1-s$ is invertible, leading to $L = P$ or $K = P$, hence $K \ll P$.
