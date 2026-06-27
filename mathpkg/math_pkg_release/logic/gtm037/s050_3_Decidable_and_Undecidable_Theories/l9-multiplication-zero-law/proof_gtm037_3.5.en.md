---
role: proof
locale: en
of_concept: l9-multiplication-zero-law
source_book: gtm037
source_chapter: "3"
source_section: "3.5 Decidable and Undecidable Theories"
---

**Proof of Lemma 16.46.** From Lemma 16.41 we obtain directly that $\mathcal{L}_9 \models v_0 \cdot 0 = 0$.

By the defining axiom of $\cdot$ in Definition 16.45, we have for any $v_0$:

$$
v_0 \cdot 0 = v_2 \leftrightarrow \pi(v_0, 0, v_2) \lor [\neg \exists v_3 \pi(v_0, 0, v_3) \land \Omega v_0 \land v_2 = \{1\}] \lor [\neg \exists v_3 \pi(v_0, 0, v_3) \land \neg \Omega v_0 \land 0 \neq 0 \land v_2 = \{1\}] \lor [\neg \exists v_3 \pi(v_0, 0, v_3) \land \neg \Omega v_0 \land 0 = 0 \land v_2 = 0].
$$

The third disjunct is impossible since $0 \neq 0$ is false. For the fourth disjunct, $0 = 0$ is true, and if $\neg \Omega v_0$ and $\neg \exists v_3 \pi(v_0, 0, v_3)$ both hold, then the fourth disjunct forces $v_2 = 0$. Lemma 16.41 (which characterizes $\pi$ for multiplication by zero) ensures that the relevant conditions are met, yielding $v_0 \cdot 0 = 0$. $\square$
