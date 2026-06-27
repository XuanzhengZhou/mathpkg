---
role: proof
locale: en
of_concept: smooth-structure-on-vector-bundles
source_book: gtm033
source_chapter: "3"
source_section: "3. The Classification of Vector Bundles"
---

# Proof of Smooth Structure on C^r Vector Bundles (Theorem 3.5)

**Existence of a $C^\infty$ structure.** Let $\xi$ be a $C^r$ vector bundle over a $C^\infty$ manifold $M$. By the classification Theorem 3.4, there exists a $C^r$ classifying map

$$g: M \to G_{s,k}$$

with $\xi \cong_r g^* \gamma_{s,k}$, where $s > k + \dim M$. Since $M$ is a $C^\infty$ manifold and $G_{s,k}$ is a $C^\infty$ manifold, we can apply the smooth approximation theorem: the $C^r$ map $g$ can be $C^r$-approximated by a $C^\infty$ map $h: M \to G_{s,k}$, and sufficiently close $C^r$ approximations are $C^r$ homotopic to the original map. Thus $g \simeq h$ (homotopic in the $C^r$ sense).

By the classification theorem (homotopic maps give isomorphic pullbacks), we have

$$\xi \cong_r g^* \gamma_{s,k} \cong_r h^* \gamma_{s,k}.$$

But $h^*\gamma_{s,k}$ is a $C^\infty$ vector bundle, because $h$ is $C^\infty$ and the universal bundle $\gamma_{s,k}$ over the Grassmannian is $C^\infty$. Therefore $\xi$ admits a compatible $C^\infty$ bundle structure (the one pulled back via $h$).

**Uniqueness up to $C^\infty$ isomorphism.** Suppose $\eta_0$ and $\eta_1$ are two $C^\infty$ $k$-plane bundles over $M$ that are $C^r$ isomorphic. Let

$$f_0, f_1: M \to G_{s,k}$$

be $C^\infty$ classifying maps for $\eta_0$ and $\eta_1$, respectively (using Theorem 3.4 with $s > k + n$). Since $\eta_0 \cong_r \eta_1$, the classification theorem implies that $f_0$ and $f_1$ are $C^r$ homotopic. Applying the $C^\infty$ approximation theorem to the homotopy $M \times I \to G_{s,k}$, we obtain a $C^\infty$ homotopy $H: M \times I \to G_{s,k}$ between $f_0$ and $f_1$ (after possibly adjusting near the boundary to ensure the homotopy is stationary on neighborhoods of $M \times \{0\}$ and $M \times \{1\}$).

Now pull back the universal bundle along this $C^\infty$ homotopy:

$$\zeta = H^* \gamma_{s,k},$$

which is a $C^\infty$ $k$-plane bundle over $M \times I$. Its restrictions to the two ends satisfy

$$\zeta|_{M \times \{0\}} \cong_\infty \eta_0, \qquad \zeta|_{M \times \{1\}} \cong_\infty \eta_1.$$

By Theorem 1.4 (the covering isomorphism theorem for vector bundles), two bundles over $M$ that are restrictions of the same bundle over $M \times I$ are $C^\infty$ isomorphic. Hence

$$\eta_0 \cong_\infty \eta_1.$$

Thus the $C^\infty$ structure on a $C^r$ bundle is unique up to $C^\infty$ isomorphism.

**Remark.** The same result holds with $C^\infty$ replaced by $C^\omega$ (real analytic), by using the analytic approximation Theorem 2.5.1 in place of the smooth approximation theorem. $\square$
