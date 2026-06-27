---
role: exercise
locale: en
chapter: "III"
section: "6"
exercise_number: 1
---

Let $(X, \mathcal{O}_X)$ be a ringed space, and let $\mathcal{F}', \mathcal{F}'' \in \operatorname{Mod}(X)$. An **extension** of $\mathcal{F}''$ by $\mathcal{F}'$ is a short exact sequence

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0.$$

Two extensions are **equivalent** if there is a commutative diagram

$$\xymatrix{
0 \ar[r] & \mathcal{F}' \ar[r] \ar@{=}[d] & \mathcal{F}_1 \ar[r] \ar[d]^{\cong} & \mathcal{F}'' \ar[r] \ar@{=}[d] & 0 \\
0 \ar[r] & \mathcal{F}' \ar[r] & \mathcal{F}_2 \ar[r] & \mathcal{F}'' \ar[r] & 0
}$$

Show that the set of equivalence classes of extensions of $\mathcal{F}''$ by $\mathcal{F}'$ is in natural one-to-one correspondence with $\operatorname{Ext}^1(\mathcal{F}'', \mathcal{F}')$.
