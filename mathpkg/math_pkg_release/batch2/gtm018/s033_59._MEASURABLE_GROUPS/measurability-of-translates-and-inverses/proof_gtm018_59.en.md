---
role: proof
locale: en
of_concept: measurability-of-translates-and-inverses
source_book: gtm018
source_chapter: "XI"
source_section: "59. Measurable Groups"
---

**Right translates $Ay$.** Let $E = A \times X$. Then $E$ is a measurable rectangle in $X \times X$, hence measurable with respect to the product $\sigma$-ring. Since $S$ is measurability preserving, $S(E)$ is measurable. The $x$-section $(S(E))_x$ is measurable for almost every $x$ with respect to $\mu$. By Theorem A, $(S(E))_x = xE_x = xA$ (since $E_x = A$ for all $x$). Hence $xA$ is measurable for almost every $x$. By left translation invariance, this implies $xA$ is measurable for all $x$. To handle $Ay$ (right translate), note that by a similar argument using $T$ and Theorem A, $A y$ is shown to be measurable via a covering argument: there exists a measurable set $B$ of positive measure such that $B \subset A^{-1}$, which implies $y^{-1}B \subset y^{-1}A^{-1}$, and since $\mu(y^{-1}B) = \mu(B) > 0$, another application yields a measurable set $C$ of positive measure with $C \subset (y^{-1}B)^{-1} \subset (y^{-1}A^{-1})^{-1} = Ay$. This settles measurability and positive measure for $Ay$.

**Measurability of $A^{-1}$.** By Theorem C and the result just proved, if $\mu(A) > 0$, then
$$\{y : \mu((Q(A \times A))^y) > 0\} = A^{-1}.$$
Since $Q$ is measure preserving (as a composition of measure preserving transformations) and product measure is used, the set on the left is measurable by Fubini-type arguments. This proves $A^{-1}$ is measurable when $\mu(A) > 0$. If $\mu(A) = 0$, find a measurable set $B$ of positive measure disjoint from $A$ (possible since $\mu$ is not identically zero and is $\sigma$-finite), then $A^{-1} = (A \cup B)^{-1} \setminus B^{-1}$ expresses $A^{-1}$ as the difference of two measurable sets, completing the proof.

**Measurability of $\hat{f}(x) = f(x^{-1})$.** This follows from the measurability of $A^{-1}$ for all measurable $A$, since $\{x : \hat{f}(x) < t\} = \{x : f(x^{-1}) < t\} = (\{x : f(x) < t\})^{-1}$.
