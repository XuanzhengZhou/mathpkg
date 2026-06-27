---
role: exercise
locale: en
chapter: "5"
section: "25"
exercise_number: 1
---

Find the shape of the region of stability in the $\varepsilon,\omega$-plane for the system described by the equations

$$\ddot{x} = -f^2(t)x$$

where $f$ is periodic. The boundary of the zone of stability has the equation

$$|\text{tr } A| = \left| 2c_1c_2 - \left( \frac{\omega_1}{\omega_2} + \frac{\omega_2}{\omega_1} \right)s_1s_2 \right| = 2.$$

Since $\varepsilon \ll 1$, we have $\omega_1/\omega_2 = (\omega + \varepsilon)/(\omega - \varepsilon) \approx 1$. Introduce the notation

$$\frac{\omega_1}{\omega_2} + \frac{\omega_2}{\omega_1} = 2(1 + \Delta),$$

where $\Delta = (2\varepsilon^2/\omega^2) + O(\varepsilon^4) \ll 1$. Using the relations $2c_1c_2 = \cos 2\pi\varepsilon + \cos 2\pi\omega$ and $2s_1s_2 = \cos 2\pi\varepsilon - \cos 2\pi\omega$, rewrite the boundary condition in the form

$$-\Delta \cos 2\pi\varepsilon + (2 + \Delta)\cos 2\pi\omega = \pm 2$$

or

$$\cos 2\pi\omega = \frac{2 + \Delta \cos 2\pi\varepsilon}{2 + \Delta}, \quad \cos 2\pi\omega = \frac{-2 + \Delta \cos 2\pi\varepsilon}{2 + \Delta}.$$

In the first case $\cos 2\pi\omega \approx 1$. Therefore, set $\omega = k + a$, $|a| \ll 1$ with $\cos 2\pi\omega = \cos 2\pi a = 1 - 2\pi^2 a^2 + O(a^4)$. Show that the stability region is determined by this boundary equation.
