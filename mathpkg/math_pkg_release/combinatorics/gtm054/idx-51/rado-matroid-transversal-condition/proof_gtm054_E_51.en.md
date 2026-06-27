---
role: proof
locale: en
of_concept: rado-matroid-transversal-condition
source_book: gtm054
source_chapter: "Chapter E: Matroid Theory"
source_section: "Section 51"
---

**Proof of Proposition E6 (Rado).**

*Necessity.* Let $\lambda$ be an LDR of $\Lambda$ and suppose that $\lambda[E] \in \mathcal{I}(\Theta)$. If $F \subseteq E$, then certainly $\lambda[F] \in \mathcal{I}(\Theta)$, because independent sets of a matroid are closed under taking subsets. Moreover, $\lambda[F] \subseteq \bigcup_{e \in F} f(e)$, so
$$|F| = |\lambda[F]| = r(\lambda[F]) \leq r\!\left(\bigcup_{e \in F} f(e)\right),$$
where the first equality follows from $\lambda$ being injective on $F$, and the inequality follows from the monotonicity of the rank function $r$.

*Sufficiency.* Assume the condition holds. We proceed by induction on $|E|$. The base case $|E| = 0$ is trivial.

**Case 1:** For every $F$ with $\varnothing \subset F \subset E$, we have strict inequality:
$$r\!\left(\bigcup_{e \in F} f(e)\right) > |F|.$$

Choose $e_0 \in E$ and pick $x_0 \in f(e_0)$ such that $\{x_0\} \in \mathcal{I}(\Theta)$. (Such an $x_0$ exists because the condition with $F = \{e_0\}$ gives $r(f(e_0)) \geq 1$, hence $f(e_0)$ contains at least one element that is not a loop of $\Theta$.)

Define a new system $\Lambda' = (V + \{x_0\}, f', E + \{e_0\})$ and a new matroid $\Theta' = \Theta_{[V + \{x_0\}]}$ (the restriction of $\Theta$ to $V + \{x_0\}$) with rank function $r'$. For $e \in E + \{e_0\}$, set $f'(e) = f(e) + \{x_0\}$ if $x_0 \in f(e)$, and $f'(e) = f(e)$ otherwise. One verifies that the rank condition continues to hold for $\Lambda'$ and $\Theta'$: for any $F \subseteq E + \{e_0\}$,
$$r'\!\left(\bigcup_{e \in F} f'(e)\right) \geq |F|.$$

By the induction hypothesis, $\Lambda'$ admits an LDR $\lambda'$ such that $\lambda'[E + \{e_0\}] \in \mathcal{I}(\Theta_{[V + \{x_0\}]})$. Define $\lambda: E \to V$ by
$$\lambda(e) = \begin{cases} \lambda'(e) & \text{if } e \in E + \{e_0\}, \\ x_0 & \text{if } e = e_0. \end{cases}$$
Then $\lambda$ is an LDR of $\Lambda$. Finally, since $\{x_0\} \in \mathcal{I}(\Theta)$ and $\lambda'(E + \{e_0\}) \in \mathcal{I}(\Theta_{[V + \{x_0\}]})$, the matroid augmentation property (D12g) implies that $\lambda(E) = \lambda'(E + \{e_0\}) \cup \{x_0\} \in \mathcal{I}(\Theta)$.

**Case 2:** There exists $E_1$ such that $\varnothing \subset E_1 \subset E$ and
$$r\!\left(\bigcup_{e \in E_1} f(e)\right) = |E_1|.$$

Let $\Lambda_1 = (V_1, f_1, E_1) = \Lambda_{E_1}$ be the subsystem restricted to $E_1$. Set $V_2 = V + V_1$, $E_2 = E + E_1$, and define $f_2(e) = f(e) \cap V_2$ for all $e \in E_2$. Let $\Lambda_2 = (V_2, f_2, E_2)$.

By the matroid restriction property (D12c), we may apply the induction hypothesis to $\Lambda_1$ (since $|E_1| < |E|$); there exists an LDR $\lambda_1$ of $\Lambda_1$ such that $\lambda_1[E_1] \in \mathcal{I}(\Theta_{V_1})$.

For any $F \in \mathcal{P}(E_2)$, applying the matroid contraction rank formula (D12d):
$$r_{[V_2]}\!\left(\bigcup_{e \in F} f_2(e)\right) = r\!\left(V + V_2 + \bigcup_{e \in F} f_2(e)\right) - r(V + V_2).$$
Using the original rank condition, one shows this is $\geq |F|$. Thus the induction hypothesis applies to $\Lambda_2$ as well, yielding an LDR $\lambda_2$ of $\Lambda_2$ with $\lambda_2[E_2] \in \mathcal{I}(\Theta_{[V_2]})$.

Combining $\lambda_1$ and $\lambda_2$ yields an LDR $\lambda$ of $\Lambda$ with $\lambda[E] \in \mathcal{I}(\Theta)$, completing the proof. $\square$
