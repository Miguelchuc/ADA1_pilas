class Pila:
    def __init__(self):
        self.disc = []

    def añadir(self, disc):
        self.disc.append(disc)

    def quitar(self):
        if not self.esta_vacia():
            return self.disc.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.disc[-1]
        return None

    def esta_vacia(self):
        return len(self.disc) == 0

    def __len__(self):
        return len(self.disc)


def hanoi(i, ini, fin, auxi):
    if i > 0:
        hanoi(i - 1, ini, auxi, fin)
        
        
        disco = ini.quitar()
        fin.añadir(disco)
        print(f"Se movió disco {disco} de torre {ini.nombre} a torre {fin.nombre}")
        
        hanoi(i - 1, auxi, fin, ini)


def main():
    
    t_a = Pila()
    t_b = Pila()
    t_c = Pila()
    t_a.nombre = "A"
    t_b.nombre = "B"
    t_c.nombre = "C"

    
    for disco in range(6, 0, -1 ):  
        t_a.añadir(disco)

    print("Estado inicial:")
    print("Torre A:", t_a.disc)  
    print("Torre B:", t_b.disc)
    print("Torre C:", t_c.disc)
    print()

    
    hanoi(len(t_a.disc), t_a, t_c, t_b)

    print("\nEstado final:")
    print("Torre A:", t_a.disc)  
    print("Torre B:", t_b.disc)
    print("Torre C:", t_c.disc)
    print("Movimientos realizados:", pow(2, 3) - 1) 


if __name__ == "__main__":
    main()



