---
role: proof
locale: en
of_concept: submanifold-via-embedding-theorem
source_book: gtm033
source_chapter: "3. Embeddings and Immersions"
source_section: "3"
---

# Proof of Theorem 3.1: Submanifold Characterization via Embedding

Let $N$ be a $C^r$ manifold, $r \geqslant 1$. A subset $A \subset N$ is a $C^r$ submanifold if and only if $A$ is the image of a $C^r$ embedding.

**Proof.** ($\Rightarrow$) Suppose $A$ is a $C^r$ submanifold. Then $A$ has a natural $C^r$ differential structure derived from a covering by submanifold charts. For each submanifold chart $(\varphi, U)$ of $N$ adapted to $A$, the restriction $\varphi|_{U \cap A}$ is a chart on $A$. These restricted charts form a $C^r$ atlas for $A$. The inclusion map $i: A \hookrightarrow N$ is then $C^r$: in the restricted charts, its local representation is the inclusion $\mathbb{R}^k \hookrightarrow \mathbb{R}^n$ as the first $k$ coordinates, which is $C^\omega$. Moreover, the derivative $T_x i$ is injective at each $x \in A$, so $i$ is an immersion. Since $i$ is the inclusion map, it is a homeomorphism onto its image. Hence $i$ is a $C^r$ embedding.

($\Leftarrow$) Suppose $f: M \to N$ is a $C^r$ embedding, and let $A = f(M)$. For each $x \in M$, choose charts $(\varphi, U)$ on $M$ and $(\psi, V)$ on $N$ with $f(U) \subset V$, $\varphi(x) = 0$, $\psi(f(x)) = 0$, and such that the local representation $\tilde{f} = \psi \circ f \circ \varphi^{-1}$ satisfies $\tilde{f}(y_1, \dots, y_m) = (y_1, \dots, y_m, 0, \dots, 0)$. This is possible by the inverse function theorem, since $T_x f$ is injective. The chart $(\psi, V)$ is then a submanifold chart for $A$, and the collection of all such charts makes $A$ a $C^r$ submanifold of $N$. $\square$

The first part of the proof collates the local submanifold charts (restricted to $A$) into a differential structure on $A$; this makes the inclusion map of $A$ into an embedding. In the second part, the passage from infinitesimal to local is achieved via the inverse function theorem: the condition that $f$ be an immersion is an infinitesimal condition (referring only to the limiting behavior of $f$ at each point), and the inverse function theorem provides the link to a local condition (behavior on whole neighborhoods).
