---
role: proof
locale: en
of_concept: null-basic-example-entry-probabilities
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

Since a null chain with high probability will be outside any given finite set after a long time, any finite set $E$ must be re-entered from the left. The entry distribution $\lambda^E$ gives the limiting probability of entering $E$ at each state $i \in E$, normalized so that $\sum_i \lambda_i^E = 1$.

For the basic example, because the chain can only move right or jump to 0, entering a finite set $E$ from the left means the chain comes from states smaller than those in $E$. But the only way to reach $E$ from the left is to pass through 0 and then step through each intermediate state. Therefore the entry must occur at the smallest state of $E$, giving $\lambda_i^E = 1$ for the first state of $E$ and 0 otherwise.

For the two-point entry probability $^i\lambda_j$ (the probability that starting from $i$, the chain eventually enters at $j$), the chain can only enter state $j$ from state $j-1$ by moving right, or from 0. In the null case, after a long time the chain is almost surely to the right of any fixed finite set, so re-entering the finite region must pass through 0. Entry from states to the right of $j$ cannot land at $j$ without passing through larger states first. Hence $^i\lambda_j = 1$ if $j < i$ (entering from the left) and 0 if $j \geq i$.

For the reverse chain $\hat{P}$, the deterministic leftward motion means the process enters finite sets from the right, giving the dual formulas.
