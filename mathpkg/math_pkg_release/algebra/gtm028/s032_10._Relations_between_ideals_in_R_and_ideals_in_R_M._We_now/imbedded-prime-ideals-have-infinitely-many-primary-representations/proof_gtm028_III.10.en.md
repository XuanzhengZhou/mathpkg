---
role: proof
locale: en
of_concept: imbedded-prime-ideals-have-infinitely-many-primary-representations
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

By hypothesis, $\mathfrak{p}$ is an imbedded prime of $\mathfrak{a}$, so there exists an associated prime ideal $\mathfrak{v}$ of $\mathfrak{a}$ strictly contained in $\mathfrak{p}$. It suffices to prove the following Lemma (stated and proved separately). Given the Lemma, starting from any irredundant primary representation, one can iteratively replace the $\mathfrak{p}$-primary component with a strictly smaller one (using the Lemma with the intersection of the other components playing the role of $\mathfrak{u}$), obtaining infinitely many distinct irredundant primary representations.

\textbf{Lemma.} Given primary ideals $\mathfrak{u}$ and $\mathfrak{q}$ in a noetherian ring $R$, which belong to prime ideals $\mathfrak{v}$ and $\mathfrak{p}$ such that $\mathfrak{v} < \mathfrak{p} \neq R$, there exists an ideal $\mathfrak{q}'$, primary for $\mathfrak{p}$, such that $\mathfrak{q}' < \mathfrak{q}$ and $\mathfrak{q}' \cap \mathfrak{u} = \mathfrak{q} \cap \mathfrak{u}$.

\textit{Proof of Lemma.} By passage to $R/(\mathfrak{q} \cap \mathfrak{u})$, we may suppose that $\mathfrak{q} \cap \mathfrak{u} = (0)$. Then the intersection of all primary ideals belonging to $\mathfrak{p}$ is $(0)$ (Theorem 20). Since $\mathfrak{q} \not\subset \mathfrak{v}$ (otherwise $\mathfrak{q}$ would be $\mathfrak{v}$-primary rather than $\mathfrak{p}$-primary), we have $\mathfrak{q} \neq (0)$. Hence there exists an ideal $\mathfrak{q}''$ primary for $\mathfrak{p}$ such that $\mathfrak{q}'' \not\supset \mathfrak{q}$ (for otherwise $\mathfrak{q}$ would be contained in every $\mathfrak{p}$-primary ideal, hence in their intersection $(0)$, a contradiction). Setting $\mathfrak{q}' = \mathfrak{q} \cap \mathfrak{q}''$, we obtain $\mathfrak{q}'$ primary for $\mathfrak{p}$ (as intersection of two $\mathfrak{p}$-primary ideals), with $\mathfrak{q}' < \mathfrak{q}$, and $\mathfrak{q}' \cap \mathfrak{u} = (0) = \mathfrak{q} \cap \mathfrak{u}$. This proves the Lemma.

Applying the Lemma repeatedly yields an infinite strictly descending chain of $\mathfrak{p}$-primary components, each giving a distinct irredundant primary representation of $\mathfrak{a}$.
