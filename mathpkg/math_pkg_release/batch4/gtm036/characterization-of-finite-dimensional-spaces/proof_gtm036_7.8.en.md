---
role: proof
locale: en
of_concept: characterization-of-finite-dimensional-spaces
source_book: gtm036
source_chapter: "7"
source_section: "7.8"
---

If $E$ is finite dimensional, then by theorem 7.3, $E$ is topologically isomorphic to a Euclidean space, and the unit sphere in any Euclidean norm is compact; thus $E$ has a precompact neighborhood of $0$. Conversely, suppose $E$ has a precompact neighborhood $U$ of $0$. Then there exists a finite set $F$ such that $U \subset \langle F \rangle + \frac{1}{2}U$. By induction, $U \subset \langle F \rangle + 2^{-n}U$ for all $n$. Since $\langle F \rangle$ is finite dimensional, it is closed by 7.3, and thus $U \subset \langle F \rangle^- = \langle F \rangle$. Hence $E = \bigcup nU \subset \langle F \rangle$, so $E$ is finite dimensional.
