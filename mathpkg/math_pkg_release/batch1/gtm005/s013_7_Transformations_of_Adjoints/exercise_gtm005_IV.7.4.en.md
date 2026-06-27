---
role: exercise
locale: en
chapter: "IV"
section: "7"
exercise_number: 4
---

(Kelly.) An adjoint square is an array of categories, functors, adjunctions, and natural transformations

$$\begin{array}{ccc}
X & \xrightarrow{\langle F, G, \varphi \rangle} A, & \sigma : F'H \xrightarrow{\cdot} KF, \\
H \downarrow & \xrightarrow{\langle F', G', \varphi' \rangle} A', & \tau : HG \xrightarrow{\cdot} G'K,
\end{array}$$

such that the following diagram of hom-sets always commutes:

$$\begin{array}{ccc}
A(Fx, a) & \xrightarrow{K} A'(KFx, Ka) & \xrightarrow{(\sigma_x)^*} A'(F'Hx, Ka) \\
\varphi \downarrow & & \downarrow \varphi' \\
X(x, Ga) & \xrightarrow{H} X'(Hx, HGa) & \xrightarrow{(\tau_a)_*} X'(Hx, G'Ka).
\end{array}$$

Express this last condition variously in terms of unit and counit of the adjunctions and prove that each of $\sigma, \tau$ determines the other. (The case $H = K = \text{identity functor}$ is that treated in the text above.)
