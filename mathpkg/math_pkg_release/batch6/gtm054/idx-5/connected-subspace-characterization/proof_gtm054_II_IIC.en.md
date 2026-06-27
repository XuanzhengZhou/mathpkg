---
role: proof
locale: en
of_concept: connected-subspace-characterization
source_book: gtm054
source_chapter: "II"
source_section: "IIC"
---

**Proof of C22 Proposition.**

The sufficiency of the condition in (a) is immediate: if every pair of elements in $\operatorname{Fnd}(\mathcal{A})$ is contained in some elementary set, then $\mathcal{A}$ cannot decompose as a nontrivial direct sum, for any such decomposition would separate the foundation into disjoint blocks with no elementary set crossing between them.

For the necessity, by repeated application of Lemma C2, we see that there exists an $x_1x_2$-path in $\Lambda(\mathcal{A})$ if and only if $\{x_1, x_2\} \subseteq M$ for some $M \in \mathcal{M}(\mathcal{A})$. Hence if $\mathcal{A}$ is connected, $\Lambda(\mathcal{A})$ is connected (by Proposition C6 and the definition), and so such a path must exist between any two elements of $\operatorname{Fnd}(\mathcal{A})$. This gives the existence of the required $M$.

Part (b) is merely a restatement of this principle: the relation $\sim$ is precisely the path-connectivity relation of C19(b) restricted to the foundation, and by C20 its equivalence classes are the components.
