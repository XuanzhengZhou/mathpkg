---
role: exercise
locale: en
chapter: "II"
section: "5"
exercise_number: 5.16
---

Tensor Operations on Sheaves. Let $A$ be a ring, and let $M$ be an $A$-module. Let $T^n(M)$ be the tensor product $M \otimes \dots \otimes M$ of $M$ with itself $n$ times, for $n \geqslant 1$. For $n = 0$ we set $T^0(M) = A$. Let $S^n(M)$ be the symmetric power, and $\bigwedge^n M$ the exterior power.

(a) Show that the tensor operations are functorial and commute with localization: $T^n(M_f) \cong T^n(M)_f$, etc.

(b) Show that there are natural isomorphisms $T^n(M \oplus N) \cong \bigoplus_{p+q=n} T^p(M) \otimes T^q(N)$.

(c) Let $0 \to M' \to M \to M'' \to 0$ be an exact sequence of $A$-modules. Show that there is a natural filtration of $S^n(M)$ whose associated graded module is $\bigoplus_{p+q=n} S^p(M') \otimes S^q(M'')$.

(d) Same statement as (c), with exterior powers instead of symmetric powers. In particular, if $M', M, M''$ have ranks $n', n, n''$ respectively, there is an isomorphism $\bigwedge^n M \cong \bigwedge^{n'} M' \otimes \bigwedge^{n''} M''$.

(e) Let $f: X \rightarrow Y$ be a morphism of ringed spaces, and let $\mathcal{F}$ be an $\mathcal{O}_Y$-module. Then $f^*$ commutes with all the tensor operations on $\mathcal{F}$, i.e., $f^*(S^n(\mathcal{F})) = S^n(f^*\mathcal{F})$ etc.

