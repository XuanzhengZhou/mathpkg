---
role: proof
locale: en
of_concept: theorem-22-27-4-if-then
source_book: gtm008
source_chapter: "22"
source_section: "22 The Completion of a Boolean Algebra

For the following let"
---
It is easily seen that the latter implies the former. Now assume $x$ and $p_{\alpha\beta}(y)$ are compatible.

$$(\exists z \in P_\alpha)[z \leq x \land z \in [p_{\alpha\beta}(y)]_{P_\alpha} = p_{\alpha\beta}'[y]_{P_\beta}] \quad \text{by 4.}$$

Therefore

$$(\exists u \in P_\beta)[u \leq y \land z = p_{\alpha\beta}(u)].$$

$$p_{\alpha\beta}(u) \leq x \rightarrow u \leq x. \quad (\text{Use 4*.})$$

So, $x$ and $y$ are compatible.

Remark. A weakly normal limiting system is obtained from a normal limiting system by replacing 4 by 4'. Actually, what we mainly use is a weakly normal limiting system. However, in many cases, the two definitions are equivalent as is seen in the following.
