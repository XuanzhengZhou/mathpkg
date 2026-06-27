---
role: proof
locale: en
of_concept: display-lemma
source_book: gtm053
source_chapter: "I"
source_section: "11"
---

If $Q$ has number $k$, then the display of $Q$ has number $k \cdot 10^k$. This follows from the numbering scheme: the symbol $\bar{1}$ is assigned the digit 9. The label $*Q*$ is the term $\bar{1} \cdots \bar{1}$ repeated $n(Q)$ times, which represents the number $n(Q)$. The display $Q * Q*$ is the concatenation of the expression $Q$ followed by its label.

The number of $Q * Q*$ is computed as:

$$n(Q * Q*) = n(Q \underbrace{\bar{1} \cdots \bar{1}}_{n(Q) \text{ times}})$$

$$= (n(Q) - 1)10^{n(Q)} + \underbrace{9 \cdots 9}_{n(Q) \text{ times}} + 1$$

$$= (n(Q) - 1)10^{n(Q)} + (10^{n(Q)} - 1) + 1$$

$$= n(Q) \cdot 10^{n(Q)}.$$

(Here we use the fact that $\bar{1}$ has number nine, which is why the label $\bar{1}\cdots\bar{1}$ repeated $k$ times has number $k$.)

Now, an expression $Q$ with number $k$ satisfies $P_E$ if and only if $P_E(\bar{k})$ is true. By definition, $P_E(x) = P(x \cdot 10^x)$, so this is equivalent to $P(\bar{k} \cdot 10^{\bar{k}})$ being true. Since $\bar{k} \cdot 10^{\bar{k}}$ represents the number $k \cdot 10^k = n(Q * Q*)$, this holds if and only if the display $Q * Q*$ satisfies $P$, i.e., $Q$ is displayed in $P$. Thus the set of expressions satisfying $P_E$ coincides with the set of expressions displayed in $P$.
