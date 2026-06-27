---
role: proof
locale: en
of_concept: proposition-5-7
source_book: gtm040
source_chapter: "5"
source_section: "7"
---

**Proof:** Letting $p$ be the statement $s_E$ and taking the random time to be identically one, we see that $p'$ in Theorem 4-10 is also $s_E$ and that

$$\Pr_i[s_E] = \sum_{k} P_{ik} \Pr_k[s_E]$$

or

$$s^E = Ps^E.$$

For any Markov chain $P$ we define a **hitting vector** $h^E$ and an **escape vector** $e^E$ by

$$h^E = \Pr_i[\text{process eventually reaches } E]$$

and

$$e^E = \Pr_i[\text{process goes on first step from } E \text{ to } \tilde{E} \text{ and then never returns to } E].$$

We notice that if $i \in E$, then $h^E = 1$, and that if $j \in \tilde{E}$ then $e^E = 0$.

The **absorption matrix** $B^E$ for the set $E$ is defined to be a square matrix with index set the set of all states and with entries defined by

$$B_{ij}^E = \Pr_i[\

We see that the $B^E$-matrix is computed by finding the entries of the $B$-matrix for the process with states of $E$ made absorbing. Specifically, if $E$ is the set of all absorbing states, then

$$B^E = \begin{pmatrix} E & \tilde{E} \\ E & \tilde{E} \end{pmatrix} \left( \begin{array}{cc} I & 0 \\ B & 0 \end{array} \right).$$

The matrices $s^E, h^E, e^E$, and $B^E$ are interrelated as in the following proposition, whose proof is left to the reader.
