#write functions here, don't add input('') statements here!
def test_config():
    return True

def areValues(*numCollection):
    for num in numCollection:
        try:
            float(num)
        except:
            return(False)
            break
    return(True)

def listMaker(*numCollection):
    list = []
    for num in numCollection:
        list.append(float(num))
    list.sort()
    return(list)

def displayList(list):
    print('_________________')
    print('Lowest Number: '+str(min(list)))
    print('Highest Number: '+str(max(list)))
    print('Sum of List: '+str(sum(list)))
    print('Average Value: '+str(sum(list)))
    print('')
