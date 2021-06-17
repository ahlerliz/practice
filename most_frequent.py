lista = [0, 1, 3, 2, 23, 43, 2, 1, 5, 2, 5, 2, 56, 23, 0, -1, 2, 2]
listb = [4, 0, 1, 0, 4, 4, 4, 4, 0, 1, 1, 1,-6, 7]
def main(list):
    final = {}
    x = 0 
    while x < len(list):
        if list[x] not in final:
            final[list[x]] = 1
        else:
            final[list[x]] += 1 
        x += 1
    final_keys = final.keys()
    final_values = final.values()
    highest_value = final_values[0]
    y = 1
    while y < len(final_values):
        if final_values[y] > highest_value:
            highest_value = final_values[y]
        y += 1
    test = final_values.index(highest_value)
    print final_keys[test]
    
    

if __name__ == "__main__":
    
    print "Most Frequent for a: " 
    str(main(lista))
    
    print "Most Frequent for b: " 
    str(main(listb))