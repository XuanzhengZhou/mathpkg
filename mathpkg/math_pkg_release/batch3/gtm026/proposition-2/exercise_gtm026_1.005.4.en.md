---
role: exercise
locale: en
chapter: "1"
section: "005"
exercise_number: 4
---

The Algebras of a Theory

The example of $(\Omega, E)$-algebras raises the question if an arbitrary algebraic theory $\mathbf{T}$ in a category $\mathcal{K}$ has algebras. Theorem 2.17 teaches us that if $\mathbf{T}$ is coextensive with its algebras, the way to describe them is as a category “of $\mathcal{K}$-objects with structure”; specifically, for each object $A$ of $\mathcal

where $\delta^@$ is defined in 1.18 and $X\rho$ is defined in 2.1.

(4.3) If $(X, \delta)$ is an $(\Omega, E)$-algebra then its structure map $\xi: XT \longrightarrow X$ is the unique $\Omega$-homomorphism such that

that is, $\xi = (\text{id}_X)^\#$ (as in 2.5).

(4.4) For fixed $\omega \in \Omega_n$, define, for each set $X$, a function $X\hat{\omega}: X^n \longrightarrow XT$ by $\langle (x_1, \ldots, x_n), X\hat{\omega} \rangle = [x_1 \cdots x_n \omega]$. Then $\hat{\omega}$ is a natural transformation, that is for every function $f: X \longrightarrow Y$ we have

where $f^n$ is defined in 1.4 and $fT$ is defined by 3.10. The $\Omega$-structure, $\delta$, on $X$ is recaptured by

for all $\omega \in \Omega_n$.

(4.6) The structure map of the $(\Omega, E)$-algebra $XT$ (2.2) is $X\mu: XTT \longrightarrow XT$.

(4.7) If $(X, \delta)$ and $(Y, \gamma)$ are $(\Omega, E)$-algebras with structure maps $\xi: XT \longrightarrow X$ and $\theta: YT \longrightarrow Y$ then a function $f: X \longrightarrow Y$ is an $\Omega$-homomorphism if and only if

$$\begin{array}{cccc}
XT & fT & YT & \theta \\
\xi & f & Y & X \\
X & f & Y
\end{array}$$

Proof. Let $(X, \delta)$ be an $\Omega$-algebra and assume that $\xi$ exists as in 4.2. For each $r: V \longrightarrow X$, $r^{\#} = r\Omega.\delta^{\#}$ (1.19), so that if $\{e_1, e_2\} \in E$ we have $e_1 r^{\#} = \langle e_1, r\Omega.X\rho.\xi \rangle = \langle e_2, r\Omega.X\rho.\xi \rangle$ (2.4 with $g = \forall \eta.r\Omega) = e_2 r^{\#}$, and $(X, \delta)$ satisfies $E$. Conversely, if $(X, \delta)$ is an $(\Omega, E)$-algebra then, using 2.5, define $\xi = (\mathrm{id}_X)^{\#}$ and observe that the diagram of 4.2 commutes because all are $\Omega$-homomorphisms and the diagram clearly commutes on the variables $x \in X$. The naturality condition on $\hat{\omega}$ is clear from the remarks on $fT$ in 3.10+. Expression 4.5 is checked by $\langle (x_1, \ldots, x_n), X\hat{\omega}.\xi \rangle = \langle [x_1 \cdots x_n\omega], \xi \rangle = \langle

$\xi: XT \longrightarrow X$ is a morphism in $\mathcal{K}$, called the structure map of $(X, \xi)$, which satisfies 4.9 and 4.10 below.

(See Exercise 11 for an alternate axiomitization.)

If $(X, \xi)$ and $(Y, \theta)$ are $\mathbf{T}$-algebras, a $\mathbf{T}$-homomorphism from $(X, \xi)$ to $(Y, \theta)$ is a $\mathcal{K}$-morphism $f: X \longrightarrow Y$ such that

Because $T$ is a functor, $\mathrm{id}_X:(X, \xi) \longrightarrow (X, \xi)$ is a $\mathbf{T}$-homomorphism, and $f.g:(X, \xi) \longrightarrow (X'', \xi'')$ is a $\mathbf{T}$-homomorphism so long as $f:(X, \xi) \longrightarrow (X'', \xi')$ and $g:(X', \xi') \longrightarrow (X'', \xi'')$ are. This gives us a category $\mathcal{K}^T$ of $\mathbf{T}$-algebras and $\mathbf{T}$-homomorphisms and a “forgetful $\mathcal{K}$-object” functor $U^T: \mathcal{K}^T \longrightarrow \mathcal{K}$.

While all definitions in 4.8 were motivated by the considerations of 4.1, it is surprising that we do not have to say more. Let us examine the heuristics somewhat further. Expressions 4.9 and 4.10 represent the idea that “$\xi = (\mathrm{id}_X)^{\#}$.” The role of 4.9 here is clear, and 4.10 is a special case of 4.11: “$\xi$ is a $\mathbf{T}$-homomorphism from $(XT, X\mu)$ to $(X, \xi)$.” It is reasonable to want $X\mu$ to be the algebra structure of $XT$ in view of 4.6, and it is consistent with our philosophy to assert so since $(XT, X\mu)$ is a $\mathbf{T}$
