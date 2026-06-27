---
role: proof
locale: en
of_concept: theorem-8-41
source_book: gtm040
source_chapter: "8"
source_section: "41"
---

**Proof:** For existence, set

$$\bar{h} = B^E \binom{h_E}{0}.$$

The product is defined, since $h_E$ is bounded and $B^E$ has row sums one. Then the restriction of $\bar{h}$ to $E$ is $h_E$ because $(B^E)_{ij} = \delta_{ij}$ for $i$ and $j$ in $E$. Moreover,

$$(I - P)\bar{h} = (I - P)B^E \binom{h_E}{0} = \binom{I - P^E}{0} \binom{h_E}{0} = \binom{(I - P^E)h_E}{0},$$

so that $\bar{h}$ is regular outside of $E$; associativity is justified in the triple product because $(I + P)B^E \binom{|h_E|}{0}$ is finite-valued.

For uniqueness, let

$$k = \binom{h_E}{\bar{k}}$$

be another such bounded function. Then $\bar{h} - k$ is a bounded

Theorem 8-42: Let $E$ be an arbitrary set of states and suppose that $h$ is a finite-valued function such that $h = B^E h$. Then the supremum of the values of $h$ is equal to the supremum of the values of $h$ on $E$. If the states of $\tilde{E}$ communicate in $^E P$, if $^E P$ is absorbing, and if $h$ assumes its maximum on $\tilde{E}$, then $h$ is constant on $\tilde{E}$.

Remark: Corresponding results hold for infima' by replacing $h$ by $-h$.

Proof:

$$h_i = \sum_{j \in E} B^E_{ij} h_j$$
$$\leq \sum_{j \in E} B^E_{ij} \left( \sup_{j \in E} h_j \right) \leq \sup_{j \in E} h_j.$$

Suppose that $h$ assumes its maximum on $\tilde{E}$, that $^E P$ is absorbing, and that the states of $\tilde{E}$ communicate in $^E P$. Let $i$ be a state where the maximum is assumed, and let $k$ be any state of $E$ that can be reached in $^E P$ from $\tilde{E}$. Since the transient states of $^E P$ communicate, we have $B^E_{ik} > 0$. Moreover,

$$h_i = B^E_{ik} h_k + \sum_{j \neq k} B^E_{ij} h_j$$
$$\leq B^E_{ik} h_k + h_i \sum_{j \neq k} B^E_{ij} \quad \text{since } h_j \leq h_i$$
$$= B^E_{ik} h_k + h_i (1 - B^E_{ik}) \quad \text{since } B^E_1 = 1$$
$$= h_i - B^E_{ik} (h_i - h_k).$$

Therefore, $h_i = h_k$ for all such $k$. Then for any $m \in \tilde{E}$, $B^E_{mj} > 0$ precisely for those $j$

If $h$ is a bounded function regular outside of $E$, then $h$ cannot assume its maximum on $\tilde{E}$ unless $h$ is constant everywhere.

Proof: By Theorem 8-41, $h$ is the unique solution to the Dirichlet problem for the function $h_E$. Hence

$$h = B^E \binom{h_E}{0}.$$

Multiplying through by $B^E$ and applying Proposition 5-8, we have

$$B^E h = B^E B^E \binom{h_E}{0} = B^E \binom{h_E}{0} = h.$$

By Theorem 8-42, $h$ is constant on $\tilde{E}$. As shown in the proof of that theorem, $h$ assumes the same constant value at every state of $E$ which can be reached in $^E P$ from $\tilde{E}$.

The result that follows is the Principle of Domination.

Theorem 8-45: Let $h$ be a finite-valued non-negative superregular function, and let $g = Nf$ be a potential. If $h$ dominates $g$ on the support of $f^+$, then $h$ dominates $g$ everywhere. If, in addition, $h$ is a potential $Nf\bar{f}$, then $\alpha f \leq \alpha \bar{f}$.

Proof: If $g$ is a pure potential supported in $E$, then $g = B^E g$ by Proposition 8-19. But by Proposition 8-16, $B^E g$ is the pointwise infimum of all non-negative superregular functions which dominate $g$ on $E$. Thus the first half is proved if $g$ is a pure potential. For arbitrary $g$, write $g = Nf^+ - Nf^-$. We have $Nf^+ - Nf^- \leq h$ on the support of $f^+$, so that

$$Nf^+ \leq h + Nf^-$$

on the support of $f^+$. Applying the special case to the superregular function $h + Nf^-$ and the potential $Nf^+$, we

Next we prove the Principle of Balayage.

Theorem 8-46: If $g$ is a pure potential and if $E$ is any set of states, then there is a unique pure potential $\bar{g}$ with support in $E$ such that $\bar{g} = g$ on $E$. The potential $\bar{g}$ satisfies $\bar{g} \leq g$ everywhere, and its total charge does not exceed the total charge of $g$.

Proof: For existence, let $\bar{g} = B^E g$. Then $\bar{g} \leq g$, $\bar{g}_E = g_E$, and $\bar{g}$ is superregular by conclusions (1) and (3) of Proposition 8-16. By Proposition 8-25, $\bar{g}$ is a potential, and the total charge of $\bar{g}$ is less than or equal to that of $g$.

For uniqueness, if $h$ were another such potential, we would have

$$\bar{g} = B^E \bar{g} = B^E h = h$$

by Proposition 8-15 and the fact that $\bar{g}_E = g_E = h_E$.

If $E$ is any set and if $g$ is a pure potential, we refer to the potential $\bar{g}$ of Theorem 8-46 as the balayage potential of $g$ on $E$.

Corollary 8-47: The balayage potential $\bar{g} = B^E g$ of $g$ on $E$ is the pointwise infimum of all pure potentials which dominate $g$ on $E$.

Proof: Apply conclusion (2) of Proposition 8-16.

Corollary 8-48: The balayage potential of $g$ on $E$ is the supremum of all pure potentials with support in $E$ which are dominated by $g$ on $E$.

Proof: Certainly the balayage potential does have the stated property. Thus let $\bar{g} = B^E g$ and let $h$ be a potential with support in $E$ and with $h_E \leq g_E$. Then by Proposition 8-19,

for all $\beta$, then

$$P(\inf h_{\beta}) \leq Ph_{\beta} \leq h_{\beta}$$

for all $\beta$, so that

$$P(\inf h_{\beta}) \leq \inf h_{\beta}.$$
