---
role: proof
locale: en
of_concept: complementary-stable-subspace-for-maximal-cyclic
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Let $\varphi_a: E_a \rightarrow E_a$ denote the restriction of $\varphi$ to $E_a$, and let $\varphi^*: E^* \leftarrow E^*$ be the linear transformation in $E^*$ dual to $\varphi$. Then (cf. sec. 13.8) $E_a^\perp$ is stable under $\varphi^*$, and the induced linear transformation
$$\varphi_a^*: E^*/E_a^\perp \leftarrow E^*/E_a^\perp$$
is dual to $\varphi_a$ with respect to the induced scalar product between $E_a$ and $E^*/E_a^\perp$.

The corollary to Theorem I, sec. 13.11 implies that the minimum polynomial of $\varphi_a$ is again $\mu$. Hence the minimum polynomial of $\varphi_a^*$ is $\mu$. But $E_a$ and $E^*/E_a^\perp$ are dual, so that
$$\dim E^*/E_a^\perp = \dim E_a = \deg \mu.$$

Thus Theorem I, sec. 13.11 implies that $E^*/E_a^\perp$ is cyclic with respect to $\varphi_a^*$. Now let $\pi: E^* \rightarrow E^*/E_a^\perp$ be the projection and choose $a^* \in E^*$ so that $\bar{a}^* = \pi(a^*)$ generates $E^*/E_a^\perp$. Then the vectors $\bar{a}_\mu^* = (\varphi_a^*)^\mu \bar{a}^*$ ($\mu = 0 \ldots m-1$) form a basis of $E^*/E_a^\perp$. Hence the vectors $a_\mu^* = (\varphi^*)^\mu a^*$ ($\mu = 0 \ldots m-1$) are linearly independent.

Now consider the cyclic subspace $E_{a^*}$. Since $a_\mu^* \in E_{a^*}$ ($\mu = 0 \ldots m-1$) it follows that $\dim E_{a^*} \geq m$. On the other hand, Theorem I, sec. 13.11, implies that $\dim E_{a^*} \leq m$. Hence $\dim E_{a^*} = m$.

Finally, since $\pi a_\mu^* = \bar{a}_\mu^*$ ($\mu = 0 \ldots m-1$) it follows that the restriction of $\pi$ to $E_{a^*}$ is injective. Thus $E_{a^*} \cap E_a^\perp = 0$. Let $F = E_{a^*}^\perp$. Then $E = E_a \oplus F$ and $F$ is stable.
