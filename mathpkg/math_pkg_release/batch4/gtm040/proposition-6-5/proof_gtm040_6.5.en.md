---
role: proof
locale: en
of_concept: proposition-6-5
source_book: gtm040
source_chapter: "6"
source_section: "5"
---

**Proof:** We have $PA = A$. Thus every column of $A$ is regular and must be constant by Proposition 6-3. Hence $A = 1\alpha$. Since $AP = A$, every row of $A$ is regular and $\alpha$ must be regular. It therefore remains to be shown that $\alpha_1 = 1$. Now $A^2 = A$ so that $(1\alpha)(1\alpha) = (1\alpha)$. By associativity $1(\alpha(1\alpha)) = 1\alpha$ so that $\alpha(1\alpha) = \alpha$. But $\alpha(1\alpha) = (\alpha_1)\alpha$ so that $(\alpha_1)\alpha = \alpha$. If $\alpha_j \neq 0$, then from

Lemma 6-6: For an arbitrary Markov chain $P$, $P^E$ is a Markov chain and

$$P^E = T + UNR,$$

where $N = \sum_{k=0}^{\infty} Q^k$.

Remark: The lemma holds even if $N$ has infinite entries, provided we agree as usual that $0 \cdot \infty = 0$.

Proof: Let $y_n$ be the $n$th outcome in the $P^E$-process. If

$$\Pr_{\pi}[y_0 = c_0 \wedge \cdots \wedge y_{n-1} = c_{n-1}] > 0,$$

let $t$ be the random time of outcome $n-1$ and apply Theorem 4-9. Then

$$\Pr_{\pi}[y_n = c_n \mid y_0 = c_0 \wedge \cdots \wedge y_{n-1} = c_{n-1}]$$

$$= \Pr_{\pi}[y_n = c_n \mid y_0 = c_0 \wedge \cdots \wedge y_{n-1} = c_{n-1} \wedge x_t = c_{n-1}]$$

$$= \Pr_{c_{n-1}}[y_1 = c_n],$$

and it follows that $P^E$ is a Markov chain. Now let $i$ and $j$ be in $E$. Applying Theorem 4-10 with the random time identically one and with the statement that $E$ is hit after time 0 first at state $j$, we have

$$P^E_{ij} = \sum_k P_{ik} B^E_{kj}$$

$$= \sum_{k \in E} P_{ik} B^E_{kj} + \sum_{k \notin E} P_{ik} B^E_{kj}$$

$$= P_{ij} + \sum_{k \notin E} P_{ik} B^E_{kj}.$$

The result then follows from Proposition 5-6.

Lemma 6-7: For an arbitrary Markov chain $P$, if $E$ is a subset of states and $\beta

where $\gamma = \beta_E(I - Q)$, $N = \sum Q^n$, and $\rho$ is non-negative and $Q$-regular. Hence

$$\beta_E \geq \gamma N \geq (\beta_E U)N.$$

Thus $\beta_E P^E = \beta_E T + \beta_E UNR \leq \beta_E T + \beta_E R \leq \beta_E.$
