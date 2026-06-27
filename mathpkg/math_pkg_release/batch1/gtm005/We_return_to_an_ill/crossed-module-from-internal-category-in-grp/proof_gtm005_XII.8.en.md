---
role: proof
locale: en
of_concept: crossed-module-from-internal-category-in-grp
source_book: gtm005
source_chapter: "XII"
source_section: "8"
---

Given an internal category in Grp with groups $C_0$ and $C_1$ and structure homomorphisms $d_0, d_1, i, \gamma$ satisfying $d_0 i = 1 = d_1 i$ and $[\ker d_0, \ker d_1] = 1$, we construct a crossed module as follows.

Define $H = \ker d_0$ and $P = C_0$. Consider the restriction of $d_1$ to the kernel of $d_0$:

$$\partial = d_1|_{H} : H \to P.$$

This is a group homomorphism because $d_1$ is a group homomorphism and $H$ is a subgroup of $C_1$.

The sequence

$$1 \to \ker d_0 \to C_1 \xrightarrow{d_0} C_0 \to 1$$

is a short exact sequence of groups. Indeed, $d_0$ is surjective because $d_0 i = 1$ implies $i$ is a section of $d_0$, so every element $p \in C_0$ has preimage $i(p) \in C_1$. The kernel of $d_0$ is $H$ by definition.

A short exact sequence of groups determines an action of the quotient $C_0$ on the kernel $H$ in the standard way: for $p \in C_0$ and $h \in H$, choose a lift $\tilde{p} \in C_1$ with $d_0(\tilde{p}) = p$ (for instance, $\tilde{p} = i(p)$). Define the action by conjugation in $C_1$:

$$h^p = \tilde{p} h \tilde{p}^{-1}.$$

This action is well-defined because any two lifts of $p$ differ by an element of $\ker d_0 = H$, and the commutator condition $[\ker d_0, \ker d_1] = 1$ ensures independence of the choice of lift when the result lies in $\ker d_0$.

We now verify the crossed module axioms. For all $h, k \in H$ and $p, q \in P$:

1. $h^1 = h$: Taking the lift of the identity as the identity element $1 \in C_1$, conjugation by $1$ is trivial.

2. $(h^p)^q = h^{pq}$: This follows from the associativity of conjugation in a group.

3. $(hk)^p = h^p k^p$: Conjugation is a group automorphism.

4. $\partial(h^p) = p (\partial h) p^{-1}$: Since $d_1$ is a group homomorphism,
   $$\partial(h^p) = d_1(\tilde{p} h \tilde{p}^{-1}) = d_1(\tilde{p}) d_1(h) d_1(\tilde{p})^{-1} = p (\partial h) p^{-1},$$
   where we used $d_1(\tilde{p}) = d_1(i(p)) = p$ (since $d_1 i = 1$).

Thus $(H, P, \partial)$ is a crossed module. This establishes the correspondence from internal categories in Grp to crossed modules.
