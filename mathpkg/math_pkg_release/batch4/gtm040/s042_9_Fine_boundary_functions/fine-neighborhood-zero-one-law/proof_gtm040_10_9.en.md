---
role: proof
locale: en
of_concept: fine-neighborhood-zero-one-law
source_book: gtm040
source_chapter: "10"
source_section: "9. Fine boundary functions"
---

**Proof.** Consider the $h$-process for $h = K(\cdot, x)$ with $x \in B_e$. By Proposition 10-35, this process disappears with probability zero, so
\[
\Pr^{K(\cdot, x)}[x_n \in S] = 1.
\]

For any set $A \subseteq S^*$, we have
\[
\Pr^{K(\cdot, x)}[x_n \in A \text{ from some time on}]
= \Pr^{K(\cdot, x)}[x_n \in S - A \text{ only finitely often}]
= 1 - \Pr^{K(\cdot, x)}[x_n \in S - A \text{ infinitely often}].
\]

By Lemma 10-46, the only bounded regular functions for the $K(\cdot, x)$-process are the constants. Proposition 5-19 then implies that the event $\{x_n \in S - A \text{ infinitely often}\}$ has probability either $0$ or $1$. Therefore,
\[
\Pr^{K(\cdot, x)}[x_n \in A \text{ from some time on}]
\]
can only take the values $0$ or $1$.

A set $A$ containing $x$ is a fine neighborhood of $x$ precisely when this probability is positive, which by the zero-one law means it equals $1$. Thus the fine neighborhoods of $x$ are exactly those $A$ in $S^*$ containing $x$ with
\[
\Pr^{K(\cdot, x)}[x_n \in A \text{ from some time on}] = 1.
\]
