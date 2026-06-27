---
role: proof
locale: en
of_concept: generated-sigma-ring-section-formula
source_book: gtm018
source_chapter: "I"
source_section: "5"
---

Denote by $\mathbf{C}$ the class of all sets of the form $B \cup (C - A)$, where

$$B \in \mathbf{S}(\mathbf{E} \cap A) \text{ and } C \in \mathbf{S}(\mathbf{E}).$$

We first verify that $\mathbf{C}$ is a $\sigma$-ring. If $E \in \mathbf{E}$, then the decomposition

$$E = (E \cap A) \cup (E - A),$$

together with $E \cap A \in \mathbf{E} \cap A \subset \mathbf{S}(\mathbf{E} \cap A)$ and $E \in \mathbf{S}(\mathbf{E})$, shows that $E \in \mathbf{C}$. Therefore $\mathbf{E} \subset \mathbf{C}$.

Since $\mathbf{C}$ is a $\sigma$-ring containing $\mathbf{E}$, it follows that $\mathbf{S}(\mathbf{E}) \subset \mathbf{C}$, and therefore

$$\mathbf{S}(\mathbf{E}) \cap A \subset \mathbf{C} \cap A.$$

Now observe that $\mathbf{C} \cap A = \mathbf{S}(\mathbf{E} \cap A)$, because for any $B \cup (C - A) \in \mathbf{C}$, its intersection with $A$ is $B \cap A = B$ (since $B \subset A$ for $B \in \mathbf{S}(\mathbf{E} \cap A)$). Hence

$$\mathbf{S}(\mathbf{E}) \cap A \subset \mathbf{S}(\mathbf{E} \cap A).$$

For the reverse inclusion, note that $\mathbf{S}(\mathbf{E}) \cap A$ is a $\sigma$-ring (as the intersection of a $\sigma$-ring with a fixed set) and

$$\mathbf{E} \cap A \subset \mathbf{S}(\mathbf{E}) \cap A.$$

Therefore $\mathbf{S}(\mathbf{E} \cap A) \subset \mathbf{S}(\mathbf{E}) \cap A$, completing the proof.
