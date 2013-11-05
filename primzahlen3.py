#primzahlen ausgeben
#For-Schleife mit Else anstelle Flag
#Wenn eine For-Schleife ein Else am Ende hat, wird der dortige Teil ausgeführt, wenn die For-Schleife ohne Break durchläuft

zahlen = list(range(1, 101))
primzahlen = []

for zahl in zahlen: 													#Für jede 'Zahl' in den 'Zahlen': mach etwas...
	print(zahl, end=": ") 												#'Zahl' ausgeben (end= optische Änderunge, : statt nl)
	if zahl > 1: 														#Die 'Zahl' muss größer sein als 1
																		#Testen ob durch Primzahl ohne Rest teilbar -> keine Primzahl
																		#Nested Loop: For-Schleife in einer For-Schleife beginnt hier:
		for primzahl in primzahlen: 									#Es wird über alle 'primzahlen' iteriert (iterable)
			if zahl%primzahl == 0: 										#Zahl durch Primzahl ohne Rest teilbar? (Modulo (%), ergibt Rest einer Division)
				print("Keine Primzahl, weil durch",
				      primzahl, "teilbar.")
				break													#Bricht aus der Schleife aus, weil Teiler gefunden (wird schneller + lesbarer)
			else: 														#Wenn es nicht durch die primzahl ohne Rest teilbar ist, dann tue:
				print("Ist nicht durch", primzahl, "teilbar.")
		else:															#Dieses Else gehört zur For-Schleife
			print("Primzahl gefunden.")									#Primzahl gefunden, da Primzahl-Schleife komplett ohne break durchgelaufen ist.
			primzahlen.append(zahl)													
	else: 
		print() 														#Ist die 'Zahl' 1, dann wird sie separat ausgeben
print("Ich habe folgende Primzahlen gefunden:")	
print(primzahlen)
