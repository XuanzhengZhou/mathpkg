---
role: proof
locale: en
of_concept: ford-circles-tangency-points
source_book: gtm041
source_chapter: "5"
source_section: "5.5"
---

Write $\alpha_1 = \alpha_1(h, k)$. Referring to Figure 5.3, the tangency point can be expressed as

$$\alpha_1 = \left( \frac{h}{k} - a \right) + i \left( \frac{1}{2k^2} - b \right).$$

To determine $a$ and $b$, use similar right triangles formed by the centers of $C(h,k)$ and $C(h_1, k_1)$ and their horizontal separation. This gives

$$\frac{a}{\frac{h}{k} - \frac{h_1}{k_1}} = \frac{\frac{1}{2k^2}}{\frac{1}{2k^2} + \frac{1}{2k_1^2}} = \frac{k_1^2}{k^2 + k_1^2}.$$

Since $h/k - h_1/k_1 = (hk_1 - h_1k)/(kk_1) = 1/(kk_1)$ by the unimodular condition $hk_1 - h_1k = 1$ (from Theorem 5.5 for consecutive Farey fractions), we obtain

$$a = \frac{1}{kk_1} \cdot \frac{k_1^2}{k^2 + k_1^2} = \frac{k_1}{k(k^2 + k_1^2)}.$$

Similarly,

$$\frac{b}{\frac{1}{2k^2}} = \frac{\frac{1}{2k^2} - \frac{1}{2k_1^2}}{\frac{1}{2k^2} + \frac{1}{2k_1^2}} = \frac{k_1^2 - k^2}{k_1^2 + k^2},$$

so

$$b = \frac{1}{2k^2} \cdot \frac{k_1^2 - k^2}{k^2 + k_1^2} = \frac{k_1^2 - k^2}{2k^2(k^2 + k_1^2)}.$$

Then

$$\frac{1}{2k^2} - b = \frac{1}{2k^2} - \frac{k_1^2 - k^2}{2k^2(k^2 + k_1^2)} = \frac{k^2 + k_1^2 - (k_1^2 - k^2)}{2k^2(k^2 + k_1^2)} = \frac{2k^2}{2k^2(k^2 + k_1^2)} = \frac{1}{k^2 + k_1^2}.$$

Hence

$$\alpha_1 = \frac{h}{k} - \frac{k_1}{k(k^2 + k_1^2)} + \frac{i}{k^2 + k_1^2}.$$

The formula for $\alpha_2(h, k)$ is obtained similarly by symmetry. The statement about $\alpha_1$ lying on the semicircle follows from the geometric construction: the line joining the centers of $C(h,k)$ and $C(h_1,k_1)$ passes through the tangency point, and the angle subtended by the diameter $[h_1/k_1, h/k]$ is a right angle.
