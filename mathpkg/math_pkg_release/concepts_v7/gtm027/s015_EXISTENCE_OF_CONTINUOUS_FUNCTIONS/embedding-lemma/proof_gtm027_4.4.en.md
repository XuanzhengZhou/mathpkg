---
role: proof
locale: en
of_concept: embedding-lemma
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Embedding Lemma (Evaluation Map)

**Embedding Lemma.** Let $F$ be a family of continuous functions, each member $f$ being on a topological space $X$ to a topological space $Y_f$. Then:

(a) The evaluation map $e$ is a continuous function on $X$ to the product space $\prod \{Y_f : f \in F\}$.

(b) The function $e$ is an open map of $X$ onto $e[X]$ if $F$ distinguishes points and closed sets.

(c) The function $e$ is one to one if and only if $F$ distinguishes points.

*Proof.* (a) The map $e$ followed by projection $P_f$ into the $f$-th coordinate space is continuous because $P_f \circ e(x) = f(x)$. Consequently, by theorem 3.3 (a map into a product is continuous iff each coordinate function is continuous), $e$ is continuous.

(b) To prove statement (b) it is sufficient to show that the image under $e$ of an open neighborhood $U$ of a point $x$ contains the intersection of $e[X]$ and a neighborhood of $e(x)$. Let $U$ be an open neighborhood of $x$. Then $X \sim U$ is closed and $x \notin X \sim U$. Since $F$ distinguishes points and closed sets, there exists $f \in F$ such that $f(x) \notin f[X \sim U]^{-}$. Let $V = Y_f \sim f[X \sim U]^{-}$. Then $V$ is an open neighborhood of $f(x)$ in $Y_f$. Now $P_f^{-1}[V]$ is a neighborhood of $e(x)$ in the product, and if $e(z) \in P_f^{-1}[V] \cap e[X]$, then $f(z) \in V$, so $f(z) \notin f[X \sim U]^{-}$, which forces $z \notin X \sim U$, i.e., $z \in U$. Hence $P_f^{-1}[V] \cap e[X] \subset e[U]$, proving that $e$ is open onto its image.

(c) If $e(x) = e(y)$, then $f(x) = f(y)$ for all $f \in F$. If $F$ distinguishes points, this forces $x = y$, so $e$ is one-to-one. Conversely, if $e$ is one-to-one and $x \neq y$, then $e(x) \neq e(y)$, so $f(x) \neq f(y)$ for some $f \in F$, meaning $F$ distinguishes points.

