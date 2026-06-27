---
role: proof
locale: en
of_concept: substitution-theorem
source_book: gtm022
source_chapter: "II"
source_section: "4"
---

[Note: The full proof of Theorem 4.11 is truncated in the source text. The following reconstructs the essential reasoning.]

Let $v: P(Y) \to \mathbb{Z}_2$ be any valuation such that $v(\varphi(a)) = 1$ for all $a \in A$. Then the composition $v \circ \varphi: P(X) \to \mathbb{Z}_2$ is a homomorphism (since both $v$ and $\varphi$ are homomorphisms), hence $v \circ \varphi$ is a valuation of $P(X)$.

For every $a \in A$, we have $(v \circ \varphi)(a) = v(\varphi(a)) = 1$, so $v \circ \varphi$ makes all of $A$ true. Since by hypothesis $A \models w$, we must have $(v \circ \varphi)(w) = 1$, i.e., $v(\varphi(w)) = 1$.

Since $v$ was an arbitrary valuation making $\varphi(A)$ true, we conclude that $\varphi(A) \models \varphi(w)$.

The result follows from the fact that $P(X)$ is a free algebra: any map from the generators $X$ into a proposition algebra extends uniquely to a homomorphism, and composing homomorphisms preserves the algebraic (and hence logical) structure.
