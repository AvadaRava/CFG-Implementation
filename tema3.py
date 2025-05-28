import random

class CFG:
    def __init__(self):
        # Sarcina 1: Definirea unei gramatici CFG 
        self.non_terminals = {'S'}
        self.terminals = {'a', 'b'}
        self.start_symbol = 'S'    
        self.rules = {
            'S': ['aSb', ''] 
        }

    # Sarcina 2: Generator de String-uri
    def generate_strings(self, max_strings=10, max_len=10):
        generated_strings = set()
        attempts = 0
        while len(generated_strings) < max_strings and attempts < max_strings * 5:
            string = self._generate_recursive(self.start_symbol, max_len)
            if string is not None:
                generated_strings.add(string if string else "ε")
            attempts += 1
        return list(generated_strings)

    def _generate_recursive(self, symbol, max_len):
    
        terminal_count = sum(1 for c in symbol if c in self.terminals)
        if terminal_count > max_len:
            return None

        for i, char in enumerate(symbol):
            if char in self.non_terminals:
                production = random.choice(self.rules[char])
                new_symbol = symbol[:i] + production + symbol[i+1:]
                return self._generate_recursive(new_symbol, max_len)

        return symbol

    # Sarcina 4: Verificator de Apartenenta
    def recognize_string(self, target_string):
        if len(target_string) % 2 != 0:
            return False
        half_len = len(target_string) // 2
        return target_string == 'a' * half_len + 'b' * half_len

    # Sarcina 3: Derivare
    def display_rightmost_derivation(self, target_string):
        if not self.recognize_string(target_string):
            display_s = 'ε' if target_string == '' else target_string
            print(f"String-ul '{display_s}' nu apartine limbajului L(G) = {{a^n b^n | n >= 0}}.")
            return

        display_s = 'ε' if target_string == '' else target_string
        print(f"Derivarea dreapta pentru '{display_s}':")

        if target_string == "":
            print("S -> ε")
            return

        derivation_steps = ["S"]
        n = len(target_string) // 2
        current_string = "S"

        for _ in range(n):
            last_index = current_string.rfind('S')
            if last_index != -1:
                current_string = current_string[:last_index] + "aSb" + current_string[last_index + 1:]
                derivation_steps.append(current_string)

        current_string = current_string.replace("S", "")
        derivation_steps.append(current_string)

        print(" -> ".join(derivation_steps))

    def display_derivation(self, target_string):
        if not self.recognize_string(target_string):
            display_s = 'ε' if target_string == '' else target_string
            print(f"String-ul '{display_s}' nu apartine limbajului L(G) = {{a^n b^n | n >= 0}}.")
            return

        display_s = 'ε' if target_string == '' else target_string
        print(f"Derivarea stanga pentru '{display_s}':")
        
        if target_string == "":
            print("S -> ε")
            return

        derivation_steps = ["S"]
        n = len(target_string) // 2
        current_string = "S"

        for _ in range(n):
            current_string = current_string.replace("S", "aSb", 1)
            derivation_steps.append(current_string)

        current_string = current_string.replace("S", "")
        derivation_steps.append(current_string)

        print(" -> ".join(derivation_steps))


# Sarcina 5: Bonus
def recognize_an_bn_cn(s):
    if not s or any(c not in 'abc' for c in s):
        return False

    n = len(s)
    i = 0
    n_a = n_b = n_c = 0

    while i < n and s[i] == 'a':
        n_a += 1
        i += 1
   
    while i < n and s[i] == 'b':
        n_b += 1
        i += 1
   
    while i < n and s[i] == 'c':
        n_c += 1
        i += 1

    if i != n:
        return False
    return n_a == n_b == n_c and n_a >= 1

def main():
    print("--- Tema: Limbaje Formale si Automate ---")
    
    # Initializarea CFG din Sarcina 1
    cfg = CFG()
    print("\n[Sarcina 1] Definirea CFG:")
    print(f"Non-terminale: {cfg.non_terminals}")
    print(f"Terminale: {cfg.terminals}")
    print(f"Simbol de start: {cfg.start_symbol}")
    print(f"Reguli de productie: S -> aSb | ε")
    
    # --- Sarcina 2 ---
    print("\n[Sarcina 2] Generarea a 10 string-uri aleatorii (lungime max. 10):")
    generated = cfg.generate_strings(max_strings=10, max_len=10)
    print(generated)
    
    # --- Sarcina 3 & 4 ---
    print("\n[Sarcina 3 & 4] Derivare si Verificare Apartenenta:")
    test_strings = ["aabb", "ab", "", "aaabbb", "abb", "aab"]
    for s in test_strings:
        is_member = cfg.recognize_string(s)
        display_s = 'ε' if s == '' else s
        print(f"\nTestare string: '{display_s}'")
        print(f"Este membru al L(G)? -> {is_member}")
        if is_member:
            cfg.display_derivation(s)
            cfg.display_rightmost_derivation(s)

    # --- Sarcina 5: Bonus ---
    print("\n[Sarcina 5] Bonus: Recognizer pentru L = {a^n b^n c^n | n >= 1}:")
    bonus_strings = ["abc", "aabbcc", "aaabbbccc", "ab", "acb", "aabbc", "aaabbb"]
    for s in bonus_strings:
        is_member = recognize_an_bn_cn(s)
        print(f"Este '{s}' în L = {{a^n b^n c^n | n >= 1}}? -> {is_member}")
    

if __name__ == "__main__":
    main()
