---
role: exercise
locale: en
chapter: "X"
section: "7"
exercise_number: 3
---

(a) If $K: M \to C$ has a right Kan extension $R$ along itself, with
$$\varphi: \operatorname{Nat}(S, R) \cong \operatorname{Nat}(SK, K),$$
prove that $\langle R, \eta, \mu \rangle$ is a monad in $C$, where
$$\eta = \varphi^{-1}(\operatorname{Id}_K), \qquad \mu = \varphi^{-1}(\varepsilon \cdot R\varepsilon).$$
(This is called the \textbf{codensity monad} of $K$.)

(b) Show that $K$ is codense if and only if $\eta$ is an isomorphism.

(c) If $G: A \to X$ has a left adjoint $F: X \to A$ with unit $\eta: \operatorname{Id} \to GF$ and counit $\varepsilon: FG \to \operatorname{Id}$, then its codensity monad exists and is $\langle GF, \eta, G\varepsilon F \rangle$. (The monad defined by the adjunction.)
