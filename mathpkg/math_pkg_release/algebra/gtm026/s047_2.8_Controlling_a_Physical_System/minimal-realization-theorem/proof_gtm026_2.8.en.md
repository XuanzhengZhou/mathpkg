---
role: proof
locale: en
of_concept: minimal-realization-theorem
source_book: gtm026
source_chapter: "2"
source_section: "2.8"
---

If $\psi: (Q, \delta) \longrightarrow (Q', \delta')$ is a dynamorphism and if $\psi = e \circ m$ is an $E$-$M$ factorization of $\psi$, then there exists a unique $X$-dynamical structure making $e$ and $m$ dynamorphisms. This is clear from the diagram

$$\begin{array}{cccc}
QX & Q''X & mX & Q'X \\
\delta & \delta'' & \delta' & \delta'
\end{array}$$

if $X$ preserves $E$ and, similarly, follows at once from 2.13 and the proof of 3.4.17 if $X^@$ preserves $E$ (i.e., the structure map $\xi$).

Then $r_f = (\tau_f)^{\#}$ if $\tau_f = I\eta \circ r_f$, $\sigma_f = (\beta_f)_{\#}$ if $\beta_f = \sigma_f \circ Y\Lambda$, and $M_f = (Q_f, \delta_f, I, \tau_f, Y, \beta_f)$ is a reachable and observable realization of $f$. Now suppose that $M = (Q, \delta, I, \tau, Y, \beta)$ is another reachable realization of $f$. By diagonal fill-in there exists unique $\psi: Q \longrightarrow Q_f$ with $r \circ \psi = r_f$ and $\psi \circ \sigma_f = \sigma$. $\psi$ is a dynamorphism because $rX$ or $rX^{\#}$ is epi and $r$ and $r \circ \psi$ are dynamorphisms, and $\psi$ is a simulation. Similarly, if $M$ is an observable realization of $f$ then there exists unique $\varphi: Q_f \longrightarrow Q$ with $r_f \circ \varphi = r$ and $\varphi \circ \sigma = \sigma_f$ and such $\varphi$ is a dynamorphism because either $r_fX$ or $r_fX^{\#}$ is epi.
