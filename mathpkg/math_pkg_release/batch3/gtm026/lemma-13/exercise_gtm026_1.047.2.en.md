---
role: exercise
locale: en
chapter: "1"
section: "047"
exercise_number: 2
---

([Barr '70-A, 5.11, 5.12]). Let $X: \mathcal{K} \longrightarrow \mathcal{K}$ be an arbitrary endofunctor.

(a) Prove that if $(Q, \delta)$ is an initial object in $\text{Dyn}(X)$ then $\delta: QX \longrightarrow Q$ is an

Given an ordinal-indexed ascending chain in M, the injections to the colimit are in M and the colimit-induced map owing to an upper bound whose components are in M is again in M.

$K$ is M well-powered.

For $Y: K \longrightarrow K$ any functor, any $f: I \longrightarrow IY$ may be transfinitely iterated through the ordinals:

$$A \xrightarrow{f_0 = f} AY \xrightarrow{f_1 = f_0 Y} AY^2 \longrightarrow \cdots AY^\omega = \text{colim} AY^n$$

$$AY^\omega \xrightarrow{f_\omega} AY^\omega + 1$$ is colimit-induced $\cdots$

Notice that if $Y$ preserves M then each $f$ is in M.

(a) Let $X: K \longrightarrow K$ preserve M and fix $I$ in $K$. Prove that the following three conditions are equivalent:

(i) The free dynamics $(IX^\alpha, I\mu_0)$ over $I$ exists.

(ii) If $Y: K \longrightarrow K$ is defined by $AY = I + AX$ and if $f: I \longrightarrow IY$ is the first injection then the iteration of $f$ (as above) stops, i.e., $f_\alpha$ is an isomorphism for some $\alpha$.

(iii) There exists $A$ in $K$ with $A \cong I + AX$.

[Hint: for (ii) implies (i) set $IX = IY^\alpha, I\mu_0 = in_2.f_\alpha^{-1}$; for (i) implies (iii) use exercise 2 (b); for (iii) implies (i) construct canonical morphisms $IY^\alpha \longrightarrow A$ in M and use well-poweredness.]

(b) As a corollary to (a), show that $X: \text{Set} \longrightarrow \text{Set}$ is an input process if and only if $\text{card}(\alpha X) \leqslant \alpha$ for arbitrarily large cardinals $\alpha$.

(c) Show that the power-set functor is

here, $g_0$ is arbitrary, $h_n$ is defined by “$\eta.h_n = f$, $\delta.h_n = g_{n-1}.\delta'$” and $g_{n+1} = h_nX$; define $E_n = \text{eq}(h_m:m \geqslant n)$; then $E = \text{colim} E_n$ is a dynamics through which $f$ factors because $X$ preserves the colimit; $E = R$ because $Q$ generates $R$.

It is standard to say that the $\Omega$-algebra $(R, \delta)$ is a Peano algebra if (i) whenever $\omega \in \Omega_n$, $\omega' \in \Omega_{n'}$, $f \in Q^n$, $f' \in Q^{n'}$ are such that $f\delta_\omega = f'\delta_\omega'$, then $n = n'$, $\omega = \omega'$, and $f = f'$ and (ii) the set $Q$ of elements not of form $f\delta_\omega$ generates $(R, \delta)$. It is clear that this concept coincides with the Peano algebras relative to $X_\Omega$ in the sense of exercise 5. It has been noted by [Lowig '52], [Slomiński '55], [Diener '66], and [Felscher '72] that Peano $\Omega$-algebras are free; this can be proved for finitary $\Omega$ as in exercise 5. It is interesting to ask which input processes not of the form $X_\Omega$ are such that “Peano implies free” is true, and to speculate upon the possibility that such new Peano algebras will play a role in the syntax of universal algebra.
