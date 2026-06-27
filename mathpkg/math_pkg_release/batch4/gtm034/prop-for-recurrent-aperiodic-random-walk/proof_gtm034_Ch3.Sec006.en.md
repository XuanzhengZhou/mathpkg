---
role: proof
locale: en
of_concept: prop-for-recurrent-aperiodic-random-walk
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: According to D1

$$\sum_{y \in A} \Pi_A(x,y) = P_z[T < \infty] \leq 1,$$

where $T = \min [k \mid 1 \leq k \leq \infty, x_k \in A]$. The second part follows from the observation that $\Pi_A^*(x,y) = \Pi_A(y,x)$, so that

$$\sum_{z \in A} \Pi_A(x,y) = \sum_{z \in A} \Pi_A^*(y,x) \leq 1$$

by the first part of P4. For recurrent aperiodic random walk P4 will be strengthened considerably in the beginning of the next section (P11.2).

Remark: The terminology and notation introduced in this section will be used throughout the remainder of the book. The rest of this chapter (sections 11 through 16) will be devoted to two-dimensional recurrent random walk. For this case a rather complete theory of stopping times $T = T_A$ for finite sets $A \subset R$ may be developed using quite elementary methods. These methods provide a good start, but turn out to be insufficient in other cases—namely for transient random walk as well as in the one-dimensional recurrent case. Therefore the theory in this chapter will have to perform the service of motivating and illustrating many later developments.

11. THE HITTING PROBABILITIES OF A FINITE SET

Through the remainder of this chapter we assume that we are dealing with aperiodic recurrent random walk in two dimensions. Further, all probabilities of interest, i.e., all the functions in D10.1 will be those associated with a nonempty finite subset $B$ of $R$. The methods and results will be independent of the cardinality $|B|$ except in a few places where the case $|B| = 1$ requires special consideration.

The primary purpose of this section is to show how one can calculate $H_B(x,y)$ which we shall call the hitting probability measure of the set $B$. To begin with, we base the calculation on part (a) of P10.1 from which one obtains

2 This will be tacitly assumed. Only the statements of the principal theorems will again explicitly contain these hypotheses.
