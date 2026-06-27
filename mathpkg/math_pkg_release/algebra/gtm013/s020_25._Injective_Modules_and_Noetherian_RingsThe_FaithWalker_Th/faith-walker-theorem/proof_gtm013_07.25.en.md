---
role: proof
locale: en
of_concept: faith-walker-theorem
source_book: gtm013
source_chapter: "7"
source_section: "25. Injective Modules and Noetherian Rings—The Faith–Walker Theorems"
---

($\Rightarrow$) As we have just observed, the condition is necessary: if $R$ is left noetherian, then by Theorem 25.6 every injective is a direct sum of indecomposable injectives. Since the set $\{E(R/I) \mid I \leq R\}$ contains an isomorphic copy of each indecomposable injective, there is a cardinal $c$ such that every indecomposable injective is $c$-generated. Thus every injective is a direct sum of $c$-generated modules.

($\Leftarrow$) Conversely, assume the existence of a cardinal number satisfying the stated condition. It is clear that any larger cardinal will then also satisfy this condition. Now to prove that $R$ is left noetherian it will suffice to show that if ${}_R E$ is injective, then $E^{(\mathbb{N})}$ is also injective (25.3). So let ${}_R E$ be injective. Now any module spanned by a set $C$ has at most $(\operatorname{card} R) \cdot (\operatorname{card} C)$ elements. Thus, our assumption implies that there is an infinite cardinal number $c$ that is greater than both $\operatorname{card} E$ and $\operatorname{card} R$ and such that every injective module is a direct sum of modules of cardinality at most $c$. Let $B$ be a set with

$$\operatorname{card} B > 2^c.$$

The direct product $E^B$ is injective (18.2), so by hypothesis

$$E^B = \bigoplus_A E_\alpha$$

where each $E_\alpha$ has cardinality at most $c$. We claim that there is a partition $\{A_0, A_1, A_2, \ldots\}$ of $A$ such that for each $n \geq 1$,

$$\bigoplus_{A_n} E_\alpha$$

contains a direct summand $Q_n$ with $Q_n \cong E$. Set

$$D = A_1 \cup \ldots \cup A_n$$

and observe that $\operatorname{card}(\bigoplus_D E_\alpha) \leq n \cdot c^2 = c$. For each $\beta \in B$, let $\iota_\beta: E \to E^B$ be the natural injection. Since $\{(\bigoplus_D E_\alpha) \cap \iota_\beta(E) \mid \beta \in B\}$ is a set of independent submodules of $\bigoplus_D E_\alpha$ and since $\bigoplus_D E_\alpha$ has at most $2^c (< \operatorname{card} B)$ subsets, there exists a $\beta \in B$ with $\bigoplus_D E_\alpha \cap \iota_\beta(E) = 0$. Thus the projection of $E^B$ on $\bigoplus_{A \setminus D} E_\alpha$ is monic on $\iota_\beta(E)$. In particular,

$$\bigoplus_{A \setminus D} E_\alpha = Q \oplus V$$

for some $Q \cong_R E$. So by (25.7) there is a subset $A_{n+1} \subseteq A \setminus D$ with $\operatorname{card} A_{n+1} \leq c$ with $Q \leq \bigoplus_{A_{n+1}} E_\alpha$. Now a standard induction argument establishes the existence of $A_1, A_2, \ldots$. Finally, set $A_0 = A \setminus \bigcup_{n=1}^{\infty} A_n$.

Now $E^{(\mathbb{N})}$ is isomorphic to a direct summand of $\bigoplus_{n=1}^{\infty} Q_n$, which in turn is a direct summand of $E^B$. Since $E^B$ is injective, $E^{(\mathbb{N})}$ is also injective, and by Theorem 25.3, $R$ is left noetherian.
