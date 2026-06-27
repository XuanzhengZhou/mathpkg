---
role: proof
locale: en
of_concept: monotone-class-2
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 1 (Monotone Class Theorem)

**Theorem 1.** Let $\mathcal{A}$ be an algebra. Then

$$\mu(\mathcal{A}) = \sigma(\mathcal{A}),$$

where $\mu(\mathcal{A})$ denotes the smallest monotone class containing $\mathcal{A}$ and $\sigma(\mathcal{A})$ denotes the smallest $\sigma$-algebra containing $\mathcal{A}$.

*Proof.* By Lemma 2, every $\sigma$-algebra is a monotonic class. Hence $\sigma(\mathcal{A})$ is a monotonic class containing $\mathcal{A}$, and therefore

$$\mu(\mathcal{A}) \subseteq \sigma(\mathcal{A}).$$

To prove the reverse inclusion, it suffices to show that $\mu(\mathcal{A})$ is itself a $\sigma$-algebra. Since $\mu(\mathcal{A})$ is by definition a monotonic class, Lemma 2 implies that we need only verify that $\mu(\mathcal{A})$ is an algebra. In other words, we must show that $\mathcal{M} := \mu(\mathcal{A})$ is closed under complementation and finite intersection.

**Step 1: Closure under complementation.** For any $A \in \mathcal{M}$, we wish to show $\overline{A} \in \mathcal{M}$. We employ the principle of appropriate sets. Define

$$\widetilde{\mathcal{M}} = \{B : B \in \mathcal{M}, \overline{B} \in \mathcal{M}\}.$$

Since $\mathcal{A}$ is an algebra and $\mathcal{A} \subseteq \mathcal{M}$, we have $\mathcal{A} \subseteq \widetilde{\mathcal{M}}$. Moreover, one readily checks that $\widetilde{\mathcal{M}}$ is a monotonic class. Because $\mathcal{M}$ is the smallest monotonic class containing $\mathcal{A}$, it follows that $\widetilde{\mathcal{M}} = \mathcal{M}$. Thus every set in $\mathcal{M}$ has its complement also in $\mathcal{M}$.

**Step 2: Closure under finite intersection.** For a fixed $A \in \mathcal{M}$, define

$$\mathcal{M}_A = \{B \in \mathcal{M} : A \cap B \in \mathcal{M}\}.$$

From the identities

$$\lim \downarrow (A \cap B_n) = A \cap \lim \downarrow B_n, \qquad \lim \uparrow (A \cap B_n) = A \cap \lim \uparrow B_n,$$

it follows that $\mathcal{M}_A$ is a monotonic class. Moreover, the symmetry condition

$$(A \in \mathcal{M}_B) \Longleftrightarrow (B \in \mathcal{M}_A)$$

is easily verified.

Now let $A \in \mathcal{A}$. Since $\mathcal{A}$ is an algebra, for every $B \in \mathcal{A}$ the intersection $A \cap B \in \mathcal{A}$, and therefore

$$\mathcal{A} \subseteq \mathcal{M}_A \subseteq \mathcal{M}.$$

But $\mathcal{M}_A$ is a monotonic class and $\mathcal{M}$ is the smallest monotonic class containing $\mathcal{A}$. Hence $\mathcal{M}_A = \mathcal{M}$ for all $A \in \mathcal{A}$. The symmetry condition (2) then yields

$$(A \in \mathcal{M}_B) \Longleftrightarrow (B \in \mathcal{M}_A = \mathcal{M})$$

whenever $A \in \mathcal{A}$ and $B \in \mathcal{M}$. Consequently, if $A \in \mathcal{A}$, then $A \in \mathcal{M}_B$ for every $B \in \mathcal{M}$. Since $A$ is an arbitrary set in $\mathcal{A}$, it follows that

$$\mathcal{A} \subseteq \mathcal{M}_B \subseteq \mathcal{M}.$$

Therefore for every $B \in \mathcal{M}$ we have $\mathcal{M}_B = \mathcal{M}$, i.e., if $B \in \mathcal{M}$ and $C \in \mathcal{M}$, then $C \cap B \in \mathcal{M}$.

**Conclusion.** We have shown that $\mathcal{M} = \mu(\mathcal{A})$ is closed under complementation and under finite intersection (and therefore under finite unions as well). Hence $\mathcal{M}$ is an algebra. Since it is also a monotonic class, Lemma 2 implies that $\mathcal{M}$ is a $\sigma$-algebra containing $\mathcal{A}$. By minimality of $\sigma(\mathcal{A})$, we obtain

$$\sigma(\mathcal{A}) \subseteq \mu(\mathcal{A}).$$

Combined with the earlier inclusion, $\mu(\mathcal{A}) = \sigma(\mathcal{A})$. $\square$
