import os
import pickle


# veikia
def prideti_darb():
    with open('darbuotojai.pickle', mode='rb') as file:
        darbuotojai = pickle.load(file)

    while True:
        vardas = input('Darbuotojo vardas: ')
        pareigos = input('Pareigos: ')
        alga = input('Alga: ')
        try:
            alga = int(alga)
        except ValueError:
            print("Alga turi būti tik skaičiai. Bandykite dar kartą.")
            continue

        darbuotojai.append([vardas, pareigos, alga])

        testi = input('"Enter" prideti dar viena darbuotoja arba "q" iseiti: ')
        if testi == 'q':
            with open('darbuotojai.pickle', mode='wb') as file:
                pickle.dump(darbuotojai, file)
            print("Darbuotojai išsaugoti.")
            print()
            break
        else:
            continue


# veikia
def ziureti_darb():
    with open('darbuotojai.pickle', mode='rb') as file:
        # noinspection PyTypeChecker
        listas_2 = pickle.load(file)
    print(listas_2)

# veikia
def keisti_darb():
    darbuotojas = input('Darbuotojas: ')

    print('Keisti: \n'
          '1. Varda \n'
          '2. Pareigas\n'
          '3. Alga \n'
          '4. Grizti')

    while True:
        pasirinkimas = input('Pasirinkimas:')
        with open('darbuotojai.pickle', mode='rb') as file:
            # noinspection PyTypeChecker
            darbuotojai = pickle.load(file)

        if pasirinkimas == '1':
            for i, darbuotojas_data in enumerate(darbuotojai):
                vardas, pareigos, alga = darbuotojas_data
                if vardas == darbuotojas:
                    naujas_vardas = input('Ivesti pataisyta varda: ')
                    darbuotojai[i] = (naujas_vardas, pareigos, alga)
                    break

            with open('darbuotojai.pickle', mode='wb') as file:
                # noinspection PyTypeChecker
                pickle.dump(darbuotojai, file)

            break

        if pasirinkimas == '2':
            for i, darbuotojas_data in enumerate(darbuotojai):
                vardas, pareigos, alga = darbuotojas_data
                if vardas == darbuotojas:
                    naujos_pareigos = input('Ivesti naujas pareigas: ')
                    darbuotojai[i] = (vardas, naujos_pareigos, alga)
                    break

            with open('darbuotojai.pickle', mode='wb') as file:
                # noinspection PyTypeChecker
                pickle.dump(darbuotojai, file)

            break

        if pasirinkimas == '3':
            for i, darbuotojas_data in enumerate(darbuotojai):
                vardas, pareigos, alga = darbuotojas_data
                if vardas == darbuotojas:
                    nauja_alga = input('Ivesti nauja alga: ')
                    # Update the list element
                    darbuotojai[i] = (vardas, pareigos, nauja_alga)
                    break

            with open('darbuotojai.pickle', mode='wb') as file:
                # noinspection PyTypeChecker
                pickle.dump(darbuotojai, file)

            break

        if pasirinkimas == '4':
            break


def atleisti():
    darbuotojas = input('Darbuotojas: ')
    with open('darbuotojai.pickle', mode='rb') as file:
        # noinspection PyTypeChecker
        darbuotojai = pickle.load(file)

    for i, darbuotojas_data in enumerate(darbuotojai):
        vardas, pareigos, alga = darbuotojas_data
        if vardas == darbuotojas:
            del darbuotojai[i]
            print('Pasalintas')
            break

    with open('darbuotojai.pickle', mode='wb') as file:
        # noinspection PyTypeChecker
        pickle.dump(darbuotojai, file)


def main():
    print('Sveiki atvyke!')
    while True:

        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
        print('| 1. Ivesti nauja darbuotoja    |\n'
              '| 2. Redaguoti darbuotoja       |\n'
              '| 3. Ziureti darbuotojus        |\n'
              '| 4. Atleisti darbuotoja        |\n'
              '| q - iseiti                    |')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
        print()
        pasirinkimas = input('Pasirinkimas: ')

        if pasirinkimas == '1':
            darbuotojai = prideti_darb()

        if pasirinkimas == '2':
            darbuotojai = keisti_darb()

        if pasirinkimas == '3':
            ziureti_darb()
            grizti = input('Enter grizti')
            if grizti == '':
                continue

        if pasirinkimas == '4':
            darbuotojai = atleisti()

        if pasirinkimas == 'q':
            break


if __name__ == '__main__':
    main()
