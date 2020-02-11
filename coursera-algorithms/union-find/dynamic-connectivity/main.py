from quick_find import QF
from quick_union import QU
from quick_union_v2 import QUv2

def main():
    while True:
        try:
            N = int(input('Please enter a number for the number of values: '))
            qu = QUv2(N)
            print('''
            Please enter in a series of values that will be connected. 
            Format should look as such: 0 1\n
                ''')
            while True:
                try:
                    print(qu)
                    pair = input('Please enter a pair: ')
                    pair_tuple = tuple(pair.split())
                    if len(pair_tuple) != 2:
                        raise ValueError
                    p = int(pair_tuple[0])
                    q = int(pair_tuple[1])
                    if not qu.connected(p, q):
                        qu.union(p, q)
                        print('{} and {} are now connected'.format(p, q))
                except ValueError:
                    print('Please enter in a valid pair!') 
                    continue 
                no_more_pairs = input('Would you like to add any more connections (type y or n): ')
                if no_more_pairs.lower() not in ('y', 'yes'):   
                    break
        except ValueError:
            print('Please enter in a number!')
        break

if __name__ == "__main__":
    main()