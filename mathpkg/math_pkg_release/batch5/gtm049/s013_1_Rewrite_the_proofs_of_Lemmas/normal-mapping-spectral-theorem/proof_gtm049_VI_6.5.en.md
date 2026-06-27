---
role: proof
locale: en
of_concept: normal-mapping-spectral-theorem
source_book: gtm049
source_chapter: "VI"
source_section: "6.5"
---
The proof proceeds by induction on $$\dim W$$.

First observe: (i) $$\|wf\| = \|wf^*\|$$ for all $$w$$ in $$W$$; (ii) if $$w$$ is an eigenvector of $$f$$ with eigenvalue $$x$$, then $$w$$ is an eigenvector of $$f^*$$ with eigenvalue $$\bar{x}$$; (iii) if $$[w]f \subset [w]$$ then $$[w]^\perp f \subset [w]^\perp$$.

Since $$W$$ is a complex vector space, $$f$$ has an eigenvector (Proposition 3, §6.3). Choose an eigenvector $$a_1$$ with eigenvalue $$x$$ and normalize so that $$\sigma(a_1, a_1) = 1$$. By property (ii), $$a_1$$ is also an eigenvector of $$f^*$$, and by (iii), the orthogonal complement $$[a_1]^\perp$$ is invariant under $$f$$. The restriction of $$f$$ to $$[a_1]^\perp$$ is again normal. Induction on $$\dim W$$ completes the proof.
