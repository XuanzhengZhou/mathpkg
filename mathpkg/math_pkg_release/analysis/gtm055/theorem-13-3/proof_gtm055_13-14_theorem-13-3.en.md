---
role: proof
locale: en
of_concept: theorem-13-3
source_book: gtm055
source_chapter: "13-14"
source_section: "Section 15_Section_15"
---

Proof. It suffices to prove that $T$ is open. Let $U$ be an open set in $\mathcal{E}$, and suppose $y_0$ is a vector belonging to $T(U)$. There exists a vector $x_0$ in $U$ such that $Tx_0 = y_0$, and since $U$ is open, $x_0$ is an interior point of $U$. It follows that the translate $U - x_0$ is a neighborhood of the origin in $\mathcal{E}$, and, by the lemma just established, $T(U - x_0) = T(U) - y_0$ is a neighborhood of the origin in $\mathcal{F}$. Thus $T(U) = (T(U) - y_0) + y_0$ contains $y_0$ as an interior point, and the theorem follows.

Example A. If $||\cdot||_1$ and $||\cdot||_2$ are two quasinorms on the same linear space $\mathcal{E}$, let us say that $||\cdot||_1$ dominates $||\cdot||_2$ if, whenever $||x_n||_1 \to 0$ for a sequence $\{x_n\}$ in $\mathcal{E}$, then $||x_n||_2 \to 0$. This is equivalent to saying that the topology induced on $\mathcal{E}$ by $||\cdot||_1$ refines the one induced by $||\cdot||_2$, or, what comes to the same thing, that the identity mapping on $\mathcal{E}$ is continuous from the quasinormed space $(\mathcal{E}, ||\cdot||_1)$ obtained by equipping $\mathcal{E}$ with $||\cdot||_1$ to the space $(\mathcal{E}, ||\cdot||_2)$ obtained by using $||\cdot||_2$. (It is also

if $q_1$ and $q_2$ are any two functions in $\mathcal{C}([a, b])$ such that $\|q_1 - q_2\|_\infty \leq \varepsilon/2M$, and if $\alpha_1$ and $\alpha_2$ are any two complex numbers such that $|\alpha_1 - \alpha_2| \leq \varepsilon/2M$, then the solutions $y_1$ and $y_2$ of the initial value problems

$$y' = py + q_1, \quad y(c) = \alpha_1,$$

and

$$y' = py + q_2, \quad y(c) = \alpha_2,$$

respectively, satisfy the condition $\|y_1 - y_2\|_\infty + \|y'_1 - y'_2\|_\infty < \varepsilon$. This contains the following more conventional result: There exists a positive constant $M$ such that if $\varepsilon > 0$ and if $|\alpha_1 - \alpha_2| < \varepsilon/M$, then the solutions $y_1$ and $y_2$ of the differential equation

$$y' = py + q$$

(2)

satisfying the initial conditions $y_1(c) = \alpha_1$ and $y_2(c) = \alpha_2$ also satisfy the condition $\|y_1 - y_2\|_\infty \leq \varepsilon$. This is customarily expressed by saying that the solutions of (2) "depend continuously on their initial values."

It should be noted, of course, that these facts may be obtained directly, without recourse to the open mapping theorem, since the general solution of (2) can be explicitly written down and examined. The method used here, however, applies with equal ease to the $k$th order linear equation

$$y^{(k)} = a_{k-1}y^{(k-1)} + \cdots + a_0y + q,$$

where $q$ and the coefficients $a_0, \ldots, a_{k-1}$ are continuous complex-valued functions on the interval $[a, b]$. Moreover, the method can also be extended so as to deal with partial differential equations.

The open mapping theorem has a surprising and extremely
