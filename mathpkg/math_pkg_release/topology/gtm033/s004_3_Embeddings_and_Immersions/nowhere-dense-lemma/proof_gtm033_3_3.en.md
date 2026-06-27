---
role: proof
locale: en
of_concept: nowhere-dense-lemma
source_book: gtm033
source_chapter: "3. Embeddings and Immersions"
source_section: "3"
---

# Proof of Nowhere Density Lemma for Low-Dimensional Domain

**Lemma.** Let $g: P \to Q$ be a $C^1$ map. If $\dim Q > \dim P$, then the image of $g$ is nowhere dense in $Q$.

*Proof.* The proof is postponed to Chapter 3 of the book. It involves Sard's theorem and the concept of measure zero sets. We outline the argument here.

Let $n = \dim P$ and $m = \dim Q$, with $m > n$. By Sard's theorem (Theorem 3.1 in the book, proved in Chapter 3), the set of critical values of a $C^1$ map $g: P \to Q$ has measure zero in $Q$. Since $\dim Q > \dim P$, every point of $P$ is a critical point of $g$ (the derivative $Dg(x): T_x P \to T_{g(x)} Q$ cannot be surjective when $\dim T_x P = n < m = \dim T_{g(x)} Q$). Therefore the entire image $g(P)$ consists of critical values, and hence has measure zero in $Q$.

A set of measure zero in a manifold is nowhere dense. More precisely, if $g(P)$ contained a nonempty open set $U \subset Q$, then $U$ would have positive measure (since open sets have positive Lebesgue measure in charts), contradicting that $g(P)$ has measure zero. Therefore the image of $g$ is nowhere dense.

$\square$

**Remark.** This lemma is a crucial ingredient in the proof of the Whitney Embedding Theorem (Theorem 3.4). Applied to the secant map $\sigma: M \times M - \Delta \to S^{q-1}$ where $\dim(M \times M - \Delta) = 2n$ and $\dim S^{q-1} = q-1$, with $q > 2n+1$, the lemma guarantees the existence of a direction $v \in S^{q-1}$ not in the image of $\sigma$, ensuring the projected map is injective. Similarly applied to $\tau: T_1 M \to S^{q-1}$ with $\dim T_1 M = 2n-1$, it guarantees the projected map is an immersion.

**Note.** The source text states: "The proof of the lemma, which involves a different set of ideas, is postponed to Chapter 3." The proof above is reconstructed from the context of Sard's theorem as presented later in Chapter 3 of the book.
