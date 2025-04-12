def game(sheldon, raj, case):
    options = [
        ['tesoura', 'papel'],
        ['papel', 'pedra'],
        ['pedra', 'lagarto'],
        ['lagarto', 'Spock'],
        ['Spock', 'tesoura'],
        ['tesoura', 'lagarto'],
        ['lagarto', 'papel'],
        ['papel', 'Spock'],
        ['Spock', 'pedra'],
        ['pedra', 'tesoura'],
    ]
    result = f'Caso #{case}: De novo!'
    for i in options:
        if i[0] == sheldon and i[1] == raj:
            result = f'Caso #{case}: Bazinga!'
        if i[0] == raj and i[1] == sheldon:
            result = f'Caso #{case}: Raj trapaceou!'
    
    return result

NC = int(input())
for i in range(1, 1 +NC):
    entry = list(map(str, input().split()))
    sheldon = entry[0]
    raj = entry[1]
    print(game(sheldon, raj, i))
    