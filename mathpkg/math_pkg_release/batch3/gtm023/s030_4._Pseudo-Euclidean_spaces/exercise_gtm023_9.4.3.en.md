---
role: exercise
locale: en
chapter: "9"
section: "4"
exercise_number: 3
---

Consider a pseudo-Euclidean space $E$ of index $n-1$ and a linear transformation $\psi$ of $E$ which is skew ($\tilde{\psi} = -\psi$). Consider the family of linear automorphisms $\varphi(t)$ which is defined by the differential equation
$$\dot{\varphi}(t) = \psi \circ \varphi(t)$$
and the initial condition
$$\varphi(0) = \iota.$$

\begin{enumerate}
  \item[(a)] Prove that $\varphi(t)$ is a family of proper rotations carrying fore-cone and past-cone into themselves.
  \item[(b)] Define the functions $C(t)$ and $S(t)$ by
    $$C(t) = \frac{1}{2} \operatorname{tr} \varphi(t) \quad \text{and} \quad S(t) = \frac{1}{2} \operatorname{tr} \big( \psi \circ \varphi(t) \big).$$
    Prove the functional-equations
    $$C(t_1 + t_2) = C(t_1)C(t_2) + S(t_1)S(t_2)$$
    and
    $$S(t_1 + t_2) = S(t_1)C(t_2) + S(t_2)C(t_1).$$
  \item[(c)] Prove that
    $$\varphi(t)a = e^{-t}a \quad \text{and} \quad \varphi(t)b = e^{-t}b.$$
\end{enumerate}
