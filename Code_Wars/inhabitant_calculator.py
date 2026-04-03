def nb_year(p0, percent, aug, p):
    years_needed = 0
    inhabitants = p0
    print(f"starting : {inhabitants}")
    
    while inhabitants < p:
        inhabitants = inhabitants + int(inhabitants * (percent / 100)) + aug
        
        
        print(f"acc : {inhabitants}")
        years_needed += 1
   
    return years_needed

print(nb_year(1500, 5, 100, 5000))