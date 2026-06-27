---
role: proof
locale: en
of_concept: continuous-image-of-compact-is-compact
source_book: gtm011
source_chapter: "4"
source_section: "4.12"
---

Let $\{V_i : i \in I\}$ be an open cover of $f(K)$ in $\Omega$. Since $f$ is continuous, each $f^{-1}(V_i)$ is open in $X$. Then $\{f^{-1}(V_i) : i \in I\}$ is an open cover of $K$ in $X$. By compactness of $K$, there exist finitely many indices $i_1, \ldots, i_n$ in $I$ such that

$$K \subset \bigcup_{k=1}^{n} f^{-1}(V_{i_k}).$$

It follows that

$$f(K) \subset \bigcup_{k=1}^{n} V_{i_k}.$$

Thus $\{V_{i_1}, \ldots, V_{i_n}\}$ is a finite subcover of $f(K)$, proving that $f(K)$ is compact in $\Omega$.
