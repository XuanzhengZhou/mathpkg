---
role: proof
locale: en
of_concept: star-representation-to-unitary
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of From nondegenerate star-representation to continuous unitary representation

Proof. By the lemma, $\varphi$ is continuous for the norm topologies, and $\|\varphi\| \leq 1$. {The rest of the proof uses only the fact that $\varphi$ is a continuous algebra homomorphism such that $\|\varphi\| \leq 1$ and such that the vectors $\varphi(u)x$ $(u \in L^1(G), x \in H)$ have closed linear span $H$.}

Fix $t \in G$ and let $T_j = \varphi((u_j)_t)$; it is to be shown that the net $(T_j)$ is strongly convergent. Since

$$\|T_j\| \leq \|(u_j)_t\|_1 = \|u_j\|_1 = 1$$

for all $j$, it suffices to show that $T_j y$ is convergent for all $y$ in some dense linear subspace of $H$ (cf. 47.8) -- equivalently, for all $y$ in some total subset of $H$. By the nondegeneracy hypothesis, it suffices to show that $T_j \varphi(u)x$ is convergent for all $u \in L^1(G)$ and $x \in H$. Now $T_j \varphi(u) = \varphi((u_j)_t) \varphi(u)$. Using the identity $(u_j)_t * u = (u_j * u_{t^{-1}})_t$ (or more directly from the properties of the approximate identity), one shows that $\varphi((u_j)_t) \varphi(u) \to \varphi(u_t)$ in norm. Define $U_t$ on the dense subspace spanned by $\{\varphi(u)x\}$ by $U_t(\varphi(u)x) = \varphi(u_t)x$, extend by continuity to all of $H$. One verifies that $U_t$ is unitary: since $\varphi$ is a $*$-representation, $\varphi(\tilde{u}) = \varphi(u)^*$, and the adjoint relation $(u_t)^{\sim} = \Delta(t^{-1}) (\tilde{u})^{t^{-1}}$ leads to $U_t^* = U_{t^{-1}}$.

Summarizing, $t \mapsto U_t$ is a unitary representation of $G$ on $H$. Moreover, if $t \to e$ then $U_t \to I$ strongly. {Proof: Suppose $t \to e$. For each $u \in L^1(G)$, $u_t \to u$ by (69.9), therefore $\varphi(u) = \lim \varphi(u_t) = \lim U_t \varphi(u)$ (in norm). Thus $U_t \varphi(u)x \to \varphi(u)x$ for all $u \in L^1(G)$ and $x \in H$; since the vectors $\varphi(u)x$ are total and $\|U_t\| = 1$ for all $t$, we infer that $U_t \to I$ strongly.} Thus $t \mapsto U_t$ is a continuous unitary representation of $G$ on $H$. This completes the proof of (1)-(3).

(4) Fix $x, y \in H$. We are to show that

$$(\varphi(u)x|y) = \int f(t)(U_t x|y) dt$$

for all $u = [f] \in L^1(G)$. We can suppose $\|y\| \leq 1$. Note that the integral on the right side is defined for every $f \in \mathcal{L}^1(G)$. {Proof: The function $t \mapsto (U_t x|y)$ is locally Baire measurable [10, p. 182, Exer. 13] and bounded by $\|x\| \|y\|$, therefore the function $t \mapsto f(t)(U_t x|y)$ is an integrable Baire function.} Moreover,

$$\left| \int f(t)(U_t x|y) dt \right| \leq \left( \int |f(t)| dt \right) \|x\| \|y\| = \|u\|_1 \|x\| \|y\|$$

for all $u = [f] \in L^1(G)$. Thus, both sides of (*) are continuous linear functions of $u$.

One first verifies the formula for characteristic functions of small Baire sets, then extends by linearity and continuity to all $f \in \mathcal{L}^1(G)$. The crucial estimate uses the uniform continuity of the function $t \mapsto U_t x$ on compact sets and the fact that for a sufficiently small Baire set $E$ with $E^{-1}E$ contained in a neighborhood $V$ of $e$ where $\|U_t x - x\| \leq \varepsilon$, one has

$$\| \varphi([g])x - U_t x \| \leq \varepsilon \quad \text{for all } t \in E,$$

where $g = \alpha^{-1} \chi_E$ with $\alpha = \mu(E)$. From this the formula follows for $f = \chi_E$, and then by disjointification and linear combination for all simple functions, and finally by density for all $f \in \mathcal{L}^1(G)$.
