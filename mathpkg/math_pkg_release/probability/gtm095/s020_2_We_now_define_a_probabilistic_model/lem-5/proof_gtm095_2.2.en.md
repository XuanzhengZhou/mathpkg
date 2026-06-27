---
role: proof
locale: en
of_concept: lem-5
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Lemma 5 (Trace of Generated $\sigma$-Algebra)

**Lemma 5.** Let $\mathcal{E}$ be a class of subsets of $\Omega$, let $B \subseteq \Omega$, and define the trace class

$$\mathcal{E} \cap B = \{A \cap B : A \in \mathcal{E}\}.$$

Then

$$\sigma(\mathcal{E} \cap B) = \sigma(\mathcal{E}) \cap B,$$

where $\sigma(\mathcal{E}) \cap B = \{A \cap B : A \in \sigma(\mathcal{E})\}$.

*Proof.* **Inclusion $\subseteq$.** Since $\mathcal{E} \subseteq \sigma(\mathcal{E})$, we have

$$\mathcal{E} \cap B \subseteq \sigma(\mathcal{E}) \cap B.$$

But $\sigma(\mathcal{E}) \cap B$ is a $\sigma$-algebra (on the subspace $B$). Indeed, it is the trace $\sigma$-algebra of $\sigma(\mathcal{E})$ on $B$. Hence the minimality of the generated $\sigma$-algebra yields

$$\sigma(\mathcal{E} \cap B) \subseteq \sigma(\mathcal{E}) \cap B.$$

**Inclusion $\supseteq$.** To prove the opposite inclusion, we again use the principle of appropriate sets. Define

$$\mathcal{C}_B = \{A \in \sigma(\mathcal{E}) : A \cap B \in \sigma(\mathcal{E} \cap B)\}.$$

Since $\sigma(\mathcal{E})$ and $\sigma(\mathcal{E} \cap B)$ are $\sigma$-algebras, it is straightforward to verify that $\mathcal{C}_B$ is also a $\sigma$-algebra. Moreover, for any $E \in \mathcal{E}$, we have $E \cap B \in \mathcal{E} \cap B \subseteq \sigma(\mathcal{E} \cap B)$, so $E \in \mathcal{C}_B$. Hence

$$\mathcal{E} \subseteq \mathcal{C}_B \subseteq \sigma(\mathcal{E}).$$

Taking $\sigma$ of both sides and using that $\mathcal{C}_B$ is already a $\sigma$-algebra,

$$\sigma(\mathcal{E}) \subseteq \sigma(\mathcal{C}_B) = \mathcal{C}_B \subseteq \sigma(\mathcal{E}),$$

so $\sigma(\mathcal{E}) = \mathcal{C}_B$. By the definition of $\mathcal{C}_B$, this means that for every $A \in \sigma(\mathcal{E})$ we have $A \cap B \in \sigma(\mathcal{E} \cap B)$. In other words,

$$\sigma(\mathcal{E}) \cap B \subseteq \sigma(\mathcal{E} \cap B).$$

Combining both inclusions, we obtain $\sigma(\mathcal{E} \cap B) = \sigma(\mathcal{E}) \cap B$. $\square$
