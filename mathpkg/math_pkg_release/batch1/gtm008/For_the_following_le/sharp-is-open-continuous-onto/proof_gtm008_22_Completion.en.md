---
role: proof
locale: en
of_concept: sharp-is-open-continuous-onto
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

**1.** We compute:
$$b_1 \in (\#^{-1})``[b_0] \leftrightarrow \#(b_1) \leq b_0 \leftrightarrow b_1 \leq i(b_0) \leftrightarrow b_1 \in [i(b_0)],$$
where the second equivalence uses Theorem 22.10(4). Hence $(\#^{-1})``[b_0] = [i(b_0)]$.

**2.** $\#$ is continuous because of 1: the preimage of every basic open set $[b_0]$ is the basic open set $[i(b_0)]$ in $P_1$, which is open.

We show that $\#``[b_1]$ is open for every $b_1 \in B_1$. Let $b_0 \in \#``[b_1]$. If $b_0' \leq b_0$, then since $\#$ is order preserving, $b_0' \leq \#(b_1)$. Hence
$$b_0' = b_0' \cdot \#(b_1) = \#(i(b_0') \cdot b_1) \quad \text{(by Theorem 22.10.5)},$$
which lies in $\#``[b_1]$. Therefore $[b_0] \subseteq \#``[b_1]$, proving that $\#``[b_1]$ is open.

$\#$ is onto by Theorem 22.10(3): for any $b_0 \in P_0$, $\#(i(b_0)) = b_0$.

**3.** By property 1, the preimage under $\#$ of a basic open set $[b_0]$ is $[i(b_0)]$. The complete monomorphism associated with $\#$ sends $[b_0]$ to the regular open set corresponding to $\#^{-1}``[b_0]$, which is exactly $i(b_0)$. Thus the associated monomorphism is $i$.
