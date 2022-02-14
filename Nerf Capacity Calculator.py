internal_clip = input("Internal clip capacity? >> ")
different_mag = int(input("How many different magazine/speedloader sizes? >> "))
total_ammo = int(internal_clip)
mag = int(0)
while mag < different_mag:
    mag_capacity = int(input("Ammo capacity of magazine/speedloader size " + str(mag + 1) + "? >> "))
    ammo_storage = int(input("How many " + str(mag_capacity) + " capacity magazine/speedloaders? >> "))
    total_ammo += mag_capacity * ammo_storage
    mag += 1
print(str(total_ammo) + " ammo held")
game_time = int(input("How many minutes is the game? >> "))
ammo_per_minutes = total_ammo / game_time
print(str(ammo_per_minutes) + " shots per minute")

save_file = input("Save as text file? (Y/N) >> ")
if save_file == "Y" or save_file == "y":
    blaster_name = input("Blaster name >> ")
    with open(blaster_name + ' Capacity.txt', 'w') as save:
        save.write(str(total_ammo) + " ammo held total\n")
        save.write(str(ammo_per_minutes) + " shots per minute for a " + str(game_time) + " minute game.")
else:
    pass
