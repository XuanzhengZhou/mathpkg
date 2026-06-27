---
role: proof
locale: en
of_concept: l2-delbar-estimate-theorem
source_book: gtm035
source_chapter: "Chapter 16"
source_section: "16.3"
---
# Proof of L^2 Estimate for the \bar{\partial}-Operator

**Theorem 16.3.** Fix $f$ in $C_{0,1}^1(\bar{\Omega})$. Let $f \in \mathcal{D}_{T_0^*} \cap \mathcal{D}_{S_0}$. Then

$$\|T_0^* f\|_1^2 + \|S_0 f\|_3^2 = \sum_{j,k} \int_{\Omega} f_j \bar{f}_k \frac{\partial^2 \phi}{\partial z_j \partial \bar{z}_k} e^{-\phi} dV$$

$$+ \sum_{j,k} \int_{\Omega} \left| \frac{\partial f_k}{\partial \bar{z}_j} \right|^2 e^{-\phi} dV + \sum_{j,k} \int_{\partial \Omega} f_j \bar{f}_k \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} e^{-\phi} dS,$$

where $dS$ denotes the element of surface area on $\partial \Omega$.

**Proof.** We work in the weighted $L^2$ spaces introduced earlier. Let $H_1 = L^2(\Omega)$ with weight $e^{-\phi}$, $H_2 = L^2_{0,1}(\Omega)$ with weight $e^{-\phi}$, and $H_3$ be the completion of $C_{0,2}^1(\bar{\Omega})$ under a suitable inner product making $\bar{\partial}$ bounded.

The operators $T_0$ and $S_0$ are the closures of $\bar{\partial}$ acting on $(0,0)$-forms and $(0,1)$-forms respectively. They satisfy $S_0 \circ T_0 = 0$.

**Step 1: Computation of $T_0^* f$.** For $u \in C^1(\bar{\Omega})$ and $f \in C_{0,1}^1(\bar{\Omega})$, we compute $(T_0 u, f)_2$ using integration by parts. Fix $j$:

$$\int_{\Omega} \frac{\partial u}{\partial \bar{z}_j} \bar{f}_j e^{-\phi} dV = \int_{\Omega} \frac{\partial}{\partial \bar{z}_j} (u \bar{f}_j e^{-\phi}) dV - \int_{\Omega} u \frac{\partial}{\partial \bar{z}_j} (\bar{f}_j e^{-\phi}) dV$$

$$= \int_{\partial \Omega} u \bar{f}_j e^{-\phi} \frac{\partial \rho}{\partial \bar{z}_j} dS - \int_{\Omega} u \frac{\partial}{\partial \bar{z}_j} (\bar{f}_j e^{-\phi}) dV,$$

where we have used the complex Green's formula with $\rho$ a defining function for $\Omega$ (so $\rho = 0$ on $\partial \Omega$ and $|\nabla \rho| = 1$ on $\partial \Omega$). Summing over $j$:

$$(T_0 u, f)_2 = -\int_{\Omega} u \sum_j \frac{\partial}{\partial \bar{z}_j} (\bar{f}_j e^{-\phi}) dV + \int_{\partial \Omega} u \sum_j \bar{f}_j \frac{\partial \rho}{\partial \bar{z}_j} e^{-\phi} dS.$$

On the other hand, if $f \in \mathcal{D}_{T_0^*}$, then by definition of the adjoint:

$$(T_0 u, f)_2 = \int_{\Omega} u \overline{T_0^* f} e^{-\phi} dV.$$

Since these hold for all $u \in C^1(\bar{\Omega})$ (which is dense), we conclude:

**(i)** $\sum_j \bar{f}_j \frac{\partial \rho}{\partial \bar{z}_j} = 0$ on $\partial \Omega$, which is boundary condition (9), and

**(ii)** $\overline{T_0^* f} e^{-\phi} = -\sum_j \frac{\partial}{\partial \bar{z}_j} (\bar{f}_j e^{-\phi}) = \overline{\sum_j \delta_j f_j}$, where we define the operator

$$\delta_j g = e^{\phi} \frac{\partial}{\partial z_j} (g e^{-\phi}).$$

Thus the adjoint acts as $T_0^* f = \sum_j \delta_j f_j$, with domain characterized by the boundary condition $\sum_j f_j \frac{\partial \rho}{\partial z_j} = 0$ on $\partial \Omega$.

**Step 2: Computation of $\|T_0^* f\|_1^2$.** Using the expression $T_0^* f = \sum_k \delta_k f_k$, we compute:

$$\|T_0^* f\|_1^2 = \sum_{j,k} \int_{\Omega} \delta_j f_j \overline{\delta_k f_k} e^{-\phi} dV.$$

Applying the commutation relation $[\delta_k, \frac{\partial}{\partial \bar{z}_j}] = \frac{\partial^2 \phi}{\partial \bar{z}_j \partial z_k}$ and integrating by parts repeatedly yields:

$$\|T_0^* f\|_1^2 = \int_{\Omega} \sum_{j,k} \frac{\partial^2 \phi}{\partial z_j \partial \bar{z}_k} f_j \bar{f}_k e^{-\phi} dV + \int_{\Omega} \sum_{j,k} \frac{\partial f_j}{\partial \bar{z}_k} \overline{\frac{\partial f_k}{\partial \bar{z}_j}} e^{-\phi} dV$$

$$- \int_{\partial \Omega} \sum_{j,k} f_j \overline{\frac{\partial f_k}{\partial \bar{z}_j}} \frac{\partial \rho}{\partial \bar{z}_k} e^{-\phi} dS + \int_{\partial \Omega} \sum_{j,k} \overline{\delta_k f_k} f_j \frac{\partial \rho}{\partial z_j} e^{-\phi} dS.$$

Using the boundary condition (9), the boundary terms simplify to:

$$- \sum_{j,k} f_j \overline{\frac{\partial f_k}{\partial \bar{z}_j}} \frac{\partial \rho}{\partial \bar{z}_k} = \sum_{j,k} f_j \bar{f}_k \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} \quad \text{on } \partial \Omega.$$

This follows by differentiating the identity $\sum_k f_k \frac{\partial \rho}{\partial z_k} = 0$ along $\partial \Omega$ and using the fact that the complex tangential gradient of this function is a multiple of the gradient of $\rho$.

Hence, after simplification:

$$\|T_0^* f\|_1^2 = \int_{\Omega} \sum_{j,k} \frac{\partial^2 \phi}{\partial z_j \partial \bar{z}_k} f_j \bar{f}_k e^{-\phi} dV + \int_{\Omega} \sum_{j,k} \frac{\partial f_j}{\partial \bar{z}_k} \overline{\frac{\partial f_k}{\partial \bar{z}_j}} e^{-\phi} dV$$

$$+ \int_{\partial \Omega} \sum_{j,k} f_j \bar{f}_k \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} e^{-\phi} dS. \tag{23}$$

**Step 3: Computation of $\|S_0 f\|_3^2$ (Lemma 16.6).** For $f \in \mathcal{D}_{S_0} \cap C_{0,1}^1(\bar{\Omega})$, a direct computation using $S_0 f = \bar{\partial}f$ gives:

$$\|S_0 f\|_3^2 = \int_{\Omega} \sum_{j,k} \left| \frac{\partial f_k}{\partial \bar{z}_j} \right|^2 e^{-\phi} dV - \int_{\Omega} \sum_{j,k} \frac{\partial f_j}{\partial \bar{z}_k} \overline{\frac{\partial f_k}{\partial \bar{z}_j}} e^{-\phi} dV.$$

(See the proof of Lemma 16.6 for the detailed algebraic expansion.)

**Step 4: Conclusion.** Adding the expressions from Steps 2 and 3, the two double sums involving $\frac{\partial f_j}{\partial \bar{z}_k} \overline{\frac{\partial f_k}{\partial \bar{z}_j}}$ cancel, yielding precisely formula (7):

$$\|T_0^* f\|_1^2 + \|S_0 f\|_3^2 = \sum_{j,k} \int_{\Omega} f_j \bar{f}_k \frac{\partial^2 \phi}{\partial z_j \partial \bar{z}_k} e^{-\phi} dV$$

$$+ \sum_{j,k} \int_{\Omega} \left| \frac{\partial f_k}{\partial \bar{z}_j} \right|^2 e^{-\phi} dV + \sum_{j,k} \int_{\partial \Omega} f_j \bar{f}_k \frac{\partial^2 \rho}{\partial z_j \partial \bar{z}_k} e^{-\phi} dS.$$

**Step 5: Extension to all $f \in \mathcal{D}_{T_0^*} \cap \mathcal{D}_{S_0}$.** The above computation was carried out for smooth $f \in C_{0,1}^1(\bar{\Omega})$. For general $f \in \mathcal{D}_{T_0^*} \cap \mathcal{D}_{S_0}$, there exists a sequence $\{f_n\} \subset \mathcal{D}_{T_0^*} \cap \mathcal{D}_{S_0} \cap C_{0,1}^1(\bar{\Omega})$ such that as $n \to \infty$:

$$\|f_n - f\|_2 \to 0, \quad \|T_0^* f_n - T_0^* f\|_1 \to 0, \quad \|S_0 f_n - S_0 f\|_3 \to 0.$$

This approximation follows from the elliptic regularity theory (Lemma 16.8) and the density of smooth forms. Passing to the limit, the identity (7) holds for all $f \in \mathcal{D}_{T_0^*} \cap \mathcal{D}_{S_0}$. $\square$

**Corollary (Theorem 16.2 applied).** Choosing $\phi(z) = |z|^2$, we obtain $\frac{\partial^2 \phi}{\partial z_j \partial \bar{z}_k} = \delta_{jk}$, so the first integral becomes $\|f\|_2^2$. If in addition $\Omega$ is strictly pseudoconvex, then the boundary integral is nonnegative by the strict plurisubharmonicity of $\rho$. Hence

$$\|T_0^* f\|_1^2 + \|S_0 f\|_3^2 \geq \|f\|_2^2,$$

which is the fundamental estimate needed for the Hormander $L^2$ theory. Applying Theorem 16.2 (the abstract duality argument for closed operators) yields: for every $S_0$-closed $(0,1)$-form $g$, there exists $u$ with $T_0 u = g$ and $\|u\|_1 \leq \|g\|_2$.
