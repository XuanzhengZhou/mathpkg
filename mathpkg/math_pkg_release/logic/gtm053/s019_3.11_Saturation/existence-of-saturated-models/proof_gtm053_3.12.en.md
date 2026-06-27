---
role: proof
locale: en
of_concept: existence-of-saturated-models
source_book: gtm053
source_chapter: "3"
source_section: "3.12-3.13"
---

**Proof of (i).** We use a standard construction. Assume that $T$ has infinite models. Let $\mathbf{A}_0$ be any model of $T$. We construct an elementary chain $\mathbf{A}_0 \prec \mathbf{A}_1 \prec \cdots \prec \mathbf{A}_\alpha \prec \cdots$ for $\alpha < \kappa^+$ as follows. At a successor stage $\alpha+1$, enumerate all $1$-types over all subsets of $A_\alpha$ of cardinality $< \kappa$. By the compactness theorem and the fact that $\text{card}(T) \leq \kappa$, each such type can be realized in an elementary extension of $\mathbf{A}_\alpha$ of size at most $\text{card}(A_\alpha) + \kappa$. By iterating this process and taking unions at limit ordinals, we obtain a $\kappa^+$-chain whose union $\mathbf{A}$ is a $\kappa$-saturated model of $T$ of cardinality at most $\kappa^+$.

**Proof of (ii).** Let $\mathbf{A}$ and $\mathbf{B}$ be two saturated models of $T$ with $\text{card}(A) = \text{card}(B) = \kappa$. Enumerate the elements of $A$ as $\{a_\alpha : \alpha < \kappa\}$ and the elements of $B$ as $\{b_\alpha : \alpha < \kappa\}$. We construct by transfinite recursion increasing sequences of subsets $A_\alpha \subseteq A$ and $B_\alpha \subseteq B$, and bijections $f_\alpha : A_\alpha \to B_\alpha$ preserving types.

For $\alpha = 0$, set $A_0 = B_0 = \emptyset$.

For $\alpha = 1$, take $a^0 := a_0$ and choose $b^0$ to be the first element among the $b_i$ satisfying the type $\text{tp}(a^0)$. Such a $b_i$ exists because $\mathbf{B}$ is $\kappa$-saturated.

Now assume that $A_\alpha = \{a^j : j < \alpha\}$ and $B_\alpha = \{b^j : j < \alpha\}$ have been constructed, satisfying the condition

$$\text{tp}(a^{j_1}, \ldots, a^{j_m}) = \text{tp}(b^{j_1}, \ldots, b^{j_m})$$

for any finite sequences $0 \leq j_1 < \cdots < j_m < \alpha$.

We introduce constant symbols $c^j$ naming the $a^j$ in $\mathbf{A}$ and $b^j$ in $\mathbf{B}$. Set $C_\alpha = \{c^j : j < \alpha\}$.

- If $\alpha$ is of the form $\delta + 2n$ (where $\delta$ is a limit ordinal and $n \in \omega$), the element $a_{\delta+n}$ is the next element to be added from $A$. If $a_{\delta+n} \notin A_\alpha$, we set $a^\alpha := a_{\delta+n}$. (If already $a_{\delta+n} \in A_\alpha$, we skip this step.) Then we choose $b^\alpha$ to be the first element among the $b_i$ satisfying the type $\text{tp}(a^\alpha / C_\alpha)$. Such a $b_i$ exists since $\text{card}(C_\alpha) < \kappa$ and $\mathbf{B}$ is $\kappa$-saturated.

- If $\alpha$ is of the form $\delta + 2n + 1$, symmetrically, the element $b_{\delta+n}$ is the next to be added from $B$. If $b_{\delta+n} \notin B_\alpha$, we set $b^\alpha := b_{\delta+n}$ and choose $a^\alpha \in A$ to be the first element among the $a_i$ satisfying the type $\text{tp}(b^\alpha / C_\alpha)$. Such an $a_i$ exists by $\kappa$-saturation of $\mathbf{A}$.

This alternating construction ensures that when we reach $\alpha = \kappa$, the map $a^j \mapsto b^j$ defines an isomorphism $\mathbf{A} \cong \mathbf{B}$.
