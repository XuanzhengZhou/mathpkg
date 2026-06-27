---
role: proof
locale: en
of_concept: boundary-symmetry
source_book: gtm027
source_chapter: "1"
source_section: "Interior and Boundary"
---

# Proof of Symmetry of the Boundary

Let $A$ be a subset of a topological space $X$. The boundary of $A$, denoted $\partial A$ (or $A^b$), is defined as the set of all points $x \in X$ which are interior to neither $A$ nor $X \sim A$. Equivalently, $x \in \partial A$ iff every neighborhood of $x$ intersects both $A$ and $X \sim A$.

Now consider $\partial (X \sim A)$. By definition, $x \in \partial (X \sim A)$ iff every neighborhood of $x$ intersects both $X \sim A$ and $X \sim (X \sim A) = A$. This condition is identical to the condition for $x \in \partial A$, since both require that every neighborhood of $x$ intersect $A$ and $X \sim A$.

Therefore $\partial A = \partial (X \sim A)$. The boundary operator is symmetric with respect to complementation. $\square$
