<!-- ===================== -->
<!--  Python Abstraction  -->
<!-- ===================== -->

![Author](https://img.shields.io/badge/Author-Enjoy%20Bhodra-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-OOP-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<h1 align="center">🎭 Python Abstraction</h1>
<p align="center">
Academic-style visual explanation of abstraction in Python (OOP)
</p>

<hr>

<h2>📘 About This File</h2>
<p>
This section explains <strong>Abstraction in Python OOP</strong> using
simple definitions and visual diagrams to help students understand
how implementation details are hidden from users.
</p>

<pre><code>abstraction.py</code> (Abstract Classes & Methods in Python)</pre>

<hr>

<!-- ========== What is Abstraction ========== -->
<h2>1️⃣ What is Abstraction?</h2>
<p>
Abstraction means <strong>hiding implementation details</strong> and
showing only essential features to the user.
</p>

<div align="center">
  <div style="border:2px solid #1F4E79;padding:14px;width:260px;background:#D9EAF7;color:#0D2240;">
    <strong>User Interface</strong><br>
    (What user sees)
  </div>

  <div style="font-size:22px;">⬇</div>

  <div style="border:2px dashed #6B7280;padding:14px;width:260px;background:#F3F4F6;color:#374151;">
    Hidden Implementation<br>
    (Internal Logic)
  </div>
</div>

<hr>

<!-- ========== Abstract Class ========== -->
<h2>2️⃣ Abstract Class</h2>
<p>
An abstract class is a class that <strong>cannot be instantiated</strong>
and is used as a blueprint for other classes.
</p>

<div align="center">
  <div style="border:2px solid #7C2D12;padding:12px;width:260px;background:#FDEBD0;color:#4A1C0F;">
    Abstract Class<br>
    <em>(Contains abstract methods)</em>
  </div>

  <div style="font-size:22px;">⬇</div>

  <div style="border:2px solid #166534;padding:12px;width:260px;background:#D1EBD3;color:#0A2F16;">
    Concrete Class<br>
    <em>(Implements methods)</em>
  </div>
</div>

<hr>

<!-- ========== Abstract Method ========== -->
<h2>3️⃣ Abstract Method</h2>
<p>
An abstract method is declared in an abstract class
but <strong>has no implementation</strong>.
</p>

<div align="center">
  <div style="border:2px solid #1F4E79;padding:12px;width:300px;background:#E8F1FB;color:#0D2240;">
    @abstractmethod<br>
    def calculate():
  </div>

  <div style="font-size:22px;">⬇</div>

  <div style="border:2px solid #166534;padding:12px;width:300px;background:#D1EBD3;color:#0A2F16;">
    def calculate():<br>
    &nbsp;&nbsp;return result
  </div>
</div>

<hr>

<!-- ========== abc Module ========== -->
<h2>4️⃣ abc Module</h2>
<p>
Python provides the <strong>abc</strong> module to implement abstraction
using abstract base classes.
</p>

<div align="center">
  <div style="border:2px solid #4B5563;padding:14px;width:300px;background:#F9FAFB;color:#111827;">
    from abc import ABC, abstractmethod
  </div>
</div>

<hr>

<!-- ========== Why Abstraction ========== -->
<h2>5️⃣ Why Use Abstraction?</h2>

<ul>
  <li>✔ Improves code readability</li>
  <li>✔ Enhances security</li>
  <li>✔ Reduces complexity</li>
  <li>✔ Enforces consistent structure</li>
</ul>

<hr>

<p align="center" style="color:#999;font-size:14px;">
© 2026 <strong>Enjoy Bhodra</strong><br>
Python OOP — Abstraction (Academic Documentation)
</p>
