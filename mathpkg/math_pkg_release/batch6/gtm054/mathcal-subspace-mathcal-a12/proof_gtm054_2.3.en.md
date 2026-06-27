---
role: proof
locale: en
of_concept: mathcal-subspace-mathcal-a12
source_book: gtm054
source_chapter: "2"
source_section: "IIA"
---

(a) Let $\mathcal{A} = \mathcal{B} \oplus \mathcal{C}$ and $B = \text{Fnd}(\mathcal{B})$. By these assumptions and A11, $\mathcal{B} \subseteq \mathcal{P}(B) \cap \mathcal{A} \subseteq \pi_B[\mathcal{A}]$. It suffices to show that $\pi_B[\mathcal{A}] \subseteq \mathcal{B}$.

Let $S \in \mathcal{A}$. Then $S = S_1 + S_2$ for some $S_1 \in \mathcal{B}$ and $S_2 \in \mathcal{C}$. By definition of $\oplus$, $B \cap S_2 = \varnothing$. Hence

$$\pi_B(S) = S \cap B = S_1 \in \mathcal{B}.$$

(b) Let $B \in \mathcal{P}(U)$ and assume that $\pi_B[\mathcal{A}] = \mathcal{P}(B) \cap \mathcal{A}$.
By A11, $\mathcal{P}(U + B) \cap

IIB Ordering

A partial order on a finite or infinite set $U$ is a relation $R$ on $U$ which is reflexive, transitive, and antisymmetric, i.e.,

$$(x, y) \in R \text{ and } (y, x) \in R \text{ imply } x = y.$$

A partial order is frequently designated by a symbol such as $\leq$ which will be used in the following way. Instead of writing: $(x, y) \in \leq$, one writes: $x \leq y$. In this context, the symbol $<$ will be used to mean: $x \leq y$ and $x \neq y$. (Compare the use of $\subseteq$ and $\subseteq$.) Clearly $<$ is also a relation on $U$.

A pair $(U, \leq)$, where $U$ is a finite or infinite set and $\leq$ is a partial order on $U$, is called a partially-ordered set. $(U, \leq)$ is a totally-ordered set and $\leq$ is a total order if either $x \leq y$ or $y \leq x$ for all $x, y \in U$. Isomorphism between sets with relations was defined in §I A.
