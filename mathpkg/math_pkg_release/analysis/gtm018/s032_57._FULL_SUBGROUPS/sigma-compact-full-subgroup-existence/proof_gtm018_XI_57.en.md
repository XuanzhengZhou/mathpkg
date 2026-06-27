---
role: proof
locale: en
of_concept: sigma-compact-full-subgroup-existence
source_book: gtm018
source_chapter: "XI"
source_section: "57"
---

By Theorem 51.A, it is sufficient to prove that if $\{C_n\}$ is a sequence of compact sets in $X$, then there exists a $\sigma$-compact full subgroup $Z$ of $X$ such that $C_n \subset Z$ for $n = 1, 2, \dots$.

Let $D$ be a compact set which contains a neighborhood of the identity $e$. Define $D_0 = D$ and, for $n = 0, 1, 2, \dots$,

$$D_{n+1} = D_n^{-1} D_n \cup C_{n+1}.$$

Set $Z = \bigcup_{n=0}^{\infty} D_n$. Then $Z$ is $\sigma$-compact (as a countable union of compact sets), has non-empty interior (since $D_0 = D$ contains a neighborhood of $e$), and contains each $C_n$. To complete the proof we must show that $Z$ is a subgroup, for which it suffices to prove $Z^{-1} Z \subset Z$.

We first show by induction that $D_n \subset D_{n+1}$ for all $n$. Note that $e \in D_0$ (since $D$ is a neighborhood of $e$). Suppose inductively that $e \in D_n$ for some $n$. Then $e \in D_n^{-1}$ as well. If $x \in D_n$, then

$$x \in (D_n^{-1}) x \subset D_n^{-1} D_n \subset D_{n+1}.$$

Thus $D_n \subset D_{n+1}$. Since $e \in D_0$, the induction hypothesis holds for all $n$, and we have

$$D_0 \subset D_1 \subset D_2 \subset \cdots.$$

Now let $x, y \in Z$. There exists $n$ such that $x, y \in D_n$. Then $y^{-1} \in D_n^{-1}$, so

$$x y^{-1} \in D_n D_n^{-1} \subset D_{n+1}^{-1} D_{n+1} \subset D_{n+2} \subset Z.$$

Thus $Z$ is closed under the group operations, i.e., $Z$ is a subgroup. Since $Z$ has non-empty interior (it contains the interior of $D$), $Z$ is a full subgroup. Therefore $Z$ is a $\sigma$-compact full subgroup containing every $C_n$, and consequently containing $E$.
