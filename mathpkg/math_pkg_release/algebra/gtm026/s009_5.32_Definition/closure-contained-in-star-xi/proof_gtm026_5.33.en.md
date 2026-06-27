---
role: proof
locale: en
of_concept: closure-contained-in-star-xi
source_book: gtm026
source_chapter: "5"
source_section: "5.33"
---

This is where we really use the algebra axioms. First of all, if $i: B \longrightarrow X$ is the inclusion map then clearly $B^*$ is just the image of $i\beta: B\beta \longrightarrow X\beta$, so that $B^*\xi$ is just $\langle B \rangle$ as in 4.31. In particular, $B \subset B^*\xi$ and $(B^*\xi)^*\xi = B^*\xi$.

To show $B^*\xi$ is $\mathcal{T}$-closed, we must show, given $\mathfrak{U} \in X\beta$ with $\mathfrak{U}\xi \in B^*\xi$, that there exists $U \in \mathfrak{U}$ such that $U \subset B^*\xi$. Since $\mathfrak{U}\xi \in B^*\xi = \langle B \rangle$, there exists $V \in B\beta$ with $V\xi = \mathfrak{U}\xi$. By the second algebra axiom (relating $\beta$ and $\xi$), the filters $\mathfrak{U}$ and $V$ are compatible, so they have a common refinement. This yields the required $U \in \mathfrak{U}$.
