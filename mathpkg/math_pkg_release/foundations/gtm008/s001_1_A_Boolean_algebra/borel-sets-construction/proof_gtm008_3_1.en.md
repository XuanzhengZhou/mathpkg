---
role: proof
locale: en
of_concept: borel-sets-construction
source_book: gtm008
source_chapter: "3"
source_section: "1"
---

*Proof.* Clearly each element in $A_0$ is a Borel set, since $A_0$ consists of open sets and their complements. If $A_\alpha$ is a collection of Borel sets then so is $A_{\alpha+1}$, because countable unions and countable intersections of Borel sets are Borel. If for $\beta < \alpha$, each $A_\beta$ is a collection of Borel sets, then $\bigcup_{\beta < \alpha} A_\beta$ is also a collection of Borel sets. By transfinite induction, $A = \bigcup_{\alpha \in \aleph_1} A_\alpha$ is a collection of Borel sets.

To prove that $A$ contains all Borel sets, it suffices to show that $A$ is a Boolean $\sigma$-algebra (since the Borel $\sigma$-algebra is the smallest $\sigma$-algebra containing the open sets).

Since $A_0 \subseteq A$ and $\varnothing, X \in T \subseteq A_0$, we have $0, 1 \in A$. Because union and intersection are associative, commutative, and distributive, we need only verify that $A$ has the closure and $\sigma$-closure properties.

First note that $\alpha < \beta$ implies $A_\alpha \subseteq A_\beta$. If $b_0, b_1, \ldots$ is an $\omega$-sequence of elements of $A$, then there exists an $\omega$-sequence of ordinals $\alpha_0, \alpha_1, \ldots$, each less than $\aleph_1$, such that $b_n \in A_{\alpha_n}$ for each $n < \omega$. Since $\aleph_1$ has uncountable cofinality ($\operatorname{cf}(\aleph_1) = \aleph_1 > \omega$), the countable sequence $\langle \alpha_n : n < \omega \rangle$ is bounded below $\aleph_1$. Let $\alpha = \sup_{n < \omega} \alpha_n$; then $\alpha < \aleph_1$ and $b_n \in A_{\alpha_n} \subseteq A_\alpha$ for all $n$. By definition of $A_{\alpha+1}$, we obtain

$$\bigcup_{n < \omega} b_n \in A_{\alpha+1} \subseteq A, \qquad \bigcap_{n < \omega} b_n \in A_{\alpha+1} \subseteq A.$$

Thus $A$ is closed under countable unions and intersections.

For complements: if $b \in A$, there exists $\alpha < \aleph_1$ with $b \in A_\alpha$. One proves by transfinite induction on $\alpha$ that $X - b \in A$. For $\alpha = 0$: if $b \in A_0$, then either $b \in T$ (so $X - b \in A_0 \subseteq A$) or $b = X - a$ for some $a \in T$ (so $X - b = a \in T \subseteq A_0 \subseteq A$). At successor stages, De Morgan's laws give $(X - \bigcup_n b_n) = \bigcap_n (X - b_n)$ and $(X - \bigcap_n b_n) = \bigcup_n (X - b_n)$, reducing complementation to the previous stage. At limit stages, the induction hypothesis applies uniformly.

Hence $A$ is a Boolean $\sigma$-algebra containing all open sets and therefore containing all Borel sets. Combined with the first part, $A$ equals exactly the set of all Borel sets in $X$. $\square$
