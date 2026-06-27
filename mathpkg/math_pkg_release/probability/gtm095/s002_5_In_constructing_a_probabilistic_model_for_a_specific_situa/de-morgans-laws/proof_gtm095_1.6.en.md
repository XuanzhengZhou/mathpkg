---
role: proof
locale: en
of_concept: de-morgans-laws-for-events
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of De Morgan's Laws for Events

**Problem 1 (Section 6).** Show the following De Morgan's laws for events:
$$\overline{A \cup B} = \overline{A} \cap \overline{B}, \qquad \overline{A \cap B} = \overline{A} \cup \overline{B}.$$

**Proof.** Let $(\Omega, \mathcal{A}, \mathrm{P})$ be a probability space with sample space $\Omega$ and events $A, B \in \mathcal{A}$. The complement is taken with respect to $\Omega$: $\overline{A} = \Omega \setminus A$.

**First law: $\overline{A \cup B} = \overline{A} \cap \overline{B}$.**

An outcome $\omega \in \Omega$ belongs to $\overline{A \cup B}$ if and only if $\omega \notin A \cup B$, which means $\omega \notin A$ and $\omega \notin B$. Equivalently, $\omega \in \overline{A}$ and $\omega \in \overline{B}$, i.e., $\omega \in \overline{A} \cap \overline{B}$. Thus:
$$\overline{A \cup B} = \{\omega \in \Omega : \omega \notin A \text{ and } \omega \notin B\} = \overline{A} \cap \overline{B}.$$

**Second law: $\overline{A \cap B} = \overline{A} \cup \overline{B}$.**

An outcome $\omega \in \Omega$ belongs to $\overline{A \cap B}$ if and only if $\omega \notin A \cap B$, which means $\omega \notin A$ or $\omega \notin B$ (or both). Equivalently, $\omega \in \overline{A}$ or $\omega \in \overline{B}$, i.e., $\omega \in \overline{A} \cup \overline{B}$. Thus:
$$\overline{A \cap B} = \{\omega \in \Omega : \omega \notin A \text{ or } \omega \notin B\} = \overline{A} \cup \overline{B}.$$

**Generalization to $n$ events.** By induction, De Morgan's laws extend to any finite collection $A_1, \ldots, A_n$:
$$\overline{\bigcup_{i=1}^n A_i} = \bigcap_{i=1}^n \overline{A_i}, \qquad \overline{\bigcap_{i=1}^n A_i} = \bigcup_{i=1}^n \overline{A_i}.$$

**Remark.** The same identities hold for arbitrary (possibly infinite) collections of sets; the proof uses the same logical negation of quantifiers. In the text, these laws appear as part of the foundational set-algebraic properties of events alongside commutativity, associativity, distributivity, and idempotency of $\cup$ and $\cap$.
