---
role: proof
locale: en
of_concept: resolution-of-birational-transformations
source_book: gtm052
source_chapter: "V"
source_section: "5"
---

**Proof.** Using (5.4), it will be sufficient to show that there is a surface $X''$, and birational morphisms $f: X'' \to X$ and $g: X'' \to X'$ such that $T = g \circ f^{-1}$. To construct $X''$, we proceed as follows.

Let $H'$ be a very ample divisor on $X'$, and let $C'$ be an irreducible non-singular curve in the linear system $|2H'|$, which does not pass through any of the fundamental points of $T^{-1}$. In other words, $C'$ is entirely contained in the largest open set $U' \subseteq X'$ on which $T^{-1}$ is represented by a morphism $\varphi: U' \to X$. Let $C = \varphi(C')$ be the image of $C'$ in $X$. We define an integer $m$ by $m = p_a(C) - p_a(C')$. Since we have a finite birational morphism of $C'$ to $C$, we see that $m \geqslant 0$, and $m = 0$ if and only if $C'$ is isomorphic to $C$ (IV, Ex. 1.8). Note also that if we replace $C'$ by a linearly equivalent curve $C'_1$, also missing the fundamental points of $T^{-1}$, then $C_1 = \varphi(C'_1)$ is linearly equivalent to $C$. In fact, if $C' - C'_1 = (f)$ for some rational function $f$ on $X'$, then $C - C_1 = (f)$ on $X$. Since the arithmetic genus of a curve depends only on its linear equivalence class (Ex. 1.3), we see that the integer $m$ depends only on $T$ and $H'$, and not on the particular curve $C' \in |2H'|$ chosen.

Now fix $C'$ temporarily. If $m > 0$, then $C$ must be singular. Let $P$ be a singular point of $C$, let $\pi: \tilde{X} \to X$ be the monoidal transformation with center $P$, [and one continues by replacing $X$ with $\tilde{X}$ and showing that the invariant $m$ strictly decreases after finitely many such monoidal transformations, eventually reaching $m = 0$, which yields the desired $X''$.]
