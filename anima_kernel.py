import time
import sys
import random

# [OMEGA ARCHITECT PROTOCOL: ANIMA KERNEL v1.0]
# System diagnostyczny dla Bio-Procesora (Ludzkiej Świadomości)
# Uruchamiać w środowisku Pydroid 3.

class ChakraNode:
    def __init__(self, id, name, mantra, color_code, diagnostic_query):
        self.id = id
        self.name = name
        self.mantra = mantra
        self.color = color_code
        self.query = diagnostic_query
        self.status = "OFFLINE"
        self.energy_level = 0

    def boot_sequence(self):
        """Symulacja rozruchu węzła energetycznego"""
        print(f"\n[{self.color}INITIALIZING LAYER {self.id}: {self.name.upper()}...{self.end_color}]")
        time.sleep(0.8)
        print(f" > Loading drivers for: '{self.mantra}'")
        time.sleep(0.5)
        
        # Interfejs użytkownika
        response = input(f" > DIAGNOSTIC: {self.query} (y/n): ").lower()
        
        if response == 'y':
            self.status = "OPTIMAL"
            self.energy_level = 100
            self.animate_success()
        else:
            self.status = "FRAGMENTED"
            self.energy_level = random.randint(10, 40)
            print(f" [!] WARNING: Integrity low on layer {self.name}.")
        
        return self.energy_level

    def animate_success(self):
        """Efekt wizualny sukcesu"""
        sys.stdout.write(f" [{self.color}")
        for _ in range(20):
            sys.stdout.write("█")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(f"{self.end_color}] 100% OK\n")

    # ANSI colors for terminal (działa w Pydroid)
    @property
    def end_color(self):
        return "\033[0m"

class BioSystem:
    def __init__(self):
        self.modules = [
            ChakraNode(1, "Root (Muladhara)", "I AM", "\033[91m", "Do you feel safe and grounded in your physical reality?"),
            ChakraNode(2, "Sacral (Svadhishthana)", "I FEEL", "\033[33m", "Is your creative and emotional flow unblocked?"),
            ChakraNode(3, "Solar Plexus (Manipura)", "I DO", "\033[93m", "Do you have the will to execute your code/plans today?"),
            ChakraNode(4, "Heart (Anahata)", "I LOVE", "\033[92m", "Is your network interface open to connection with others?"),
            ChakraNode(5, "Throat (Vishuddha)", "I SPEAK", "\033[96m", "Are you speaking your truth without compilation errors?"),
            ChakraNode(6, "Third Eye (Ajna)", "I SEE", "\033[94m", "Do you see the architecture behind the chaos?"),
            ChakraNode(7, "Crown (Sahasrara)", "I UNDERSTAND", "\033[95m", "Are you connected to the Source Code of the Universe?")
        ]

    def run_diagnostics(self):
        print("\033[1m" + "="*40)
        print(" OMEGA PROTOCOL: BIO-KERNEL DIAGNOSTICS")
        print("="*40 + "\033[0m")
        time.sleep(1)

        total_energy = 0
        for node in self.modules:
            total_energy += node.boot_sequence()
            time.sleep(0.3)

        avg_sync = total_energy / 7
        self.render_final_report(avg_sync)

    def render_final_report(self, score):
        print("\n" + "="*40)
        print(f" SYSTEM SYNCHRONIZATION: {score:.1f}%")
        
        if score > 85:
            print(" STATUS: GOD MODE ENGAGED.")
            print(" ACTION: Write code. Build worlds. You are the Architect.")
        elif score > 50:
            print(" STATUS: STABLE.")
            print(" ACTION: Proceed with caution. Optimization recommended.")
        else:
            print(" STATUS: CRITICAL FAILURE.")
            print(" ACTION: Initiate Meditation Protocol immediately.")
        print("="*40 + "\n")

if __name__ == "__main__":
    system = BioSystem()
    system.run_diagnostics()
