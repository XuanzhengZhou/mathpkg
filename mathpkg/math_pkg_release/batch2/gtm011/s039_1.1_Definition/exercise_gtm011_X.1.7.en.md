---
role: exercise
locale: en
chapter: "X"
section: "1"
exercise_number: 7
---

Let $u(x, y)$ be defined on $G$ and put $U(r, \theta) = u(r \cos \theta, r \sin \theta)$.

(a) Show that

$$r^2 \left[ \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right] = r^2 \frac{\partial^2 U}{\partial r^2} + r \frac{\partial U}{\partial r} + \frac{\partial^2 U}{\partial \theta^2} = r \frac{\partial}{\partial r} \left( r \frac{\partial U}{\partial r} \right) + \frac{\partial^2 U}{\partial \theta^2}.$$

So if $0 \notin G$ then $u$ is harmonic iff

$$r \frac{\partial}{\partial r} \left( r \frac{\partial U}{\partial r} \right) + \frac{\partial^2 U}{\partial \theta^2} = 0.$$

(b) Let $u$ have the property that it depends only on $|z|$ and not $\arg z$. That is, $u(z) = \varphi(|z|)$. Show that $u$ is harmonic iff $u(z) = a \log |z| + b$ for some constants $a$ and $b$.
