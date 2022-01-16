internal_clip = input("Internal clip capacity? >> ")
different_mag = int(input("How many different magazine/speedloader sizes? >> "))
total_ammo = int(internal_clip)
mag = int(0)
while mag < different_mag:
    mag_capacity = int(input("Ammo capacity of magazine/speedloader size " + str(mag+1) + "? >> "))
    ammo_storage = int(input("How many "+ str(mag_capacity) +" capacity magazine/speedloaders? >> "))
    total_ammo += mag_capacity * ammo_storage
    mag += 1
print(str(total_ammo) + " ammo held")
game_time = int(input("How many minutes is the game? >> "))
ammo_per_minutes = total_ammo / game_time
print(str(ammo_per_minutes) + " shots per minute")
