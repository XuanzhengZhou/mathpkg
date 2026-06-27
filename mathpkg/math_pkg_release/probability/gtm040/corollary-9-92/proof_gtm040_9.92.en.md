---
role: proof
locale: en
of_concept: corollary-9-92
source_book: gtm040
source_chapter: "9"
source_section: "92"
---

Proof: By Proposition 6-17,

$$B^E N^{(n)} - N^{(n)} = E N P^{n+1} - E N.$$

Now

$$\text{dual } (^E N P^{n+1}) = \hat{P}^{n+1} E \hat{N} \rightarrow 1^E \hat{\nu} \text{ by Proposition 9-47, so that}$$

$$^E N P^{n+1} \rightarrow^E d\alpha.$$

Lemma 9-94: If $E$ is a finite set, then

$$B^E K = K + ^E N - ^E d\alpha$$

and

$$K \binom{^E \bar{N}}{0} = K + ^E N - 1^E \nu.$$

Proof: Each row of $B^E - I$ is a weak charge. By Theorem 9-84 and Lemma 9-93,

$$(B^E - I)K = -\lim_n (B^E - I)N^{(n)} = ^E N - ^E d\alpha.$$

The second result is dual.

Lemma 9-95: If $E$ is a finite set, then

$$\lambda^E K = k(E) \alpha + ^E \nu$$

and

$$K l^E = k(E) 1 + ^E d.$$

Proof: Multiply the equation of Lemma 9-94 on the right by $l^E$ to obtain

$$B^E (K l^E) = K l^E + ^E N l^E - ^E d(\alpha l^E)$$

$$= K l^E - ^E d.$$

But $(K l^E)_E = K_E l_E^E$, which by Proposition 9-87 equals $k(E) 1$. Hence

$$K l^E = k(E) 1 + ^E d.$$

The other result is dual.

Lemma 9-96: If $E, F$, and $L$ are finite sets with $E$ and $F$ both contained in $L$, then

$$[k(E) -

PROOF: Multiplying the equation of Lemma 9-95 through by $\lambda^L$, we obtain

$$\lambda^L Kl^E = k(E) + \lambda^L E d$$

and similarly

$$\lambda^L Kl^F = k(F) + \lambda^L F d.$$

Subtracting, we see that it is sufficient to prove that $\lambda^L Kl^E = \lambda^L Kl^F$. But

$$\lambda^L Kl^E = (\lambda^L_K L)_L l^E = k(L) \alpha_L l^E = k(L)$$

since the support of $l^E$ is in $L$. Similarly, $\lambda^L Kl^F = k(L)$. The other equality is dual.

Lemma 9-97: For any sets $A_1, A_2, \ldots, A_r$ which have at least one point in common,

$$A_1 \cap A_2 \cap \cdots \cap A_r N_{ij} \geq \sum_s A_s N_{ij} - \sum_{s \neq t} A_s \cup A_t N_{ij}$$

$$+ \sum_{s \neq t \neq u} A_s \cup A_t \cup A_u N_{ij} - \cdots + (-1)^{r+1} A_1 \cap A_2 \cap \cdots \cap A_r N_{ij}.$$

PROOF: The left side is the mean number of times in state $j$, starting in $i$, before the intersection of sets is reached. We shall show that the right side is the mean number of times in $j$ before all of the sets have been reached. The former is clearly at least as large as the latter. Let $n_j(\omega)$ be the number of times on $\omega$ that the process is in $j$ before all sets are entered. On the path $\omega$ let $S_k$ be the set of times at which the process is in $j$ before $A_k$ is entered. Then $n_j(\omega)$ is the cardinal number of $S_1 \cup S_2 \cup \cdots \cup S_r$ and equals

$$\sum_s n(S_s) - \sum_{s \

Proof: We first prove monotonicity. Let $A \subset B$; then

$$A N \geq B N.$$

Thus

$$P^n A N \geq P^n B N.$$

As $n \to \infty$,

$$A \nu \geq B \nu.$$

Therefore

$$(A \nu - B \nu) l^L \geq 0.$$

If $L$ contains $A$ and $B$, then by Lemma 9-96, $k(B) - k(A) \geq 0$ or

$$k(B) \geq k(A).$$

Therefore $k$ is monotone. The other inequality of the proposition follows in exactly the same manner starting from the result of Lemma 9-97.

In the next section we shall prove potential principles for sets of positive capacity. It is therefore particularly annoying when all sets in a chain have capacity zero, and we treat this case now.

Definition 9-99: A normal chain is degenerate if, for every choice of the reference state 0, $k(E) = 0$ for all finite sets $E$.

Lemma 9-100: If, for a single reference point 0, $k(E) = 0$ for all $E \in \mathcal{L}_0$ and for all one-point sets, then the chain is degenerate.

Proof: If $0'$ is any other reference point, then

$$k(E) = k'(E) + k(\{0'\}) = k'(E).$$

Hence it suffices to show that $k(E) = 0$. If $0 \in E$, $k(E) = 0$ by hypothesis. If $0 \notin E$, let $0'$ be any point of $E$, and $0 = k'(\{0'\}) \leq k'(E) = k(E) \leq k(E \cup \{0\}) = 0$. Both inequalities follow by the monotonicity proved in Proposition 9-98.

Lemma 9-101: A normal chain is degenerate if and only if for every pair of states $i$ and $j$ either $i \lambda_j = 0$ and $

Conversely, if $0\lambda_j = 0$ or $0\hat{\lambda}_j = 0$ for all states $j$, then $k(E) = 0$ for all $E \in \mathcal{L}_0$ (by Proposition 9-89 since $\lambda_j^E \leq 0\lambda_j$). And

$$k(\{j\}) = \frac{1}{\alpha_j} (G_{0j} - C_{0j}) = \frac{0N_{jj}}{\alpha_0} (0\lambda_j - j\hat{\lambda}_0).$$

But $0\lambda_j$ and $j\hat{\lambda}_0$ are either both 0 or both 1. Hence $k(\{j\}) = 0$. Thus the converse follows from Lemma 9-100.

The basic example and its reverse are degenerate when null. It can be shown that degenerate chains are all of a type similar to the basic example. (See the problems.)
