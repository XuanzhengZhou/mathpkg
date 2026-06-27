---
role: proof
locale: en
of_concept: unitary-to-star-representation
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of From continuous unitary representation to nondegenerate star-representation

Proof. (1) The uniqueness assertion is obvious, since the right side of (*) depends only on the given unitary representation.

Suppose $u \in L^1(G)$, say $u = [f]$. For each pair of vectors $x, y$ in $H$, define

$$B_u(x, y) = \int f(t)(U_t x|y) dt$$

(it is shown in the proof of (69.20) that the integral exists). Clearly $B_u$ is a sesquilinear form on $H$ such that

$$|B_u(x, y)| \leq \|u\|_1 \|x\| \|y\|$$

for all $x, y \in H$; let $\varphi(u)$ be the operator on $H$ such that $B_u(x, y) = (\varphi(u)x|y)$ for all $x, y \in H$ (43.9).

We have thus defined a mapping $\varphi: L^1(G) \to \mathcal{L}(H)$ satisfying (*). It is routine to check that $\varphi$ is linear; moreover, for $u = [f], v = [g] \in L^1(G)$ and $x, y \in H$, since $h = f * g$ a.e., we have (by Fubini's theorem and the left invariance of Haar measure)

$$\langle \varphi(uv)x | y \rangle = \int h(t)(U_t x | y) dt$$

$$= \int \left( \int f(s) g(s^{-1}t) ds \right)(U_t x | y) dt$$

$$= \int f(s) \left( \int g(s^{-1}t)(U_t x | y) dt \right) ds$$

$$= \int f(s) \left( \int g(t)(U_t x | U_s^* y) dt \right) ds$$

$$= \int f(s)(\varphi(v)x | U_s^* y) ds$$

$$= \int f(s)(U_s \varphi(v)x | y) ds$$

$$= (\varphi(u) \varphi(v)x | y).$$

Thus $\varphi(uv) = \varphi(u)\varphi(v)$, so $\varphi$ is an algebra homomorphism.

To show $\varphi(\tilde{u}) = \varphi(u)^*$: using the property $\tilde{f}(t) = \Delta(t)f(t^{-1})^*$ and the unitarity of $U_t$, one computes

$$(\varphi(\tilde{u})x | y) = \int \Delta(t) f(t^{-1})^* (U_t x | y) dt = \int f(t)^* (U_t^* x | y) dt = (x | \varphi(u)y),$$

which shows $\varphi(\tilde{u}) = \varphi(u)^*$. Hence $\varphi$ is a $*$-representation.

(2) Let $x \in H$, $\|x\| = 1$; we seek $u \in L^1(G)$ such that $\varphi(u)x \neq \theta$. Since $(U_e x | x) = (Ix | x) = 1$ and the representation $t \mapsto U_t$ is continuous, there exists a neighborhood $V$ of $e$ such that

$$|(U_t x | x) - 1| \leq 1/2 \quad \text{for all } t \in V.$$

We can suppose $V$ is a Baire set (e.g., a compact $G_\delta$). Choose any $f \in \mathcal{F}_V$ (cf. 69.12) and let $u = [f]$. Then

$$\langle \varphi(u)x | x \rangle - 1 = \int f(t)(U_t x | x) dt - \int f(t) dt = \int_V f(t)[(U_t x | x) - 1] dt,$$

thus

$$|\langle \varphi(u)x | x \rangle - 1| \leq \int_V f(t)|(U_t x | x) - 1| dt \leq \frac{1}{2} \int f(t) dt = \frac{1}{2},$$

so $\varphi(u)x \neq \theta$. Since the closed linear span of $\{\varphi(u)x : u \in L^1(G), x \in H\}$ contains all vectors $x$ (by the approximate identity argument), $\varphi$ is nondegenerate.

(3) For all $u = [f] \in L^1(G)$, $s \in G$ and $x, y \in H$,

$$(\varphi(u_s)x | y) = \int f(s^{-1}t)(U_t x | y) dt = \int f(t)(U_{st} x | y) dt = \int f(t)(U_t x | U_s^* y) dt = (U_s \varphi(u)x | y).$$

(4) Let $(u_j)_{j \in J}$ be an approximate identity in $L^1(G)$, and let $t \in G$. By (3), we have

$$\varphi((u_j)_t) = U_t \varphi(u_j)$$

for all $j$; on the other hand, $\varphi(u_j) \to I$ strongly by (69.20) applied to $\varphi$, thus $\varphi((u_j)_t) \to U_t I = U_t$ strongly.
