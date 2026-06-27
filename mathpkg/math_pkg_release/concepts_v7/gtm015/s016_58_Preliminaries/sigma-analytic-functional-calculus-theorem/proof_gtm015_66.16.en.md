---
role: proof
locale: en
of_concept: sigma-analytic-functional-calculus-theorem
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of Sigma-analytic functional calculus

Proof. If $\lambda$ is an interior point of $\sigma$, then int $(\sigma)$ is a neighborhood of $\lambda$ on which $f$ is the uniform limit of (rational) analytic functions.

In particular, if $\sigma$ has nonempty interior and if $u(\lambda) \equiv \lambda$ is the identity function on $\sigma$, then the complex conjugate function $u^*(\lambda) = \lambda^*$ does not belong to $\mathcal{A}(\sigma)$. Thus, while the continuous functional calculus for a normal operator $T$ encompasses $T^*$, in general the $\sigma(T)$-analytic functional calculus does not. This ‘defect’ is precisely what makes the theory of spectral sets applicable to nonnormal operators.

If $\sigma$ is a proper, closed subset of $\mathfrak{S}$, then the subalgebra $\mathcal{A}(\sigma)$ of $\mathcal{C}(\sigma)$ separates the points of $\sigma$. {Proof: If $\sigma$ excludes $\infty$ (i.e., if $\sigma \subset \mathbb{C

with unity. Incidentally, the converse was proved in (60.1). Assuming $a \in A$, $a^* = a$, it will suffice to show that $\varphi(a)$ is also self-adjoint. Since $\sigma(a)$ is real (58.4), we may define

$$v = (a - i1)(a + i1)^{-1}$$

($v$ is the ‘Cayley transform’ of $a$). Elementary algebra yields $v^*v = vv^* = 1$, thus $v$ is unitary. Then $\|v\| = \|v^{-1}\| = 1$. {Proof: $\|v\|^2 = \|v^*v\| = 1$ and $v^{-1} = v^*$.} By the hypothesis on $\varphi$, we have

$$\|\varphi(v)\| \leq \|v\| = 1, \quad \|\varphi(v)^{-1}\| = \|\varphi(v^{-1})\| \leq \|v^{-1}\| = 1;$$

thus, setting $V = \varphi(v)$, we have $\|V\| \leq 1$ and $\|V^{-1}\| \leq 1$. It follows that $V$ is unitary (see the proof of (66.11)). Elementary algebra shows that $1 - v$ is invertible and $a = i(1 + v)(1 - v)^{-1}$, therefore

$$\varphi(a) = i(I + V)(I - V)^{-1};$$

since $V^* = V^{-1}$, further elementary algebra then shows that $\varphi(a)^* = \varphi(a)$.

If $T$ is normal then $\sigma(T)$ is a spectral set for $T$ (66.10); this is not a satisfying example since, for a normal operator, the spectral theory described in Section 65 does even more. If $T$ is nonnormal, then $\sigma(T)$ need not be a spectral set for $T$ (66.29); but a trivial spectral set is $\mathbb{C}$. Does every operator $T$ have a bounded spectral set? The affirmative answer is due to von Neumann: the closed disc $\

(the two norms are calculated in the Banach algebras $\mathcal{L}(H)$ and $\mathcal{L}(K)$, respectively). On the other hand, since the unit circle is a spectral set for $U$ (66.11), so is $\Delta_1$ (66.7), thus

$$\|f(U)\| \leq \|f\|_{\Delta_1}.$$

The lemma is immediate from (*) and (**).
