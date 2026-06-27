---
role: proof
locale: en
of_concept: wild-arc-tame-theorem
source_book: gtm047
source_chapter: "19"
source_section: "19 (A Wild Arc with Simply Connected Complement)"
---

In each spherical shell $\text{Cl}(C_i - C_{i+1})$, take a polyhedral 3-cell $D_i$, such that $B_i$ is unknotted in $D_i$, and $D_i$ intersects $\text{Bd } C_i$ and $\text{Bd } C_{i+1}$ in 2-cells $d_i$ and $d_{i+1}$. (The notation conveys that

$$D_i \cap \text{Bd } C_{i+1} = D_{i+1} \cap \text{Bd } C_{i+1},$$

and this property is easily arranged.) Let

$$E_i = \text{Cl} \left[ C_i - (D_i \cup C_{i+1}) \right].$$

Then $E_i$ is a polyhedral 3-cell. Let $L$ be the (straight) line through $P$ and the points $P_i$; let

$$B_i' = L \cap \text{Cl}(C_i - C_{i+1}),$$

and let $D_i'$ be chosen for $B_i'$ in $\text{Cl}(C_i - C_{i+1})$ in the same way that $D_i$ was chosen for $B_i$. We take the sets $D_i'$ in such a way that $D_i' \cap \text{Bd } C_j = D_i \cap \text{Bd } C_j$ for each $i$ and $j$. Let $A_1'$ be the union of the sets $B_i'$ and $P$. We now define a homeomorphism $\phi: \mathbf{R}^3 \leftrightarrow \mathbf{R}^3$, in the following stages:

(1) $\phi$ is the identity in $\mathbf{R}^3 - C_1$.

(2) $\phi$ is the identity on each set $\text{Bd } C_i$.

(3) Moving inward from $C_1$, we extend $\phi$ to send each $D_i$ onto $D_i'$ and each $E_i$ onto the corresponding $E_i'$, using the unknottedness of the broken line segments to ensure the extension is a PLH at each stage. By construction, $\phi$ sends $A_1$ onto the straight line segment $A_1'$, proving $A_1$ is tame.
