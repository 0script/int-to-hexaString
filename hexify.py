import sys

HEXA={
    '10' :'A',
    '11' :'B',
    '12' :'C',
    '13' :'D',
    '14' :'E',
    '15' :'F',
}

def returnQuoReste(number,diviseur):
    ''' perform arithmetique division return quotien and reste '''

    reste=int(number)
    quotient=0

    while reste>=diviseur:
        reste=reste-diviseur
        quotient=quotient+1

    return {'quotien':quotient,'reste':reste}

def hexify(int_number):
    '''
        change integer into a string hexa using method explained in 
        the video : https://www.youtube.com/watch?v=QJW6qnfhC70&t=313s
    '''
    
    number=int_number
    restes=[]
    while number:
        qr=returnQuoReste(number,16)
        number=qr['quotien']
        restes.append(qr['reste'])

    restes=[str(i) for i in restes[::-1]]
    
    restes=[i if i not in HEXA.keys() else HEXA[i] for i in restes ]
    
    return ''.join(restes)

#################################################

if __name__=='__main__':
    try:
        print(hexify(sys.argv[1]))
    except Exception as e:
        print('Error : ',e)
        exit(1)