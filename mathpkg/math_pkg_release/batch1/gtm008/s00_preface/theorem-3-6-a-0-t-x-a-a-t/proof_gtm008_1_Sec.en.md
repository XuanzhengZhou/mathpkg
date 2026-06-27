---
role: proof
locale: en
of_concept: theorem-3-6-a-0-t-x-a-a-t
source_book: gtm008
source_chapter: "1"
source_section: "1 A Boolean algebra"
---
Clearly each element in $A_0$ is a Borel set. If $A_\alpha$ is a collection of Borel sets then so is $A_{\alpha+1}$. If for $\beta < \alpha$, $A_\beta$ is a collection of Borel sets then

$$\bigcup_{\beta < \alpha} A_\beta$$

is a collection of Borel sets. Therefore $A$ is a collection of Borel sets. To prove that $A$ contains all Borel sets it is sufficient to prove that $A$ is a Boolean $\sigma$-algebra.

Since $A_0 \subseteq A$ and $0, 1 \in A_0$ we have $0, 1 \in A$. Since union and intersection are associative, commutative, and distributive we need only prove that $A$ has the closure and $\sigma$-closure properties.

We first note that $\alpha < \beta$ implies $A_\alpha \subseteq A_\beta$. If

$$b_0, b_1, \ldots$$

is an $\omega$-sequence of elements of $A$ then there exists an $\omega$-sequence of ordinals

$$\alpha_0, \alpha_1, \ldots$$

each less than $\aleph_1$ and such that $b_0 \in A_{\alpha_0}, b_1 \in A_{\alpha_
