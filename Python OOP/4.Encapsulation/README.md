<!-- ======================= -->
<!--  Python Encapsulation  -->
<!-- ======================= -->

![Author](https://img.shields.io/badge/Author-Enjoy%20Bhodra-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-OOP-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<h1 align="center">🐍 Python Encapsulation</h1>
<p align="center">
Academic-style visual explanation of Encapsulation in Python (OOP)
</p>

<hr>

<h2>📘 About This File</h2>

<p>
This repository contains a single Python file named:
</p>

<pre><code>encapsulation.py</code> (Encapsulation, Getter & Setter in Python)</pre>

<p>
This file is created for <strong>students</strong> to understand how data hiding
and controlled access work in Python Object-Oriented Programming.
</p>

<hr>

<!-- ========== What is Encapsulation ========== -->
<h2>🔐 What is Encapsulation?</h2>

<p>
Encapsulation is an OOP principle that <strong>binds data and methods together</strong>
and <strong>hides internal implementation details</strong> from outside access.
</p>

<p>
In Python, Encapsulation is achieved using:
</p>

<ul>
  <li>Private variables (<code>__variable</code>)</li>
  <li>Getter methods</li>
  <li>Setter methods</li>
</ul>

<hr>

<!-- ========== Visual Diagram ========== -->
<h2>📊 Encapsulation Diagram</h2>

<div align="center">
  <div style="border:2px solid #1F4E79;padding:12px;width:260px;background:#E8F1FB;color:#0D2240;">
    🔒 Private Data<br>
    <strong>__balance</strong>
  </div>

  <div style="font-size:22px;">⬇ ⬆</div>

  <div style="display:flex;gap:40px;justify-content:center;">
    <div style="border:2px solid #166534;padding:12px;width:200px;background:#D1EBD3;color:#0A2F16;">
      Getter Method<br>
      <strong>get_balance()</strong>
    </div>
    <div style="border:2px solid #7C2D12;padding:12px;width:200px;background:#FDEBD0;color:#4A1C0F;">
      Setter Method<br>
      <strong>set_balance()</strong>
    </div>
  </div>
</div>

<hr>

<!-- ========== Python Example ========== -->
<h2>🐍 Python Example</h2>

<pre><code>
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")


acc = BankAccount(5000)

print(acc.get_balance())   # Getter
acc.set_balance(7000)      # Setter
print(acc.get_balance())
</code></pre>

<hr>

<!-- ========== Key Points ========== -->
<h2>🧠 Key Concepts</h2>

<table border="1" cellpadding="8" cellspacing="0" width="100%">
  <tr style="background:#f2f2f2;">
    <th align="left">Concept</th>
    <th align="left">Purpose</th>
  </tr>
  <tr>
    <td>Encapsulation</td>
    <td>Protects data from direct access</td>
  </tr>
  <tr>
    <td>Private Variables</td>
    <td>Prevent unauthorized modification</td>
  </tr>
  <tr>
    <td>Getter</td>
    <td>Safely access private data</td>
  </tr>
  <tr>
    <td>Setter</td>
    <td>Modify data with validation</td>
  </tr>
</table>

<hr>

## 🔗 Connect with Me

- 💼 LinkedIn: https://www.linkedin.com/in/bhodra-enjoy
- 💻 GitHub: https://github.com/EnjoyBhodra

<hr>

## 📜 License (MIT)

This project is licensed under the **MIT License**.

You are free to:
- ✔ Use
- ✔ Modify
- ✔ Distribute
- ✔ Use commercially

<hr>

<p align="center" style="color:#999;font-size:14px;">
© 2026 <strong>Enjoy Bhodra</strong><br>
Python OOP & Encapsulation — Academic Documentation
</p>
