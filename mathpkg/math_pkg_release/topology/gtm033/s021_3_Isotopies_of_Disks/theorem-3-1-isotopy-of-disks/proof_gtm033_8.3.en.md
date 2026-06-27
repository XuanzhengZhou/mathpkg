---
role: proof
locale: en
of_concept: disk-embedding-isotopy
source_book: gtm033
source_chapter: "8"
source_section: "3"
---

# Proof of Theorem 3.1 (Isotopy Classification of Disk Embeddings)

Let $M$ be a connected $n$-manifold and $f, g: D^k \hookrightarrow M$ embeddings of the $k$-disk, $0 \leqslant k \leqslant n$. If $k = n$ and $M$ is orientable, assume that $f$ and $g$ both preserve, or both reverse, orientation. Then $f$ and $g$ are isotopic. If $f(D^k) \cup g(D^k) \subset M - \partial M$, an isotopy between them can be realized by a diffeotopy of $M$ having compact support.

**Proof.** We use repeatedly the fact that isotopy is an equivalence relation on the set of embeddings.

First assume $\partial M = \varnothing$.

Since $M$ is connected, the embeddings $f|0, g|0: 0 \rightarrow M$ are isotopic; by Theorem 1.3 they are ambiently isotopic. Therefore we may assume $f(0) = g(0)$.

Let $(\varphi, U)$ be a chart on $M$ at $f(0)$ such that $\varphi(U, f(0)) = (\mathbb{R}^n, 0)$. We can radially isotop $f$ and $g$ to embeddings in $U$.

Moreover we can also assume, for any $k$, that $\varphi f$ and $\varphi g$ are linear: any embedding $h: D^k \to \mathbb{R}^n$ with $h(0) = 0$ is isotopic to a linear one by the standard isotopy (see proof of Theorem 4.5.3):

$$(x,t) \mapsto \begin{cases} t^{-1}h(tx), & 1 \geqslant t > 0 \\ Dh(0)x, & t = 0. \end{cases}$$

If $\varphi f$ and $\varphi g$ are linear, and $k = n$, then their determinants are both positive, by our orientation assumptions. Hence they are restrictions of maps in the same component of $\mathrm{GL}(n)$. A smooth path in $\mathrm{GL}(n)$ provides the required isotopy. If $k < n$, we can first extend $f$ and $g$ to linear automorphisms of $\mathbb{R}^n$ having positive determinants and then use a path in $\mathrm{GL}(n)$. This finishes the proof when $\partial M = \varnothing$.

If $\partial M \neq \varnothing$, first isotop $f$ and $g$ into $M - \partial M$ by isotoping $M$ into $M - \partial M$; this is easily accomplished with a collar on $\partial M$. Then apply the previous constructions to $f, g: D^k \to M - \partial M$. $\square$
