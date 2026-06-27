---
role: proof
locale: en
of_concept: unique-factorization-induction
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

Applying the result that in a principal ideal domain every irreducible element is prime, to the equality
$$p_1 \cdots p_r = q_1 \cdots q_s,$$
we see that $p_1$ divides the product $q_1 \cdots q_s$. Since $p_1$ is irreducible (hence prime), $p_1$ must divide some $q_j$. Without loss of generality, reorder so that $p_1$ divides $q_1$.

Since $p_1$ and $q_1$ are both irreducible elements in a principal ideal domain, the divisibility $p_1 \mid q_1$ implies that $p_1$ and $q_1$ are associates: there exists an invertible element $e_1$ such that $p_1 = e_1 q_1$.

Cancelling $q_1$ from both sides of the original equality (which is possible since $R$ is an integral domain), we obtain
$$e_1 p_2 \cdots p_r = q_2 \cdots q_s.$$

Now we may apply the induction hypothesis on $\min(r, s)$, since the number of factors has been reduced by one on each side. The result follows.
