---
role: proof
locale: en
of_concept: dedekind-eta-functional-equation-lemma-3
source_book: gtm041
source_chapter: "3"
source_section: "Supplement"
---

For $A T^m$: Replace $\tau$ by $T^m \tau = \tau + m$ in the functional equation (5). Then
$$
\eta(A T^m \tau) = \varepsilon(A) \{-i(c T^m \tau + d)\}^{1/2} \eta(T^m \tau)
= \varepsilon(A) \{-i(c\tau + mc + d)\}^{1/2} e^{\pi i m/12} \eta(\tau).
$$
Using Lemma 1 ($\varepsilon(A T^m) = e^{\pi i m/12} \varepsilon(A)$), we obtain
$$
\eta(A T^m \tau) = \varepsilon(A T^m) \{-i((c)\tau + (cm+d))\}^{1/2} \eta(\tau),
$$
which is precisely the functional equation for $A T^m$.

For $A S$: Replace $\tau$ by $S \tau = -1/\tau$ in (5) and use Theorem 3.1 ($\eta(S\tau) = \{-i\tau\}^{1/2} \eta(\tau)$). This gives
$$
\eta(A S \tau) = \varepsilon(A) \{-i(c S \tau + d)\}^{1/2} \{-i\tau\}^{1/2} \eta(\tau).
$$
Analyzing the product of square roots for the cases $d > 0$ and $d < 0$ (as in Lemma 2), and applying the corresponding value of $\varepsilon(AS)$, yields the functional equation for $A S$.
