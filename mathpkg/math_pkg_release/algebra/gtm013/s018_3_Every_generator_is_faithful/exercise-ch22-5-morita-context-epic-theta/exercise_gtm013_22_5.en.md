---
role: exercise
locale: en
chapter: "22"
section: "Exercises"
exercise_number: 5
---
In a Morita context $(R, S, {}_R P_S, {}_S Q_R, \theta, \phi)$, define
$$\hat{\phi}(x): f \mapsto \phi(f \otimes x) \quad \text{and} \quad \bar{\phi}(f): x \mapsto \phi(f \otimes x).$$
Prove that:
\begin{enumerate}
    \item[(1)] $\hat{\phi}$ is an $(S, R)$-homomorphism ${}_S P_R \to \operatorname{Hom}_R({}_R Q_S, {}_R R_R)$ and $\bar{\phi}$ is an $(R, S)$-homomorphism ${}_R Q_S \to \operatorname{Hom}_R({}_S P_R, {}_R R_R)$.
    \item[(2)] If $\theta$ is epic, then
    \begin{enumerate}
        \item[(i)] $\theta$ is an isomorphism;
        \item[(ii)] $P_R$ and ${}_R Q$ are finitely generated projective;
        \item[(iii)] ${}_S P$ and $Q_S$ are generators;
        \item[(iv)] $\hat{\phi}$ and $\bar{\phi}$ are isomorphisms;
        \item[(v)] $\lambda: S \to \operatorname{End}(P_R)$ and $\rho: S \to \operatorname{End}({}_R Q)$ are ring isomorphisms.
    \end{enumerate}
\end{enumerate}
[Hint: For (iii) observe that $\operatorname{Tr}_S(P) \geq \hat{\theta}(Q)(P) = \theta(P \otimes Q)$. Next suppose that $\sum_i \theta(x_i \otimes f_i) = 1_S \in S$. Then $\sum_j(y_j \otimes g_j) = \sum_i(x_i \otimes f_i(\sum_j \theta(y_j \otimes g_j)))$, and it follows that $\theta$ is monic. Also $(x_i)$ and $(\bar{\phi}(f_i))$ form a dual basis for $P_R$. If $\bar{\phi}(f) = 0$, then show that $f = f1_S = 0$. If $g \in \operatorname{Hom}_R(P, R)$, then $g = \bar{\phi}(\sum_i g(x_i)f_i)$. If $\lambda(s) = 0$, then $s = s1_S = 0$. Finally, if $u \in \operatorname{End}(P_R)$, then $u = \lambda(\sum_i \theta(ux_i \otimes f_i))$.]
