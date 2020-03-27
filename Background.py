import PySimpleGUI as sg


def getrawcost(i):
    return int(Books.books[i][8])


def getcost(i):
    return int(Books.books[i][1])


def getMostPopularBook():
    best = 0
    bookName = ''
    for i in range(len(Books.books)):
        if int(Books.books[i][4]) > best:
            best = Books.books[i][4]
            bookName = Books.books[i][0]
    else:
        if best == 0:
            return 'N/A'
    return bookName


def sortPublishers():
    newPublishers = [[' ', 0] for i in range(len(Books.books))]
    for i in range(len(Books.books)):
        newPublishers[i][0] = Books.books[i][2]
        newPublishers[i][1] = int(Books.books[i][4])
    sorted(newPublishers, key=lambda j: j[1])
    for i in range(len(newPublishers)):
        newPublishers[i] = ' '.join([str(i + 1), ':', newPublishers[i][0], 'with', str(newPublishers[i][1]), ' sales,'])
    return ' '.join(newPublishers)


def sortBooks():
    newBooks = [[' ', 0] for i in range(len(Books.books))]
    for i in range(len(Books.books)):
        newBooks[i][0] = Books.books[i][0]
        newBooks[i][1] = int(Books.books[i][9])
    sorted(newBooks, key=lambda j: j[1])
    for i in range(len(newBooks)):
        newBooks[i] = ' '.join([str(i + 1), ':', newBooks[i][0], 'with $', str(newBooks[i][1]), ' total profit,'])
    return ' '.join(newBooks)


def getMostProfitBook():
    best = 0
    bookName = ' '
    for i in range(len(Books.books)):
        if int(Books.books[i][9]) > best:
            best = Books.books[i][9]
            bookName = Books.books[i][0]
    else:
        if best == 0:
            return 'N/A'
    return bookName


class Books:
    # Bookname =0     ,cost =1,Publisher =2,authorname =3,purchased=4 ,ISBN=5 ,type= 6,Year of publication=7,
    # Book Original Price=8, Total Profit=9
    with open(sg.popup_get_file('Select the file that contains books info')) as textFile:
        books = [line.split() for line in textFile]

    for i in range(len(books)):
        books[i].extend(['0'])
    most_sell_amnt = 0
    most_sell_value = 0
    total_books_sold = 0
    total_sales = 0
    net_gain = 0
    total_cost = 0

    def __init__(self):
        print('Constructor Called')

    def __del__(self):
        print('Destructor called')

    for i in range(len(books)):
        total_cost += int(books[i][8])
    total_profit = net_gain - total_cost

    def purchased(self, i):
        cc = self.books[i][4]
        return cc

    def all_Books(self):
        vals = []

        for i in range(len(self.books)):
            vals.insert(i, self.books[i][0])
        return vals

    # Bookname =0     ,cost =1,Publisher =2,authorname =3,purchased=4 ,ISBN=5 ,type= 6,Year of publication=7
    def getBookInfo(self, i):
        return ' '.join(['Title: ', self.books[i][0], ', Publisher: ', self.books[i][2],
                         ', ISBN: ', self.books[i][5], ', Sell price: ', '$' + self.books[i][1], ', Type: ',
                         self.books[i][6],
                         ', Year of publication: ', self.books[i][7], ', Times purchased: ', str(self.books[i][4]),
                         ',Cost: ', '$' + self.books[i][8]])

    def getMosSoldtBook(self):

        for i in range(19):
            print("Book Name:", self.books[i][0], " sold :", self.books[i][4], " publisher:", self.books[i][2])


class Pricing(Books):
    re = [0]
    VAT = .05
    promocodes = ['promo', 'discounts']
    postalCharge = 70

    total = 0

    def buyBook(self, index, amount):
        x = int(Books.books[index][1])
        price = float((x + x * Pricing.VAT + Pricing.postalCharge) * amount)
        # promo = input("type your promo code if you have it, else type in 0: ")
        # if promo in Pricing.promocodes:
        #   price -= price * .25
        x = Pricing.re[0] + price
        Pricing.re[0] = x
        t = int(Books.books[index][4]) + amount
        Books.books[index][4] = t

        self.re + [Books.books[index][0]]
        self.re + [Books.books[index][1]]

        self.re.insert(1, Books.books[index][0])
        self.re.insert(2, Books.books[index][1])

        self.total += price
        y = int(Books.books[index][9])
        Books.total_sales += amount
        Books.books[index][9] = y + price
        Books.total_profit += price - getrawcost(index)

        return price

    def getAllOprstion(self):
        i = 1
        run = True

        for i in range(100):
            print(self.re[i])

        return self.re[0]

    def getTotal(self):
        return self.total

    def resetTotalPrice(self):
        self.total = 0
        return

