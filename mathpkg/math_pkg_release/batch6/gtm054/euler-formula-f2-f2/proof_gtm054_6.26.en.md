---
role: proof
locale: en
of_concept: euler-formula-f2-f2
source_book: gtm054
source_chapter: "6"
source_section: "VIA"
---

(Adapted from H. B. Mann and H. J. Ryser [m.6].) We proceed by induction on $|E|$. If $E = \{e\}$, then $|E| \leq q$ and $\Lambda$ admits exactly $|f(e)|$ LDR’s, where $|f(e)| \geq q = q! / (q - 1)!$ as required. The in

LDR's if $q \geq |E|$. To each LDR $\lambda'$ of $\Lambda'$ corresponds the unique LDR $\lambda$ of $\Lambda$ given by

$$\lambda(e) = \begin{cases} \lambda'(e) & \text{if } e \in E'; \\ x_0 & \text{if } e = e_0. \end{cases}$$

As there exist at least $q$ initial choices for $x_0$, $\Lambda$ admits at least $q$ times as many LDR's as $\Lambda'$ does, as required.

Case 2: there exists non-empty $D \subset E$ such that $|D| = |\bigcup_{e \in D} f(e)|$. In this case, for all $e \in D$, one has $q \leq |f(e)| \leq |D| < |E|$. By the induction hypothesis, the subsystem $\Lambda_D$ admits at least $q!$ LDR's. Now form another subsystem $\Theta = (W, g, E + D)$ where $W = V + \bigcup_{e \in D} f(e)$ and $g(e) = f(e) \cap W$ for all $e \in E + D$.

We show that $\Theta$ satisfies F3. Suppose that for some $A \subseteq E + D$ it held that $|A| > |\bigcup_{e \in A} g(e)|$. Since $D \cap A = \varnothing$, our various assumptions give

$$\left| \bigcup_{e \in D + A} f(e) \right| \leq \left| \bigcup_{e \in D} f(e) \right| + \left| \bigcup_{e \in A} f(e) \right|$$

$$< |D| + |A| = |D + A|,$$

contrary to the assumption that $\Lambda$ satisfies F3.

Since $\Theta$ satisfies F3, it satisfies the hypothesis of the theorem with 1 in place of $q$. By the induction hypothesis, $\Theta$ admits at least one LDR $\lambda_1$. (Note: $\lambda_1$ could have been obtained here by the Philip

$\rho(x) \geq q$ for all $x \in V_1$. If $\Gamma$ admits a matching of $V_1$, then the number of such matchings is at least

(a) $q!$ if $q < |V_1|$;
(b) $q! / (q - |V_1|)!$ if $q \geq |V_1|$.
