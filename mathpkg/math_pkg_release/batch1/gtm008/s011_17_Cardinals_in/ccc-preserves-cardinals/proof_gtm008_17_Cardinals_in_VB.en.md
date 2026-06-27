---
role: proof
locale: en
of_concept: ccc-preserves-cardinals
source_book: gtm008
source_chapter: "17"
source_section: "Cardinals in V^{(B)}"
---

The proof proceeds by contradiction using the $\gamma$-chain condition. Given a cardinal $\alpha$, assume that $[\text{Card}(\check{\alpha})] \neq 1$, so there exists a nonzero $b \in B$ with $b \leq \llbracket \neg \text{Card}(\check{\alpha}) \rrbracket$. Then

$$b \leq \llbracket (\exists f)(\exists \beta < \check{\alpha}) [f: \check{\beta} \rightarrow \check{\alpha} \land \mathcal{W}(f) = \check{\alpha}] \rrbracket.$$

There exist $\beta < \alpha$, $f \in V^{(B)}$, and $0 < b' \leq b$ such that

$$b' \leq \llbracket f: \check{\beta} \rightarrow \check{\alpha} \rrbracket \land \llbracket \mathcal{W}(f) = \check{\alpha} \rrbracket.$$

Since $\alpha$ is a cardinal, $\bar{\beta} < \alpha$ and $\bar{\alpha} = \alpha$. Let $A_{\xi} = \{\eta < \alpha \mid b' \cdot \llbracket f(\check{\xi}) = \check{\eta} \rrbracket \neq 0\}$ for $\xi < \beta$. Then

$$b' \leq \llbracket \mathcal{W}(f) = \check{\alpha} \rrbracket = \llbracket (\forall \eta < \check{\alpha})(\exists \xi < \check{\beta}) [f(\check{\xi}) = \check{\eta}] \rrbracket.$$

Hence $\alpha = \bigcup_{\xi < \beta} A_{\xi}$. Since $\beta < \alpha$ and $\alpha$ is a cardinal, $\bar{\beta} \cdot \gamma < \alpha$ for all $\gamma < \alpha$. Therefore there exists some $\xi_* < \beta$ such that $\bar{A}_{\xi_*} > \gamma$, since otherwise $(\forall \xi_* < \beta)[\bar{A}_{\xi_*} \leq \gamma]$ would imply $\bar{\alpha} \leq \bar{\beta} \cdot \gamma < \alpha$, a contradiction.

Consider

$$S = \{b' \cdot \llbracket f(\check{\xi_*}) = \check{\eta} \rrbracket \mid \eta \in A_{\xi_*}\}.$$

Then for $\eta \in A_{\xi_*}$, $\xi_n = \xi_*$ and hence

$$b' \cdot \llbracket f(\check{\xi_*}) = \check{\eta} \rrbracket = b' \cdot \llbracket f(\check{\xi_n}) = \check{\eta} \rrbracket \neq 0$$

since $b' \leq \llbracket f: \check{\beta} \rightarrow \check{\alpha} \rrbracket$ and $\llbracket \xi_* = \xi_n \rrbracket = 1$.

Therefore elements of $S$ are nonzero. Moreover, if $\eta_1, \eta_2 \in A_{\xi_*}$ and $\eta_1 \neq \eta_2$,

$$b' \cdot \llbracket f(\check{\xi_*}) = \check{\eta}_1 \rrbracket \cdot \llbracket f(\check{\xi_*}) = \check{\eta}_2 \rrbracket \leq \llbracket \check{\eta}_1 = \check{\eta}_2 \rrbracket = 0.$$

Therefore elements of $S$ are mutually disjoint and $|S| > \gamma$. But the existence of such an $S$ contradicts the assumption that $B$ satisfies the $\gamma$-chain condition. Taking $\gamma = \aleph_0$ gives the c.c.c. case.
