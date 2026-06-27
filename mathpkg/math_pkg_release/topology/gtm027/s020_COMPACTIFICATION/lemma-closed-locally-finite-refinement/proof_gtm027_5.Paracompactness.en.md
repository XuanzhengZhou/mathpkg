---
role: proof
locale: en
of_concept: lemma-closed-locally-finite-refinement
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof of Existence of Closed Locally Finite Refinements

**Lemma 29.** If $X$ is regular and each open cover has a locally finite refinement, then each open cover has a closed locally finite refinement.

*Proof.* Let $\mathcal{U}$ be an open cover of $X$. Since $X$ is regular, there exists an open cover $\mathcal{V}$ such that the family of closures of members of $\mathcal{V}$ refines $\mathcal{U}$. (For each $x \in X$, choose $U \in \mathcal{U}$ with $x \in U$; by regularity pick an open neighborhood $V_x$ of $x$ such that $\overline{V_x} \subset U$; the collection of all such $V_x$ forms $\mathcal{V}$.)

By hypothesis, $\mathcal{V}$ has a locally finite refinement $\mathcal{A}$. Consider the family of closures $\overline{\mathcal{A}} = \{\overline{A} : A \in \mathcal{A}\}$. Since $\mathcal{A}$ is locally finite, $\overline{\mathcal{A}}$ is also locally finite. Moreover, each $A \in \mathcal{A}$ is contained in some $V \in \mathcal{V}$, so $\overline{A} \subset \overline{V}$ for that $V$. By construction, each $\overline{V}$ is contained in some $U \in \mathcal{U}$. Thus $\overline{A} \subset U$, and $\overline{\mathcal{A}}$ is a closed locally finite refinement of $\mathcal{U}$. $\square$
