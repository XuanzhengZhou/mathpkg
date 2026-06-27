---
role: proof
locale: en
of_concept: strong-markov-property
source_book: gtm040
source_chapter: "4"
source_section: "4"
---

We prove the theorem for any statement $r$ measurable with respect to $\mathcal{T}_t \cap \mathcal{F}$; the extension to general $r$ relative to $\mathcal{T}_t$ follows from the uniqueness of extension of a probability measure (Theorem 1-19), exactly as in the proof of Lemma 4-7.

Decompose along the value of the random time $t$:

$$\Pr_{\pi}[r \mid q \land x_t = i] = \sum_{n} \Pr_{\pi}[r \mid q \land x_n = i \land t = n] \cdot \Pr_{\pi}[t = n \mid q \land x_t = i].$$

For each fixed $n$, the statement $q \land t = n$ is relative to $\mathcal{F}_n$ (by definition of $\mathcal{F}_t$). Let $\hat{r}$ be the statement obtained from $r$ by replacing each occurrence of $t$ with $n$ in the constraints $x_t = c_t \land \cdots \land x_{t+N} = c_{t+N}$. That is, $\hat{r}$ is the statement

$$x_n = c_t \land \cdots \land x_{n+N} = c_{t+N},$$

and $r$ is the disjunction of such statements over all finite $N$. Then $\hat{r}$ is relative to $\mathcal{T}_n \cap \mathcal{F}$ (since $r$ is in $\mathcal{T}_t \cap \mathcal{F}$, each component $r \land t = n$ corresponds to a statement in $\mathcal{T}_n \cap \mathcal{F}$).

Moreover, $\omega$ is in the truth set of $\hat{r}$ if and only if $\omega_n$ is in the truth set of $r'$. Hence

$$\Pr_{\pi}[r \mid q \land x_n = i \land t = n] = \Pr_{\pi}[r \land t = n \mid q \land x_n = i \land t = n] = \Pr_{\pi}[\hat{r} \land t = n \mid q \land x_n = i \land t = n].$$

Now note that $t = n$ is part of the condition on both sides, and $(q \land t = n)$ is relative to $\mathcal{F}_n$. Therefore

$$\Pr_{\pi}[\hat{r} \land t = n \mid (q \land t = n) \land x_n = i] = \Pr_{\pi}[\hat{r} \mid (q \land t = n) \land x_n = i].$$

Since $q \land t = n$ is relative to $\mathcal{F}_n$ and $\hat{r}$ is relative to $\mathcal{T}_n$, Lemma 4-7 applies, giving

$$\Pr_{\pi}[\hat{r} \mid (q \land t = n) \land x_n = i] = \Pr_{\pi}[\hat{r} \mid x_n = i] = \Pr_i[r'].$$

Summing over $n$, the right-hand side $\Pr_i[r']$ factors out (it does not depend on $n$), and since $\sum_n \Pr_{\pi}[t = n \mid q \land x_t = i] = 1$, we obtain

$$\Pr_{\pi}[r \mid q \land x_t = i] = \Pr_i[r'].$$

The equality $\Pr_{\pi}[r \mid x_t = i] = \Pr_i[r']$ follows by taking $q$ to be the identically true statement.

To obtain the alternative formulation, observe that by the definition of conditional probability:

$$\Pr_{\pi}[q \land r \mid x_t = i] = \Pr_{\pi}[r \mid q \land x_t = i] \cdot \Pr_{\pi}[q \mid x_t = i] = \Pr_{\pi}[r \mid x_t = i] \cdot \Pr_{\pi}[q \mid x_t = i],$$

which is precisely the statement that past and future are conditionally independent given the present.
