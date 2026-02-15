<!-- ===================== -->
<!--  Python Polymorphism -->
<!-- ===================== -->

![Author](https://img.shields.io/badge/Author-Enjoy%20Bhodra-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-OOP-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<h1 align="center">🐍 Python Polymorphism</h1>
<p align="center">
Academic-style visual explanation of Polymorphism in Python (OOP)
</p>

<hr>

<h2>📘 About This File</h2>

<p>
This repository contains Python examples that explain
<strong>Polymorphism</strong> in Object-Oriented Programming using Python.
</p>

<p>
This is a <strong>learning & academic reference file</strong>, not a project.
</p>

<hr>

<h2>🧠 What is Polymorphism?</h2>

<p>
<strong>Polymorphism</strong> means <em>one name, many forms</em>.
The same method or function name behaves differently
depending on the object calling it.
</p>

<hr>

<!-- ========== Method Overriding ========== -->
<h2>1️⃣ Method Overriding (Runtime Polymorphism)</h2>

<p>
A child class provides its own implementation of a method
already defined in the parent class.
</p>

<div align="center">
  <div style="border:2px solid #1F4E79;padding:12px;width:240px;background:#D9EAF7;color:#0D2240;">
    Parent Class <br><code>speak()</code>
  </div>

  <div style="font-size:22px;">⬇</div>

  <div style="border:2px solid #166534;padding:12px;width:240px;background:#D1EBD3;color:#0A2F16;">
    Child Class <br><code>speak()</code> (Modified)
  </div>
</div>

<hr>

<!-- ========== Duck Typing ========== -->
<h2>2️⃣ Duck Typing</h2>

<p>
Python follows the philosophy:
<strong>"If it looks like a duck and quacks like a duck, it is a duck."</strong>
</p>

<p>
Object type does not matter — only behavior matters.
</p>

<div align="center">
  <div style="display:flex;gap:30px;justify-content:center;">
    <div style="border:2px solid #1F4E79;padding:12px;width:180px;background:#E8F1FB;color:#0D2240;">
      Object A <br><code>move()</code>
    </div>
    <div style="border:2px solid #1F4E79;padding:12px;width:180px;background:#E8F1FB;color:#0D2240;">
      Object B <br><code>move()</code>
    </div>
  </div>
</div>

<hr>

<!-- ========== Operator Overloading ========== -->
<h2>3️⃣ Operator Overloading</h2>

<p>
Same operator behaves differently for different data types.
</p>

<div align="center">
  <div style="border:2px solid #1F4E79;padding:12px;width:260px;background:#D9EAF7;color:#0D2240;">
    <code>+</code> for numbers → Addition
  </div>

  <div style="font-size:22px;">⬇</div>

  <div style="border:2px solid #166534;padding:12px;width:260px;background:#D1EBD3;color:#0A2F16;">
    <code>+</code> for strings → Concatenation
  </div>
</div>

<hr>

<h2>🧪 Simple Python Example</h2>

<pre><code>
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane flies faster")

def lift_off(entity):
    entity.fly()

lift_off(Bird())
lift_off(Airplane())
</code></pre>

<hr>

<h2>✅ Why Polymorphism is Important?</h2>

<ul>
  <li>Improves code flexibility</li>
  <li>Reduces conditional statements</li>
  <li>Supports dynamic behavior</li>
  <li>Makes code scalable and reusable</li>
</ul>

<hr>

<h2>🧩 OOP Pillar</h2>

<p>
Polymorphism is one of the <strong>four main pillars of OOP</strong>:
</p>

<ul>
  <li>Encapsulation</li>
  <li>Abstraction</li>
  <li>Inheritance</li>
  <li><strong>Polymorphism</strong></li>
</ul>

<hr>

## 🔗 Connect with Me

- 💼 LinkedIn: https://www.linkedin.com/in/bhodra-enjoy
- 💻 GitHub: https://github.com/EnjoyBhodra

<hr>

## 📜 License (MIT)

This learning material is licensed under the **MIT License**.

You are free to:
- ✔ Use
- ✔ Modify
- ✔ Distribute
- ✔ Use commercially

<hr>

<p align="center" style="color:#999;font-size:14px;">
© 2026 <strong>Enjoy Bhodra</strong><br>
Python OOP & Polymorphism — Academic Documentation
</p>
