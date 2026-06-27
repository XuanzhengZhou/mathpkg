---
role: proof
locale: en
of_concept: characterization-of-1-place-recursive-functions
source_book: gtm037
source_chapter: "3"
source_section: "Recursive Functions; Turing Computability"
---

Clearly the intersection indicated is included in the class of 1-place recursive functions. Now suppose that $A$ satisfies the conditions of the theorem. Note that $U_0^1 \in A$, since $U_0^1 = K_1^1(\mathrm{Exc}, \mathrm{Exc}^{(-1)})$. If $f$ is a 1-place recursive function, then $f = K_1^1(f, U_0^1)$. Hence in order to show that all 1-place recursive functions are in $A$ (which is all that remains for the proof), it suffices to prove the statement

$$(*) \text{ if } f \text{ is an } m\text{-ary general recursive function and } g_0, \ldots, g_{m-1} \in A, \text{ then } K_1^m(f; g_0, \ldots, g_{m-1}) \in A.$$

To prove $(*)$, let $B$ be the set of all $f$ such that if $f$ is $m$-ary and $g_0, \ldots, g_{m-1} \in A$ then $K_1^m(f; g_0, \ldots, g_{m-1}) \in A$. Note that for $f$ unary we have $f \in A$ iff $f \in B$. Hence $+$, $\omega$, $\mathrm{Exc}$, $U_i^n \in B$ (for $0 \leq i < n < \omega$) and $B$ is closed under inversion, applied to functions with range $\omega$. To show that $B$ is closed under composition, assume that $f$ ($m$-ary) is in $B$, that $h_0, \ldots, h_{m-1}$ (all $n$-ary) are in $B$, and that $g_0, \ldots, g_{n-1} \in A$. Then by the definition of $K_1^m$, the function $K_1^m(f \circ (h_0, \ldots, h_{m-1}); g_0, \ldots, g_{n-1})$ can be expressed in terms of the corresponding $K_1^n$ instances, showing closure under composition. The closure under primitive recursion and minimalization is established similarly using the properties of $A$.
