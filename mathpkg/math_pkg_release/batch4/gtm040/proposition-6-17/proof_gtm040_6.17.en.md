---
role: proof
locale: en
of_concept: proposition-6-17
source_book: gtm040
source_chapter: "6"
source_section: "17"
---

**Proof:** Set $N = \sum Q^n$. For the first identity we have

$$(I - P)B^E = \begin{pmatrix} I - T & -U \\ -R & I - Q \end{pmatrix} \begin{pmatrix} I & 0 \\ NR & 0 \end{pmatrix} = \begin{pmatrix} I - (T + UNR) & 0 \\ -R + (I - Q)NR & 0 \end{pmatrix}$$

$$= \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix}$$ since $(I - Q)N = I$

For the second identity, we have

$$E^E N = \begin{pmatrix} 0 & 0 \\ 0 & N \end{pmatrix}$$

and hence

$$E

Proposition 6-18: For any set $E$

$$\binom{E}{\bar{N}}(I - P) = \binom{I - P^E}{0}.$$

Proof: Apply duality to the first identity of Proposition 6-17, using Propositions 6-15 and 6-16. Then

$$\binom{E}{\hat{N}}(I - \hat{P}) = \binom{I - \hat{P}^E}{0}.$$

Since this identity holds for all reverse processes $\hat{P}$, it holds for all processes.

Using Proposition 6-16, we can obtain a simple interpretation for the ratio $\alpha_j/\alpha_i$. The case in which $P$ is recurrent is of special importance because $\alpha$ is unique up to multiplication by a constant. But first we prove a more general result.

Proposition 6-19: Let $\alpha$ be a positive finite-valued superregular measure for $P$, and let $\hat{P}$ be the $\alpha$-dual for $P$. Then for any set $E$,

$$\sum_{i \in E} \alpha_i^E \bar{N}_{ij} = \alpha_j \hat{h}_j^E.$$

Proof: By Proposition 6-16,

$$(\text{dual } \hat{B}^E)_{ij} = \begin{cases} E \bar{N}_{ij} & \text{for } i \in E \\ 0 & \text{for } i \notin E. \end{cases}$$

Therefore

$$\text{dual } \hat{h}^E = \text{dual } (\hat{B}^E 1) = \alpha(\text{dual } \hat{B}^E)$$

$$= \sum_{i \in E} \alpha_i^E \bar{N}_{ij}.$$

Corollary 6-20: Let $\alpha$ be a positive finite-valued superregular measure for $P$, and let $\hat{P}$ be the $\alpha$-dual of $P$. Then

$$^i \bar{N}_{ij} = \frac{\alpha_j}{\alpha_i} \hat{H}_{

Corollary 6-21: Let $\alpha$ be a positive finite-valued regular measure for a recurrent chain $P$. Then

$$i \bar{N}_{ij} = \alpha_j / \alpha_i.$$

Proof: Since $P$ is recurrent, so is $\hat{P}$. Thus $\hat{H}_{ji} = 1$, and we may apply Corollary 6-20.

Corollary 6-22: Let $\alpha$ be a positive finite-valued regular measure for a recurrent chain $P$. Then

$$\sum_{i \in E} \alpha_i^E \bar{N}_{ij} = \alpha_j \quad \text{for all } j.$$

Proof: Apply Proposition 6-19. Then $\hat{h}_j^E = 1$.

Definition 6-23: Let $P$ be a recurrent chain. Set

$$M_{ij} = M_i[t_j]$$

and

$$\bar{M}_{ij} = M_i[\bar{t}_j].$$

The matrix $M$ is called the mean first passage time matrix. Similarly $M_{iE}$ is the mean time from $i$ until $E$ is reached, and $\bar{M}_{iE}$ is the mean time from $i$ to return to $E$.

Proposition 6-24: If $P$ is a recurrent chain with positive regular measure $\alpha$, then

$$\sum_{i \in E} \alpha_i \bar{M}_{iE} = \alpha 1.$$

Proof: We have

$$\sum_{i \in E} \alpha_i \bar{M}_{iE} = \sum_{i \in E} \sum_j \alpha_i^E \bar{N}_{ij} = \sum_j \sum_{i \in E} \alpha_i^E \bar{N}_{ij}$$

$$= \sum_j \alpha_j = \alpha 1,$$

the next to last equality following from Corollary 6-22.

Proposition 6-25: If $P$ is a recurrent chain with positive regular measure $\alpha$, then
