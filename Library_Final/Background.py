import PySimpleGUI as sg

from Files.Background import Books, Pricing, sortBooks, sortPublishers, getMostProfitBook, getMostPopularBook

usernames = ['user', 'user2']
passwords = ['user', 'user2']


def signup(username, password):
    usernames.append(username)
    passwords.append(password)


def signin(username, password):
    i = 0
    for i in range(len(usernames)):
        if username == usernames[i]:
            break
    if password == passwords[i]:
        return True
    else:
        return False


memberName = 'name'

obj = Books()

pricingobj = Pricing()


def getindex(vals):
    booknames = obj.all_Books()
    for i in range(len(booknames)):
        if vals == booknames[i]:
            return i


def layouts():
    layout_main = [[sg.Text('Welcome to the library! ')],
                   [sg.Button('Login'), sg.Button('Sign up'), sg.Button('Cancel')]]

    layout_login = [[sg.Text('Name: ',size=(10,1)), sg.InputText(key='name')],
                    [sg.Text('Password: ',size=(10,1)), sg.InputText(password_char='*', key='pass')],
                    [sg.Button('Confirm'), sg.Button('Return to signup')]]

    layout_signup = [[sg.Text('Name:', size=[10, 1]), sg.InputText(key='suname')],
                     [sg.Text('Password:', size=[10, 1]), sg.InputText(password_char='*', key='supass')],
                     [sg.Text('Address:', size=[10, 1]), sg.InputText(key='suaddress')],
                     [sg.Text('Phone:', size=[10, 1]), sg.InputText(key='suphone')],
                     [sg.Button('Confirm and login'), sg.Button('Return to login')]]

    layout_menu = [[sg.Text('Book of the day!: Lord of the ring 1 (-25%!)')],
                   [sg.Button('List books', size=(25, 1))],
                   [sg.Button('Cart', size=(25, 1))],
                   [sg.Button('Sign out', size=(25, 1))]]
    layout_menu_admin = [[sg.Button('Add book', size=(25, 1))],
                         [sg.Button('Statistics', size=(25, 1))],
                         [sg.Button('Log out', size=(25, 1))]]

    layout_books = [[sg.Combo(obj.all_Books(), default_value='Select book', size=(31, 1), key='Choice')],
                    [sg.Spin([i for i in range(1, 51)], initial_value=1, size=(2, 1), key='amount'), sg.Text('Amount')],
                    [sg.Button('Add to cart'), sg.Button('Show book info'), sg.Button('Return')]]

    layout_cart = [[sg.Output((70, 20))],
                   [sg.Button('Proceed and buy'), sg.Button('Return to menu')]]

    layout_stats = [[sg.Text('Total sales: ',size=(25,1)), sg.Text(obj.total_sales, size=(20, 1), key='totalSales')],
                    [sg.Text('Total Profit/loss:',size=(25,1)), sg.Text(obj.total_profit, size=(20, 1), key='totalProfit')],
                    [sg.Text('Most popular book: ',size=(25,1)), sg.Text(getMostPopularBook(), size=(20, 1), key='getMostPopBook')],
                    [sg.Text('Highest profit: ',size=(25,1)), sg.Text(getMostProfitBook(), size=(20, 1), key='getMostProfit')],
                    [sg.Text('Publisher ranking: ',size=(25,1)),
                     sg.Multiline(sortPublishers(), key='sortPublishers')],
                    [sg.Text('Book rankin based on profit: ',size=(25,1)), sg.Multiline(sortBooks(), key='sortBooks')],
                    [sg.Button('Return to admin menu')]]

    mainCol = sg.Column(layout_main, key='panel_main')
    loginCol = sg.Column(layout_login, key='panel_login', visible=False)
    signupCol = sg.Column(layout_signup, key='panel_signup', visible=False)
    menuCol = sg.Column(layout_menu, key='panel_menu', visible=False)
    booksCol = sg.Column(layout_books, key='panel_books', visible=False)
    cartCol = sg.Column(layout_cart, key='panel_cart', visible=False)
    adminCol = sg.Column(layout_menu_admin, key='panel_admin', visible=False)
    statsCol = sg.Column(layout_stats, key='panel_stats', visible=False)

    panel = [
        [sg.Pane([mainCol, loginCol, signupCol, menuCol, booksCol, cartCol, adminCol, statsCol], relief=sg.RELIEF_FLAT)]
    ]
    return panel


sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
# Create the Window
window = sg.Window('Book library',default_element_size=(25,1)).Layout(layouts())


# Event Loop to process "events" and get the "values" of the inputs
def mainUI():
    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            break
        if event in ('Login', 'Return to login', 'Sign out', 'Log out'):
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=False)
            window['panel_login'].update(visible=True)
            window['panel_menu'].update(visible=False)
            window['panel_books'].update(visible=False)
            window['panel_cart'].update(visible=False)
            window['panel_admin'].update(visible=False)
        if event in ('Sign up', 'Return to signup'):
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=True)
            window['panel_login'].update(visible=False)
            window['panel_menu'].update(visible=False)
            window['panel_books'].update(visible=False)
            window['panel_cart'].update(visible=False)
        if event in ('Confirm', 'Return to admin menu'):
            if values['name'] == 'admin' and values['pass'] == 'admin':
                window['totalSales'].update(obj.total_sales)
                window['totalProfit'].update(obj.total_profit)
                window['getMostPopBook'].update(getMostPopularBook())
                window['getMostProfit'].update(getMostProfitBook())
                window['panel_main'].update(visible=False)
                window['panel_signup'].update(visible=False)
                window['panel_login'].update(visible=False)
                window['panel_menu'].update(visible=False)
                window['panel_books'].update(visible=False)
                window['panel_cart'].update(visible=False)
                window['panel_admin'].update(visible=True)
                window['panel_stats'].update(visible=False)
            elif signin(values['name'], values['pass']):
                window['panel_main'].update(visible=False)
                window['panel_signup'].update(visible=False)
                window['panel_login'].update(visible=False)
                window['panel_menu'].update(visible=True)
                window['panel_books'].update(visible=False)
                window['panel_cart'].update(visible=False)
            else:
                sg.popup('Wrong login credentials!')
        if event in ('Return', 'Return to menu'):
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=False)
            window['panel_login'].update(visible=False)
            window['panel_menu'].update(visible=True)
            window['panel_books'].update(visible=False)
            window['panel_cart'].update(visible=False)
        if event == 'Cart':
            if pricingobj.getTotal() > 0:
                print('Total cost: $', pricingobj.getTotal())
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=False)
            window['panel_login'].update(visible=False)
            window['panel_menu'].update(visible=False)
            window['panel_books'].update(visible=False)
            window['panel_cart'].update(visible=True)
        if event == 'List books':
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=False)
            window['panel_login'].update(visible=False)
            window['panel_menu'].update(visible=False)
            window['panel_books'].update(visible=True)
            window['panel_cart'].update(visible=False)
        if event == 'Add to cart':
            print('\nBook title: ', values['Choice'], ' , Amount: ', values['amount'], ' , Price: $',
                  pricingobj.buyBook(getindex(values['Choice']), values['amount']))
        if event == 'Show book info':
            sg.popup_scrolled(obj.getBookInfo(getindex(values['Choice'])))
        if event == 'Proceed and buy':
            obj.total_sales += 1
            sg.popup('Success!, the book will be shipped to your address as soon as possible',
                     title='Purchase successful!')
            pricingobj.resetTotalPrice()
            print('\n', '=' * 60, '\n')
            window.Refresh()
        if event == 'Confirm and login':
            signup(values['suname'], values['supass'])
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=False)
            window['panel_login'].update(visible=True)
            window['panel_menu'].update(visible=False)
            window['panel_books'].update(visible=False)
            window['panel_cart'].update(visible=False)
        if event == 'Statistics':
            window['sortPublishers'].update(sortPublishers())
            window['sortBooks'].update(sortBooks())
            window['panel_main'].update(visible=False)
            window['panel_signup'].update(visible=False)
            window['panel_login'].update(visible=False)
            window['panel_menu'].update(visible=False)
            window['panel_books'].update(visible=False)
            window['panel_cart'].update(visible=False)
            window['panel_admin'].update(visible=False)
            window['panel_stats'].update(visible=True)

    window.close()


mainUI()
