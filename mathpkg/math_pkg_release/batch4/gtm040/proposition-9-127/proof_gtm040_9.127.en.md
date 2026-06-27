---
role: proof
locale: en
of_concept: proposition-9-127
source_book: gtm040
source_chapter: "9"
source_section: "127"
---

**Proof:** We have

$$\alpha_i P_{ij} = \alpha_i \frac{c_{ij}}{\sum_k c_{ik}} = \alpha_i \frac{c_{ij}}{\alpha_i} = c_{ij} = c_{ji} = \alpha_j P_{ji},$$

and hence

$$\sum_i \alpha_i P_{ij} = \sum_i \alpha_j P_{ji} = \alpha_j.$$

Therefore $\alpha$ is regular. Since $P_{ij} = (\alpha_j P_{ji}) / \alpha_i$, the $\alpha$-dual of $P$ is $P$.

In terms of Proposition 9-127 we can transform the equation $\mu_i = \sum_k (v_i - v_k) c_{ik}$ as follows:

$$\mu_i = v_i \alpha_i - \sum_k \alpha_i P_{ik} v_k$$

$$= v_i \alpha_i - \sum_k v_k \alpha_k P_{ki}$$

$$= [(\text{dual } v)(I - P)]_i.$$

Hence $\mu = (\text{dual } v)(I - P)$. Since $P = \hat{P}$,

$$\text{dual } \mu = (I - P)v.$$

Let $f_i = \mu_i / \alpha_i$, that is, $f$ is the dual of the vector of charges at the various terminals. Then

$$f = (I - P)v.$$

We

is transient or null, then $v$ is a potential in the Markov chain sense. And if $P$ is ergodic, then $v - (\alpha f)1$ is a potential. In any case, $f$ is the charge.

Conversely, if, in a chain which represents a circuit, $g$ is a potential vanishing outside a finite set $F$ with a charge $f$ such that $f$ has total charge 0 and $f$ has support in $E \cup \tilde{F}$, where $E \subset F$, then $g$ solves the standard voltage problem for $E$ and $F$ with the specified values $g_E$ on $E$. It is in this sense that electric circuits form a model for potential theory.

We turn to the problem of classifying all Markov chains which represent circuits. A chain $P$ is said to be $\alpha$-reversible if $\hat{P}$, the $\alpha$-dual of $P$, equals $P$.
