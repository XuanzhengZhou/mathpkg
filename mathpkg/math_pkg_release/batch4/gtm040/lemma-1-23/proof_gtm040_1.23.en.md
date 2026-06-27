---
role: proof
locale: en
of_concept: lemma-1-23
source_book: gtm040
source_chapter: "1"
source_section: "23"
---

**Proof:** We prove only the first and third assertions. First we observe that $(A_1 \cup A_2) \oplus (B_1 \cup B_2) \subset (A_1 \oplus B_1) \cup (A_2 \oplus B_2)$. For suppose $x \in (A_1 \cup A_2) \oplus (B_1 \cup B_2)$. We may assume without loss of generality that $x \in A_1 \cup A_2$ but $x \notin B_1 \cup B_2$. If $x \in A_1$, then $x \notin B_1$ so that $x \in A_1 \oplus B_1$. Similarly if $x \in A_2$, then $x \in A_2 \oplus B_2$ and the containment is established. The first assertion of the lemma now follows by applying Lemmas 1-20 and 1-21. For the third part, we have

$$B \oplus A = (A \cap \tilde{B}) \cup (\tilde{A} \cap B)$$

and

$$\tilde{B

we have $A_n \cup B_n \rightarrow A \cup B$, $A_n \cap B_n \rightarrow A \cap B$, and $\tilde{A}_n \rightarrow \tilde{A}$. The limit of $\mu(C_n)$ is established by the inequalities

$$\mu(C_n) \leq d(C_n, C) + \mu(C)$$

and

$$\mu(C) \leq d(C_n, C) + \mu(C_n).$$
