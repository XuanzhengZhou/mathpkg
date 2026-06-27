---
role: proof
locale: en
of_concept: bounded-equational-presentation-is-algebraic
source_book: gtm026
source_chapter: "1"
source_section: "1.27"
---

**Proof.** As just mentioned above, the proof of 1.26 shows that $U$ creates limits and that $U$ creates quotients of congruences. By 1.22 (1) it suffices to prove that for an arbitrary set $S$, $U$ satisfies the solution set condition at $S$. Given an $(\Omega, E)$-algebra $(X, \delta)$ and a function $f: S \longrightarrow X$ let $A$ be the intersection of all $\Omega$-subalgebras of $(X, \delta)$ containing $f(S)$. It is obvious that $A$ is itself an $\Omega$-subalgebra. Moreover, if $\{p, q\} \in E$ is an $n$-ary equation then naturality squares (where $\bar{\delta}$ is the subalgebra structure on $A$ and $i: A \longrightarrow X$ is the inclusion map) prove that $(A, \bar{\delta})$ is an $(\Omega, E)$-algebra, since $i$ is a monomorphism. We clearly have a factorization $S \to A \to X$.

By the condition that $(\Omega, E)$ is bounded, $\bar{\delta}$ ranges over a small set once $A$ is fixed. To complete the proof, it is enough to show that there exists a cardinal number $\alpha$, depending only on $\Omega$ and $S$, such that the cardinality of $A$ is $\leqslant \alpha$.

$\alpha$ is constructed as follows. Let $\alpha_1$ be any infinite cardinal $> \text{card}(S)$ and $> \text{card}(\Omega_n)$ for all $n$. This is possible because $(\Omega, E)$ is bounded. Let $\alpha_2$ be any infinite cardinal $>$ every $n$ for which $\Omega_n$ is non-empty. This is possible, again because $(\Omega, E)$ is bounded. Define $\alpha = \alpha_1^{\alpha_2}$. We will show that $\text{card}(A) \leqslant \alpha$.

**Step 1.** Construct a transfinite tower $A_\beta$ of subsets of $X$, starting with $A_0 = f(S)$. For a successor ordinal $\beta + 1$, define $A_{\beta+1} = A_\beta \cup \bigcup(\delta_\omega(A_\beta^n): \omega \in \Omega_n)$. For a limit ordinal, take the union of previous stages. Set $A_\alpha = \bigcup_{\beta < \alpha} A_\beta$.

**Step 2.** Show $A = A_\alpha$. By transfinite induction, each $A_\beta \subseteq A$. For the reverse inclusion, show $A_\alpha$ is an $\Omega$-subalgebra: for any $\omega \in \Omega_n$ and $a_i \in A_\alpha$, each $a_i \in A_{\beta(i)}$ for some $\beta(i) < \alpha$. Let $\bar{\beta} = \text{Sup}(\beta(i))$. Since $\alpha$ is a regular cardinal (being $\alpha_1^{\alpha_2}$ with $\alpha_1, \alpha_2$ infinite), $\bar{\beta} < \alpha$. Therefore $\delta_\omega(a_i) \in A_{\bar{\beta}+1} \subset A_\alpha$.

**Step 3.** $\text{card}(A_\alpha) \leqslant \alpha$. We have $\text{card}(A_0) \leqslant \text{card}(S) < \alpha_1 \leqslant \alpha$. For $0 < \beta < \alpha$, assuming $\text{card}(A_\gamma) \leqslant \alpha$ for all $\gamma < \beta$, we have $\text{card}(\bigcup(A_\gamma : \gamma < \beta)) \leqslant \beta \times \alpha \leqslant \alpha \times \alpha = \alpha$. Therefore, for $\omega \in \Omega_n$,
$$\text{card}(\delta_\omega((\bigcup(A_\gamma : \gamma < \beta))^n)) \leqslant (\beta \times \alpha)^n \leqslant (\alpha \times \alpha)^n = \alpha^n \leqslant \alpha.$$
Therefore,
$$\text{card}(A_\beta) \leqslant \alpha + \text{card}(\bigcup(\Omega_n \times \alpha : \Omega_n \neq \emptyset)) \leqslant \alpha + (\alpha_2 \times \alpha_1 \times \alpha) \leqslant \alpha + \alpha = \alpha.$$
By transfinite induction, $\text{card}(A_\beta) \leqslant \alpha$ for all $\beta < \alpha$. Then $\text{card}(A_\alpha) = \text{card}(\bigcup(A_\beta : \beta < \alpha)) \leqslant \alpha \times \alpha = \alpha$. $\square$
