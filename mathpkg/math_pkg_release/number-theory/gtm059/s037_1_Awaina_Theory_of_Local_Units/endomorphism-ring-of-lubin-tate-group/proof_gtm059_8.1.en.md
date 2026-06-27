---
role: proof
locale: en
of_concept: endomorphism-ring-of-lubin-tate-group
source_book: gtm059
source_chapter: "8"
source_section: "1. Lubin-Tate Groups"
---

\textbf{Existence of $[a]_f$:} Apply the Construction Lemma with $f = g$ and the linear form $L(X) = aX$. We obtain a unique power series $[a]_f(X)$ satisfying $[a]_f(X) \equiv aX \pmod{\deg 2}$ and $f([a]_f(X)) = [a]_f(f(X))$.

\textbf{Additivity:} Consider $H(X) = F_f([a]_f(X), [b]_f(X))$. Then
$$
H(X) \equiv aX + bX = (a+b)X \pmod{\deg 2},
$$
and
$$
f(H(X)) = f(F_f([a]_f(X), [b]_f(X))) = F_f(f([a]_f(X)), f([b]_f(X))) = F_f([a]_f(f(X)), [b]_f(f(X))) = H(f(X)).
$$
Thus $H$ satisfies the characterizing properties of $[a+b]_f$, so by uniqueness $H = [a+b]_f$, giving $[a+b]_f(X) = F_f([a]_f(X), [b]_f(X))$.

\textbf{Multiplicativity:} Consider $K(X) = [a]_f([b]_f(X))$. Then
$$
K(X) \equiv a(bX) = (ab)X \pmod{\deg 2},
$$
and
$$
f(K(X)) = f([a]_f([b]_f(X))) = [a]_f(f([b]_f(X))) = [a]_f([b]_f(f(X))) = K(f(X)).
$$
Thus $K$ satisfies the characterizing properties of $[ab]_f$, so $[ab]_f(X) = [a]_f([b]_f(X))$.

\textbf{Injectivity:} If $[a]_f = [b]_f$, then comparing linear coefficients gives $aX = bX$, so $a = b$. The ring homomorphism properties follow from the identities established above.
