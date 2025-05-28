# CFG-Implementation
Context- Free Grammar Implementation in python

# 📚 Tema 3 - Limbaje Formale și Automate

## 🔍 Descriere

Acest proiect implementează funcționalități esențiale pentru lucrul cu o gramatică independentă de context (CFG).
Gramatica folosită este: S → aSb | ε
Limbajul generat este: L = { aⁿbⁿ | n ≥ 0 }
## ✅ Ce face fiecare componentă

| Funcționalitate       | Descriere |
|-----------------------|-----------|
| CFG Definition        | Definim simbolurile terminale, neterminale, regulile și simbolul de start |
| String Generator      | Generează până la 10 șiruri aleatorii de maxim 10 caractere |
| Leftmost Derivation   | Arată pașii derivării folosind înlocuirea celui mai din stânga neterminal |
| Rightmost Derivation  | Arată pașii derivării folosind înlocuirea celui mai din dreapta neterminal |
| Recognizer            | Verifică dacă un șir aparține limbajului definit |
| Bonus: aⁿbⁿcⁿ Tester   | Testează apartenența unui șir la limbajul { aⁿbⁿcⁿ | n ≥ 1 } — limbaj care **nu este context-free** |
