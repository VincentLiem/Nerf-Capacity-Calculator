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
if game_time > 0:
    ammo_per_minutes = total_ammo / game_time
    print(str(ammo_per_minutes) + " shots per minute")
else:
    print("No game time entered")
save_file = input("Save as text file? (Y/N) >> ")
if save_file.lower() == "y" or save_file.lower() == "yes":
    blaster_name = input("Blaster name >> ")
    blaster_name = blaster_name[0].upper() + blaster_name[1:]
    with open(blaster_name + ' Capacity.txt', 'w') as save:
        save.write(blaster_name + '\n')
        save.write(str(total_ammo) + ' ammo held total')
else:
    pass
