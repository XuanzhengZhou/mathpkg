---
role: proof
locale: en
of_concept: symmetric-relation-triple-composition
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof of Symmetric Relation Triple Composition Formula (Lemma 6.1)

**Lemma 6.1.** If $V$ is symmetric, then $V \circ U \circ V = \bigcup \{V[x] \times V[y] : (x,y) \in U\}$.

**Proof.** By definition, $V \circ U \circ V$ is the set of all pairs $(u,v)$ such that $(u,x) \in V$, $(x,y) \in U$, and $(y,v) \in V$ for some $x$ and some $y$. Since $V$ is symmetric, this is equivalent to the condition $u \in V[x]$ and $v \in V[y]$ for some $(x,y) \in U$. That is, $(u,v) \in V[x] \times V[y]$ for some $(x,y) \in U$. Hence

$$V \circ U \circ V = \bigcup \{V[x] \times V[y] : (x,y) \in U\}.$$

This completes the proof.
